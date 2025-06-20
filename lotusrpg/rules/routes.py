from flask import Blueprint, jsonify, render_template, request
from lotusrpg.models import Section, Content

rules = Blueprint('rules', __name__)

@rules.route('/core/<slug>')
def core_rules(slug):
    """
    Render the rulebook page for a specific section.
    """
    section = Section.query.filter_by(slug=slug, rulebook='core').first_or_404()
    return render_template('core_rules.html', section=section)

@rules.route('/darkholme/<slug>')
def darkholme_rules(slug):
    section = Section.query.filter_by(slug=slug, rulebook='darkholme').first_or_404()
    return render_template('darkholme.html', section=section)


@rules.route('/api/chapters/<rulebook>', methods=['GET'])
def get_chapters(rulebook):
    chapters = Section.query.filter_by(rulebook=rulebook).with_entities(Section.chapter).distinct()
    chapter_data = []
    for chapter in chapters:
        sections = Section.query.filter_by(chapter=chapter.chapter, rulebook=rulebook).all()
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

@rules.route('/search')
def search_rules():
    """
    Search for rules in the core and darkholme rule sets.
    """
    query = request.args.get('q', '').strip()
    if not query:
        return render_template('search_results.html', results=[], query="")

    # Search for matching content in core_rules and darkholme
    matching_contents = Content.query.filter(Content.content_data.ilike(f"%{query}%")).all()

    results = []
    for content in matching_contents:
        section = Section.query.get(content.section_id)
        if section:
            results.append({
                "section_title": section.title,
                "slug": section.slug,
                "rulebook": section.rulebook,
                "content_data": str(content.content_data)[:200] + "..."
            })

    return render_template('search_results.html', results=results, query=query)