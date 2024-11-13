import requests
from bs4 import BeautifulSoup
from flask import Blueprint, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Create a Blueprint for MCQ-related routes
mcq_routes = Blueprint('mcq_routes', __name__)

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def process_question_data(raw_data):
    # Split the raw data by '###', which separates the questions
    question_blocks = raw_data.strip().split("###")
    print("blocks :", question_blocks)
    
    questions_list = []
    
    for block in question_blocks:
        # Trim leading/trailing whitespace
        block = block.strip()
        
        if not block:
            continue  # Skip empty blocks
        
        # Split the block into lines (first line is the question, subsequent lines are options)
        lines = block.split("\n")
        
        question_obj = {}
        
        # The first line is the question
        question_obj['question'] = lines[0].strip()
        print("ques obj :", question_obj)
        
        # The following lines are options (A, B, C, D, etc.)
        options = {}
        for line in lines[1:]:
            # Each option starts with 'A.', 'B.', 'C.', 'D.', etc.
            if line.startswith("A.") or line.startswith("B.") or line.startswith("C.") or line.startswith("D."):
                option_label = line.split(".")[0].strip()  # Option A, Option B, etc.
                option_text = line.split(".")[1].strip()  # Option text
                options[option_label] = option_text
        
        question_obj['options'] = options
        
        # Add this question object to the list
        questions_list.append(question_obj)
    
    print("Final List :", questions_list)
    return questions_list  # Return as a list of dictionaries



def generate_mcq_from_content(title,context):
    # Define a prompt that asks OpenAI to generate MCQs based on website content
    prompt = f"""
    Given the following context scraped from a website, generate 2 meaningful multiple-choice question (MCQ) with 4 options. 
    The aim is to classify the visitor’s intent. For example, if someone enters apple.com, your program should return a question like: 'Which product category
    are you interested in?' with options such as 'A. Mac, B. iPad, C. iPhone, D. Watch.' These options should reflect the primary categories or content themes 
    found on the input site. 
    
    So the question and options should be more like what a user choose among those rather than any right or wrong quesions.


    Page: Tile : "{title}"
    Page Context : {context}"

    Note : seperate each question with 2 new lines and use ### to seperate each questions from start and options to start with A. , B. , C. ,D. 
    """

    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        question_data = completion.choices[0].message.content
        
        print("Ques Data :",question_data)
        
        processed_data = process_question_data(question_data)
        
        return processed_data
    except Exception as e:
        print(f"Error while calling OpenAI API: {e}")
        return None



@mcq_routes.route('/submit-url', methods=['POST'])
def submit_url():
    data = request.get_json()
    user_url = data.get('url')
    print("Received URL:", user_url)

    # Step 1: Scrape the main page content
    try:
        response = requests.get(user_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to retrieve content from the URL", "details": str(e)}), 500

    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 2: Extract the title of the page
    title = soup.title.string if soup.title else "No Title Found"

    # Step 3: Extract main content text
    paragraphs = soup.find_all('p')
    content_text = " ".join([p.get_text() for p in paragraphs])
    
    print(content_text)

    # Generate MCQs using OpenAI based on scraped content
    question_data = generate_mcq_from_content(title,content_text)

    if question_data:
        # Return the generated question and options as a response
        return jsonify({"message": "Questions generated successfully!", "question_data": question_data}), 200
    else:
        return jsonify({"error": "Failed to generate question from content"}), 500