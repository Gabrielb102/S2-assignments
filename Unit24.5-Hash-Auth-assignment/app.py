from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, MODELNAME

app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET_KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///DATABASE NAME"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)