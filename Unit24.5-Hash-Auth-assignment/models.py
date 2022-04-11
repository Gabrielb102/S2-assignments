from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class MODELNAME(db.Model) :
    """WHAT DOES IT MODEL"""

    __tablename__="TABLE NAME"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=False, default='https://tinyurl.com/demo-cupcake')

    def __repr__(self) :
        c = self
        return f"HOW WOULD YOU REPRESENT YOUR MODEL"
