import requests
from bs4 import BeautifulSoup
from flask import Blueprint, request, jsonify
from util import classifyUser, generate_mcq_from_content
from models import db, URL, MCQ, UserResponse  # Import the database and models

# Create a Blueprint for MCQ-related routes
mcq_routes = Blueprint('mcq_routes', __name__)

@mcq_routes.route('/submit-url', methods=['POST'])
def submit_url():
    data = request.get_json()
    user_url = data.get('url')
    print("Received URL:", user_url)

    # Step 1: Check if the URL already exists in the database
    existing_url = URL.query.filter_by(url=user_url).first()

    if existing_url:
        # URL exists, retrieve related MCQ data
        mcq_data = MCQ.query.filter_by(url_id=existing_url.id).all()
        return jsonify({
            "message": "URL already exists in the database!",
            "url": existing_url.url,
            "title": existing_url.title,
            "mcq_data": [mcq.questions_data for mcq in mcq_data]
        }), 200

    # Step 2: If URL doesn't exist, scrape and generate new data
    try:
        response = requests.get(user_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to retrieve content from the URL", "details": str(e)}), 500

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title
    title = soup.title.string if soup.title else "No Title Found"

    # Extract main content
    content_text = soup.get_text(separator=" ")

    # Generate MCQs using OpenAI or your custom logic
    question_data = generate_mcq_from_content(title, content_text)

    if not question_data:
        return jsonify({"error": "Failed to generate question from content"}), 500

    # Step 3: Save new URL and MCQs to the database
    try:
        new_url = URL(url=user_url, title=title)
        db.session.add(new_url)
        db.session.flush()  # Ensure `new_url.id` is populated

        # Save MCQ data linked to the new URL
        for question in question_data:
            mcq = MCQ(url_id=new_url.id, questions_data=question)
            db.session.add(mcq)

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to save data to the database", "details": str(e)}), 500

    return jsonify({
        "message": "URL and MCQs saved successfully!",
        "url": new_url.url,
        "title": new_url.title,
        "mcq_data": question_data
    }), 201

    
@mcq_routes.route('/submit-answers', methods=['POST'])
def submit_answers():
    data = request.get_json()
    print("User Res Data : ",data)
    url = data.get("url")
    responses = data.get("answers")
    
    if not url or not responses:
        return jsonify({"error": "Invalid payload. Ensure 'url' and 'answers' are provided."}), 400

    # Fetch the corresponding URL record
    url_record = URL.query.filter_by(url=url).first()
    if not url_record:
        return jsonify({"error": "URL not found in the database"}), 404

    try:
        # Save user response
        user_response = UserResponse(
            url_id=url_record.id,
            response_data=responses
        )
        db.session.add(user_response)
        db.session.commit()

        result_data = classifyUser(responses)
        return jsonify({"message": "Answer received successfully!","Result ":result_data}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to save responses", "details": str(e)}), 500