"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class User(db.Model) :
    """User"""

    __tablename__ = "users"

    id = db.Column(db.Integer,
        primary_key=True,
        autoincrement=True)
    first_name = db.Column(db.String(50),
        nullable=False)
    last_name = db.Column(db.String(50),
        nullable = True)
    image_url = db.Column(db.String, 
        nullable=False,
        default='http://127.0.0.1:5000/static/default-profile-pic.png')

    def __repr__(self) :
        u = self
        return f"<user id={u.id} name={u.first_name} {u.last_name}>"

class Post(db.Model) :
    """Post"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String, nullable = False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    author = db.relationship('User', backref='posts')

