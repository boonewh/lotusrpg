from flask import Blueprint, render_template
from lotusrpg.models import Section

rules = Blueprint('rules', __name__)

@rules.route('/core/<slug>')
def core_rules(slug):
    """
    Route to display a rulebook section based on the slug.
    """
    # Fetch the section from the database
    section = Section.query.filter_by(slug=slug).first_or_404()

    # Render the section.html template, passing the section data
    return render_template('core_rules.html', section=section)