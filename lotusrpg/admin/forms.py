from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Optional

class SectionForm(FlaskForm):
    """Form for creating or editing a section."""
    title = StringField('Section Title', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])
    submit = SubmitField('Save Section')

class ContentForm(FlaskForm):
    """Form for creating or editing content."""
    content_type = SelectField(
        'Content Type',
        choices=[
            ('heading', 'Heading'),
            ('paragraph', 'Paragraph'),
            ('list', 'List'),
            ('table', 'Table'),
            ('image', 'Image')
        ],
        validators=[DataRequired()]
    )
    content_order = IntegerField('Content Order', validators=[DataRequired()])
    content_data = TextAreaField('Content Data', validators=[DataRequired()])
    style_class = StringField('CSS Class', validators=[Optional()])
    submit = SubmitField('Save Content')

class ImageForm(FlaskForm):
    """Form for adding or editing an image."""
    file_path = StringField('File Path', validators=[DataRequired()])
    alt_text = StringField('Alt Text', validators=[Optional()])
    class_name = StringField('CSS Class', validators=[Optional()])
    submit = SubmitField('Save Image')
