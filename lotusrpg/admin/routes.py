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
def manage_page(slug):
    section = Section.query.filter_by(slug=slug).first_or_404()
    contents = section.contents  # Get contents related to the section
    images = Image.query.all()   # Example: Update to filter images by section if needed

    import re

    # Sanitize content_data thoroughly
    for content in contents:
        content.content_data = re.sub(r'[\r\n]+', ' ', content.content_data.strip())


    # Initialize forms
    section_form = SectionForm(obj=section)
    content_form = ContentForm()
    image_form = ImageForm()

    if request.method == 'POST':
        # Handle editing the section
        if section_form.validate_on_submit():
            section.title = section_form.title.data
            section.slug = section_form.slug.data
            db.session.commit()
            flash('Section updated successfully!', 'success')
            return redirect(url_for('admin.manage_page', slug=slug))

        # Handle adding or editing content
        if 'content_data' in request.form:
            content_id = request.form.get('content_id')
            if content_id:  # Update existing content
                content = Content.query.get_or_404(content_id)
                content.content_data = request.form['content_data']
                content.content_order = request.form.get('content_order', content.content_order)
                content.style_class = request.form.get('style_class', content.style_class)
            else:  # Add new content
                content = Content(
                    section_id=section.id,
                    content_data=request.form['content_data'],
                    content_order=request.form.get('content_order', 0),
                    style_class=request.form.get('style_class', None),
                )
                db.session.add(content)
            db.session.commit()
            flash('Content updated successfully!', 'success')
            return redirect(url_for('admin.manage_page', slug=slug))

        # Handle deleting content
        if 'delete_content_id' in request.form:
            content_id = request.form['delete_content_id']
            content = Content.query.get(content_id)
            if content:
                db.session.delete(content)
                db.session.commit()
                flash('Content deleted successfully!', 'success')
            return redirect(url_for('admin.manage_page', slug=slug))

        # Handle adding/editing images
        if 'file_path' in request.form:
            image_id = request.form.get('image_id')
            image = Image.query.get(image_id) if image_id else Image()
            image.file_path = request.form['file_path']
            image.alt_text = request.form['alt_text']
            image.class_name = request.form['class_name']
            db.session.add(image)
            db.session.commit()
            flash('Image updated successfully!', 'success')
            return redirect(url_for('admin.manage_page', slug=slug))

        # Handle deleting images
        if 'delete_image_id' in request.form:
            image_id = request.form['delete_image_id']
            image = Image.query.get(image_id)
            if image:
                db.session.delete(image)
                db.session.commit()
                flash('Image deleted successfully!', 'success')
            return redirect(url_for('admin.manage_page', slug=slug))

    return render_template(
        'manage_page.html',
        section=section,
        contents=contents,
        images=images,
        section_form=section_form,
        content_form=content_form,
        image_form=image_form
    )
