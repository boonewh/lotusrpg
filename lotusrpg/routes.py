import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from lotusrpg import app, db, bcrypt
from lotusrpg.forms import RegistrationForm, LoginForm, UpdateAccountForm
from lotusrpg.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/forums')
def forums():
    return render_template('forums.html', posts=posts)

@app.route('/charity')
def charity():
    return render_template('charity.html')

@app.route('/sponsors')
def sponsors():
    return render_template('sponsors.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8) # Generating a random hex to prevent overwriting files with the same name
    _, f_ext = os.path.splitext(form_picture.filename) # Splitting the filename and extension
    picture_fn = random_hex + f_ext # Creating a new filename by combing the hex and the extension
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)  # Saving the picture to the filesystem

    output_size = (125, 125) # The next four lines resize the image and save it to the filesystem with Pillow package
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
             # Delete the old image if it's not the default image
            if current_user.image_file != 'default.jpg':
                old_picture_path = os.path.join(app.root_path, 'static/images', current_user.image_file)
                if os.path.exists(old_picture_path):
                    os.remove(old_picture_path)
            # Save the new picture
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.email = form.email.data
        db.session.commit()
        flash('Email updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.email.data = current_user.email
    image_file = url_for('static', filename='images/' + current_user.image_file)
    return render_template('account.html', image_file=image_file, form=form)