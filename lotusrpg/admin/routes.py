from flask import Blueprint, render_template, redirect, url_for, flash, request
from lotusrpg.models import db, Section, Content, Image, User, Role
from lotusrpg.admin.forms import SectionForm, ContentForm, ImageForm
from flask_security import roles_required

admin = Blueprint('admin', __name__)

@admin.route('/dashboard')
def dashboard():
    sections = Section.query.all()
    return render_template('dashboard.html', sections=sections)

# Administer Users and Roles Routes

@admin.route('/users')
@roles_required('admin')
def manage_users():
    search_query = request.args.get('search', '').strip()
    page = request.args.get('page', 1, type=int)
    
    if search_query:
        users = User.query.filter(
            User.username.ilike(f'%{search_query}%') | 
            User.email.ilike(f'%{search_query}%')
        ).paginate(page=page, per_page=10)
    else:
        users = User.query.paginate(page=page, per_page=10)
    
    return render_template('manage_users.html', users=users)

@admin.route('/user/<int:user_id>/ban', methods=['POST'])
@roles_required('admin')
def ban_user(user_id):
    user = User.query.get_or_404(user_id)
    user.is_banned = not user.is_banned
    db.session.commit()
    flash(f"User {'banned' if user.is_banned else 'unbanned'} successfully!", 'success')
    return redirect(url_for('admin.manage_users'))

@admin.route('/manage/<slug>', methods=['GET', 'POST'])
@roles_required('admin')
def manage_page(slug):
    # Fetch the current section and related data
    section = Section.query.filter_by(slug=slug).first_or_404()
    contents = section.contents
    images = Image.query.filter_by(section_id=section.id).all()

    # Query all chapters and their sections dynamically
    chapters = Section.query.with_entities(Section.chapter).distinct()
    chapter_data = []
    for chapter in chapters:
        sections = Section.query.filter_by(chapter=chapter.chapter).all()
        chapter_data.append({
            "title": chapter.chapter,
            "sections": [{"title": s.title, "slug": s.slug} for s in sections]
        })

    # Initialize forms
    section_form = SectionForm(obj=section)
    content_form = ContentForm()
    image_form = ImageForm()

    # Handle POST requests
    if request.method == 'POST':
        action = request.form.get('action', '')

        # Handle section edits
        if action == 'edit_section' and section_form.validate_on_submit():
            section.title = section_form.title.data
            section.slug = section_form.slug.data
            db.session.commit()
            flash('Section updated successfully!', 'success')
            return redirect(url_for('admin.manage_page', slug=slug))

        # Handle adding/editing content
        elif action == 'add_content':
            content_id = request.form.get('content_id')
            if content_id:  # Update existing content
                content = Content.query.get_or_404(content_id)
                content.content_data = request.form['content_data']
                content.content_order = request.form.get('content_order', content.content_order)
                content.style_class = request.form.get('style_class', content.style_class)
                flash('Content updated successfully!', 'success')
            else:  # Add new content
                new_content = Content(
                    section_id=section.id,
                    content_data=request.form['content_data'],
                    content_order=request.form.get('content_order', 0),
                    style_class=request.form.get('style_class')
                )
                db.session.add(new_content)
                flash('Content added successfully!', 'success')
            db.session.commit()
            return redirect(url_for('admin.manage_page', slug=slug))

        # Handle deleting content
        elif action == 'delete_content':
            content_id = request.form.get('delete_content_id')
            content = Content.query.get(content_id)
            if content:
                db.session.delete(content)
                db.session.commit()
                flash('Content deleted successfully!', 'success')
            return redirect(url_for('admin.manage_page', slug=slug))

        # Handle adding/editing images
        elif action == 'add_image':
            image_id = request.form.get('image_id')
            if image_id:  # Update existing image
                image = Image.query.get_or_404(image_id)
                image.file_path = request.form['file_path']
                image.alt_text = request.form['alt_text']
                image.class_name = request.form['class_name']
                flash('Image updated successfully!', 'success')
            else:  # Add new image
                new_image = Image(
                    section_id=section.id,
                    file_path=request.form['file_path'],
                    alt_text=request.form['alt_text'],
                    class_name=request.form['class_name']
                )
                db.session.add(new_image)
                flash('Image added successfully!', 'success')
            db.session.commit()
            return redirect(url_for('admin.manage_page', slug=slug))

        # Handle deleting images
        elif action == 'delete_image':
            image_id = request.form.get('delete_image_id')
            image = Image.query.get(image_id)
            if image:
                db.session.delete(image)
                db.session.commit()
                flash('Image deleted successfully!', 'success')
            return redirect(url_for('admin.manage_page', slug=slug))

    # Render the page
    return render_template(
        'manage_page.html',
        section=section,
        chapters=chapter_data,  # Properly structured data
        contents=contents,
        images=images,
        section_form=section_form,
        content_form=content_form,
        image_form=image_form
    )

