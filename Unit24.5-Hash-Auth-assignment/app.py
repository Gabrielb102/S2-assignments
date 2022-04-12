from flask import Flask, request, flash, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from forms import RegisterForm, LoginForm
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///users"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

bcrypt = Bcrypt()

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/', methods=['GET'])
def redirect_to_register() :
    """Redirect to /register"""
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def present_handle_registration() : 
    """Show a form that when submitted will register/create a user. 
    This form accepts a username, password, email, first_name, and last_name. 
    Redirect to user-only content if successful."""

    form = RegisterForm()
    if form.validate_on_submit() :
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        hashed = bcrypt.generate_password_hash(password)
        user = User(username=username, password=hashed, email=email, first_name=first_name, last_name=last_name)

        db.session.add(user)
        db.session.commit()
    
        return redirect('/secret')
    else :
        return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def present_handle_login() :
    """Show a form that when submitted will login a user. 
    This form should accept a username and a password.
    Redirect to user-only content if successful."""
    # Make sure you are using WTForms and that your password input hides the characters that the user is typing!
    form = LoginForm()
    if form.validate_on_submit() :
        username = form.username.data
        attempt = form.password.data
        user = User.query.get(username)
        hashed = user.password

        if bcrypt.check_password_hash(hashed, attempt) :
            return redirect('/secret')
    else :
        return render_template('login.html')

@app.route('/secret', methods=['GET'])
def show_secret_page():
    """Return the text “You made it!” (don’t worry, we’ll get rid of this soon)"""
    return render_template('secret.html')