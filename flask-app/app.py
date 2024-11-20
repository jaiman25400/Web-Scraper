# app.py
from flask import Flask
from flask_cors import CORS
from routes.mcqRoutes import mcq_routes # Importing the mcq_routes blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Migrate
from models import db
import os


app = Flask(__name__)
CORS(app)  # Enable CORS to allow React to communicate with Flask

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

    
# Registering the blueprint from mcqRoutes
app.register_blueprint(mcq_routes, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to the Home Page!"

if __name__ == '__main__':
    app.run(debug=True)
