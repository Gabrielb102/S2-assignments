from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

CREATE SOME MODEL INSTANCES TO POPULATE YOUR DATABASE

db.session.add_all([LIST OF INSTANCES])
db.session.commit()