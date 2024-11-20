from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Table to store URLs
class URL(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(2048), unique=True, nullable=False)  # Store unique URLs
    title = db.Column(db.String(512), nullable=True)  # Page title
    hit_count = db.Column(db.Integer, nullable=True ,default = 0)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Relationship to access MCQs linked to this URL
    mcqs = db.relationship('MCQ', backref='url', cascade='all, delete-orphan')

# Table to store MCQs as JSON
class MCQ(db.Model):
    __tablename__ = 'mcqs'
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey('urls.id'), nullable=False)  # Foreign key to link to URLs
    questions_data = db.Column(db.JSON, nullable=False)  # Store questions and options as JSON
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Table to store user responses
class UserResponse(db.Model):
    __tablename__ = 'user_responses'
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey('urls.id'), nullable=False)  # Foreign key to link to URLs
    classify_user = db.Column(db.String(128), nullable=True)  # Track individual users (e.g., session ID)
    response_data = db.Column(db.JSON, nullable=False)  # Store user answers in JSON
    created_at = db.Column(db.DateTime, server_default=db.func.now())
