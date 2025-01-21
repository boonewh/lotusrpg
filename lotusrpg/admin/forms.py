from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class RuleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])
    content_type = SelectField('Content Type', choices=[
        ('heading', 'Heading'),
        ('subheading', 'Subheading'),
        ('paragraph', 'Paragraph'),
        ('table', 'Table'),
        ('list', 'List'),
        ('image', 'Image')
    ])
    content_order = IntegerField('Content Order')
    content = TextAreaField('Content', validators=[DataRequired()])
    style_class = StringField('Style Class')
    submit = SubmitField('Save')

