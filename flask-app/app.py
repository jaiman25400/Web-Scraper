# app.py
from flask import Flask,request
from flask_cors import CORS
from routes.mcqRoutes import mcq_routes  # Importing the mcq_routes blueprint
from flask_migrate import Migrate  # Import Migrate
from models import db
from sqlalchemy.sql import text  # Import text for raw SQL
import os

app = Flask(__name__)
CORS(app)  # Enable CORS to allow React to communicate with Flask

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Helper function to check DB connection
def check_db_connection():
    try:
        with app.app_context():
            # Use text() for the raw SQL expression
            db.session.execute(text('SELECT 1'))
        return True
    except Exception as e:
        print(f"Database connection error: {e}")
        return False

# Registering the blueprint from mcqRoutes
app.register_blueprint(mcq_routes, url_prefix='/api')

@app.route('/')
def home():
    if check_db_connection():
        return (f"Welcome to the Home Page! Database connected successfully!<br>"
                f"App is running on host: {request.host}")
    else:
        return (f"Welcome to the Home Page! Database connection failed.<br>"
                f"App is running on host: {request.host}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
