from flask import Blueprint, jsonify, render_template
from lotusrpg.models import Section

rules = Blueprint('rules', __name__)

@rules.route('/core/<slug>')
def core_rules(slug):
    """
    Render the rulebook page for a specific section.
    """
    section = Section.query.filter_by(slug=slug).first_or_404()
    return render_template('core_rules.html', section=section)

@rules.route('/api/chapters', methods=['GET'])
def get_chapters():
    """
    API route to return chapters and their sections dynamically.
    """
    chapters = Section.query.with_entities(Section.chapter).distinct()
    chapter_data = []
    for chapter in chapters:
        sections = Section.query.filter_by(chapter=chapter.chapter).all()
        chapter_data.append({
            "title": chapter.chapter,
            "sections": [{"title": s.title, "slug": s.slug} for s in sections]
        })
    return jsonify(chapters=chapter_data)

@rules.route('/api/section/<slug>', methods=['GET'])
def get_section(slug):
    """
    API route to return content for a specific section dynamically.
    """
    section = Section.query.filter_by(slug=slug).first_or_404()
    contents = [{"type": c.content_type, "data": c.content_data, "order": c.content_order, "style_class": c.style_class} for c in section.contents]
    return jsonify(title=section.title, contents=contents)
