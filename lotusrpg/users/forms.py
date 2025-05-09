from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flask_login import current_user
from flask_security.forms import RegisterForm
from lotusrpg.models import User

class ExtendedRegisterForm(RegisterForm):
    username = StringField('Username',
                         validators=[DataRequired(), Length(min=2, max=20)])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class UpdateAccountForm(FlaskForm):
    email = StringField('Email',
                       validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', 
                       validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')