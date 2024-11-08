
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow React to communicate with Flask

@app.route('/api/submit-url', methods=['POST'])
def submit_url():
    data = request.get_json()  # Get the JSON data from React
    user_url = data.get('url')  # Extract the URL
    print("Received URL:", user_url)  # Log the URL for now
    
    # For now, just return a success message
    return jsonify({"message": "URL received successfully!"}), 200

@app.route('/')
def home():
    return "Welcome to the Home Page!"

if __name__ == '__main__':
    app.run(debug=True)
