"""Blogly application."""

from flask import Flask, render_template, request, redirect, flash
from models import db, connect_db, User, Post

app = Flask(__name__)
connect_db(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "Dontyadaughtadothatbaby"

@app.route('/', methods=['GET'])
def show_homepage() :
    """Redirect to list of users. (We’ll fix this in a later step)"""
    return redirect('/users')

@app.route('/users', methods=['GET'])
def show_users() :
    """Show all users"""
    users = list(User.query.all())
    return render_template('users.html', users=users)

@app.route('/users/<user_id>', methods=['GET'])
def show_user_and_posts(user_id) :
    """view the detail page for the user, as well as show all of their posts"""
    user = User.query.get(int(user_id))
    posts = Post.query.filter(Post.user_id == user_id)
    return render_template('user-detail.html', user=user, posts=posts)

@app.route('/users/new', methods=['GET'])
def show_new_user_form() :
    """Show an add form for users"""
    return render_template("user-form.html")

@app.route('/users/new', methods=['POST'])
def submit_new_user_form() :
    """Process the add form, 
    adding a new user and going back to /users"""
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    if not '.png' in image_url and not '.jpeg' in image_url and not '.jpg' in image_url and not '.gif' in image_url : 
        image_url = 'http://127.0.0.1:5000/static/default-profile-pic.png'
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()
    flash('new user added')
    return redirect('/users')

# Have a button to get to their edit page, and to delete the user.
@app.route('/users/<user_id>/edit', methods=['GET'])
def show_edit_page(user_id) :
    """Show the edit page for a user"""
    user = User.query.get(user_id)
    return render_template('user-edits.html', user=user)

    # Have a cancel button that returns to the detail page for a user, 

    # and a save button that updates the user.

@app.route('/users/<user_id>/edit', methods=['POST'])
def submit_user_edits(user_id) :
    """Process the edit form, returning the user to the /users page"""
    user = User.query.get(int(user_id))
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']
    if not '.png' in request.form['image_url'] and not '.jpeg' in request.form['image_url'] and not '.jpg' in request.form['image_url'] and not '.gif' in request.form['image_url'] : 
        user.image_url = 'http://127.0.0.1:5000/static/default-profile-pic.png'
        flash('profile image url not compatible')
    db.session.add(user)
    db.session.commit()
    return redirect(f"/users/{user_id}")

@app.route('/users/<user_id>/delete', methods=['POST'])
def delete_user(user_id) : 
    """Delete the user"""
    user = User.query.get(int(user_id))
    db.session.delete(user)
    db.session.commit()
    flash("user deleted")
    return redirect(f"/users")

@app.route('/users/<user_id>/post<post_id>')
def show_post_detail(user_id, post_id) :
    """show a user's specified post"""
    user = User.query.get(int(user_id))
    post = Post.query.get(int(post_id))
    return render_template("post.html", user=user, post=post)

@app.route('/users/<user_id>/post<post_id>/delete', methods=['POST'])
def delete_post(user_id, post_id) : 
    """Delete the user's post"""
    user = User.query.get(int(user_id))
    post = Post.query.get(int(post_id))
    db.session.delete(post)
    db.session.commit()
    flash("post deleted")
    return redirect(f"/users/{user.id}")

@app.route('/users/<user_id>/post<post_id>/edit', methods=['GET'])
def show_edit_post(user_id, post_id) :
    """Shows user page where edits to their post can be made"""
    user = User.query.get(user_id)
    post = Post.query.get(post_id)
    return render_template('post-edits.html', user=user, post=post)

@app.route('/users/<user_id>/post<post_id>/edit', methods=['POST'])
def submit_post_edit(user_id, post_id) :
    """Submits the changes made to the post by the user"""
    user = User.query.get(user_id)
    post = Post.query.get(post_id)
    post.title = request.form['title']
    post.content = request.form['content']
    db.session.add(post)
    db.session.commit()
    return redirect(f"/users/{user.id}/post{post.id}")

@app.route('/users/<user_id>/newpost', methods=['GET'])
def show_post_form(user_id) :
    user = User.query.get (user_id)
    return render_template("post-form.html", user=user)

@app.route('/users/<user_id>/newpost', methods=['POST'])
def submit_post(user_id) :
    user = User.query.get(user_id)
    title = request.form['title']
    content = request.form['content']
    post = Post(title=title, content=content, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    newpost = Post.query.filter(Post.user_id==user_id, Post.title==title).first()
    return redirect(f"/users/{user.id}/post{newpost.id}")