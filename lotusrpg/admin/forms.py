from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class SectionForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])
    submit = SubmitField('Save Section')

class ContentForm(FlaskForm):
    content_type = SelectField('Content Type', choices=[
        ('heading', 'Heading'),
        ('subheading', 'Subheading'),
        ('paragraph', 'Paragraph'),
        ('table', 'Table'),
        ('list', 'List'),
        ('image', 'Image')
    ], validators=[DataRequired()])
    content_order = IntegerField('Content Order', validators=[DataRequired()])
    content_data = TextAreaField('Content Data', validators=[DataRequired()])
    style_class = StringField('Style Class')
    submit = SubmitField('Save Content')
