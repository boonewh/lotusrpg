from flask import Blueprint, jsonify, render_template, request
from lotusrpg.models import Section, Content
from lotusrpg import db

rules = Blueprint('rules', __name__)

@rules.route('/core/<slug>')
def core_rules(slug):
    """
    Render the rulebook page for a specific section (Core).
    """
    section = Section.query.filter_by(slug=slug, rulebook='core').first_or_404()
    contents = Content.query.filter_by(section_id=section.id).order_by(Content.content_order).all()
    return render_template('core_rules.html', section=section, contents=contents)

@rules.route('/darkholme/<slug>')
def darkholme_rules(slug):
    """
    Render the rulebook page for a specific section (Darkholme).
    """
    section = Section.query.filter_by(slug=slug, rulebook='darkholme').first_or_404()
    contents = Content.query.filter_by(section_id=section.id).order_by(Content.content_order).all()
    return render_template('darkholme.html', section=section, contents=contents)

@rules.route('/api/chapters/<rulebook>', methods=['GET'])
def get_chapters(rulebook):
    """
    Return chapters and their sections, with sections ordered by section_order.
    """
    chapters = Section.query.filter_by(rulebook=rulebook).with_entities(Section.chapter).distinct().all()
    chapter_data = []
    for chapter in chapters:
        sections = (
            Section.query
            .filter_by(chapter=chapter.chapter, rulebook=rulebook)
            .order_by(Section.section_order)
            .all()
        )
        chapter_data.append({
            "title": chapter.chapter,
            "sections": [{"title": s.title, "slug": s.slug} for s in sections]
        })
    return jsonify(chapters=chapter_data)

@rules.route('/api/section/<slug>', methods=['GET'])
def get_section(slug):
    """
    API: Return section details and all content blocks in order.
    """
    section = Section.query.filter_by(slug=slug).first_or_404()
    contents = Content.query.filter_by(section_id=section.id).order_by(Content.content_order).all()
    contents_json = [
        {
            "type": c.content_type,
            "data": c.content_data,
            "order": c.content_order,
            "style_class": c.style_class
        }
        for c in contents
    ]
    return jsonify(title=section.title, contents=contents_json)

@rules.route('/search')
def search_rules():
    """
    Search for rules in both rulebooks by content text.
    Results are ordered by content_order within section.
    """
    query = request.args.get('q', '').strip()
    if not query:
        return render_template('search_results.html', results=[], query="")

    matching_contents = Content.query.filter(Content.content_data.ilike(f"%{query}%")).order_by(Content.content_order).all()
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

@rules.route('/api/section/<slug>', methods=['PUT'])
def update_section(slug):
    """
    API: Replace all content blocks for a section.
    """
    payload = request.get_json()
    contents = payload.get("contents", [])

    section = Section.query.filter_by(slug=slug).first_or_404()
    Content.query.filter_by(section_id=section.id).delete()

    # Validate all content blocks first
    for i, item in enumerate(contents):
        if not isinstance(item, dict) or 'type' not in item or 'data' not in item or 'order' not in item:
            return jsonify({
                "success": False,
                "message": f"Content block at index {i} is missing required fields"
            }), 400

    # Add new content blocks, ordered
    for item in contents:
        new_content = Content(
            section_id=section.id,
            content_type=item['type'],
            content_order=item['order'],
            content_data=item['data'],
            style_class=item.get('style_class', '')
        )
        db.session.add(new_content)

    db.session.commit()
    return jsonify({"success": True, "message": "Section updated successfully"})

@rules.route('/api/section', methods=['POST'])
def create_section():
    """
    API: Create a new section with initial content blocks.
    """
    data = request.get_json()
    required_fields = ['title', 'slug', 'chapter', 'rulebook', 'contents']
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"success": False, "message": f"Missing fields: {', '.join(missing)}"}), 400

    section = Section(
        title=data['title'],
        slug=data['slug'],
        chapter=data['chapter'],
        rulebook=data['rulebook'],
        section_order=data.get('section_order')  # Add if provided!
    )
    db.session.add(section)
    db.session.commit()

    # Validate and add content blocks
    for i, item in enumerate(data['contents']):
        if not isinstance(item, dict) or 'type' not in item or 'data' not in item:
            return jsonify({
                "success": False,
                "message": f"Invalid content block at index {i}"
            }), 400

        content = Content(
            section_id=section.id,
            content_type=item['type'],
            content_order=item.get('order', i),
            content_data=item['data'],
            style_class=item.get('style_class', '')
        )
        db.session.add(content)

    db.session.commit()
    return jsonify({
        "success": True,
        "message": "Section created successfully",
        "slug": section.slug
    }), 201
