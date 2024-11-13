# app.py
from flask import Flask
from flask_cors import CORS
from routes.mcqRoutes import mcq_routes # Importing the mcq_routes blueprint

app = Flask(__name__)
CORS(app)  # Enable CORS to allow React to communicate with Flask

# Registering the blueprint from mcqRoutes
app.register_blueprint(mcq_routes, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to the Home Page!"

if __name__ == '__main__':
    app.run(debug=True)
