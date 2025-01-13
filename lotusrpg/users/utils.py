import os
import secrets
from PIL import Image
from flask import url_for, current_app as app
from flask_mail import Message  
from lotusrpg import mail  


def save_picture(form_picture):
    random_hex = secrets.token_hex(8) # Generating a random hex to prevent overwriting files with the same name
    _, f_ext = os.path.splitext(form_picture.filename) # Splitting the filename and extension
    picture_fn = random_hex + f_ext # Creating a new filename by combing the hex and the extension
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)  # Saving the picture to the filesystem

    output_size = (125, 125) # The next four lines resize the image and save it to the filesystem with Pillow package
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()  # Assumes your User model has a method to generate a reset token
    msg = Message(
        'Password Reset Request',
        sender='boonewh@gmail.com', 
        recipients=[user.email]
    )
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request, simply ignore this email and no changes will be made.
'''
    mail.send(msg)