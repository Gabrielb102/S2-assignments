from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model) :
    """Users for the site"""

    __tablename__="users"

    username = db.Column(db.String, primary_key=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

    def __repr__(self) :
        u = self
        return f"User {u.id}: {u.username}: {u.first_name} {u.last_name}"
