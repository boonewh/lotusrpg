from flask import Blueprint, render_template, url_for, flash, redirect, request, current_app as app
from flask_login import current_user, login_user
from flask_security import auth_required, verify_password
from lotusrpg import db
from lotusrpg.models import User
from lotusrpg.users.forms import UpdateAccountForm  # Updated import
from lotusrpg.users.utils import save_picture
import os

users = Blueprint('users', __name__)

@users.route('/account', methods=['GET', 'POST'])
@auth_required()
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            # Delete the old image if it's not the default image
            if current_user.image_file != 'default.png':
                old_picture_path = os.path.join(app.root_path, 'static/profile_pics', current_user.image_file)
                if os.path.exists(old_picture_path):
                    os.remove(old_picture_path)
            # Save the new picture
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', image_file=image_file, form=form)

@users.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')