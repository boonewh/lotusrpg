from flask import Blueprint, render_template, redirect, url_for, flash, request
from lotusrpg.models import Section, Content, Image, User, Role
from lotusrpg.admin.forms import SectionForm, ContentForm, ImageForm, NewRuleForm, ContainerForm
from flask_security import roles_required
from lotusrpg import db

admin = Blueprint('admin', __name__)

@admin.route('/dashboard')
@roles_required('admin')
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

@admin.route('/user/<int:user_id>/roles', methods=['GET', 'POST'])
@roles_required('admin')
def edit_roles(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        # Update user roles
        roles = request.form.getlist('roles')  # Get selected roles from form
        user.roles = Role.query.filter(Role.id.in_(roles)).all()
        db.session.commit()
        flash('Roles updated successfully!', 'success')
        return redirect(url_for('admin.manage_users'))
    all_roles = Role.query.all()
    return render_template('edit_roles.html', user=user, roles=all_roles)

# Edit Route
@admin.route('/edit/<slug>', methods=['GET', 'POST'])
@roles_required('admin')
def edit_rules(slug):
    section = Section.query.filter_by(slug=slug).first_or_404()
    contents = section.contents
    images = Image.query.filter_by(section_id=section.id).all()

    chapters = Section.query.with_entities(Section.chapter).distinct()
    chapter_data = []
    for chapter in chapters:
        sections = Section.query.filter_by(chapter=chapter.chapter).all()
        chapter_data.append({
            "title": chapter.chapter,
            "sections": [{"title": s.title, "slug": s.slug} for s in sections]
        })

    section_form = SectionForm(obj=section)

    if request.method == 'POST':
        action = request.form.get('action', '')

        if action == 'edit_title':
            new_title = request.form.get('title')
            section.title = new_title
            db.session.commit()
            flash("Title updated successfully!", "success")
            return redirect(url_for('admin.edit_rules', slug=slug))

        elif action == 'edit_section':
            section_form.populate_obj(section)
            db.session.commit()
            flash('Section updated successfully!', 'success')
            return redirect(url_for('admin.edit_rules', slug=slug))

        elif action == 'edit_content':
            content_id = request.form.get('content_id')
            content = Content.query.get(content_id)
            if content:
                content.content_type = request.form.get('content_type')
                content.content_data = request.form.get('content_data')
                content.content_order = request.form.get('content_order')
                content.style_class = request.form.get('style_class')
                db.session.commit()
                flash('Content updated successfully!', 'success')
            return redirect(url_for('admin.edit_rules', slug=slug))

        elif action == 'delete_content':
            content_id = request.form.get('content_id')
            content = Content.query.get(content_id)
            if content:
                db.session.delete(content)
                db.session.commit()
                flash('Content deleted successfully!', 'success')
            return redirect(url_for('admin.edit_rules', slug=slug))

        elif action == 'delete_section':
            db.session.delete(section)
            db.session.commit()
            flash('Section deleted successfully!', 'success')
            return redirect(url_for('admin.dashboard'))

    return render_template(
        'edit_rules.html',
        section=section,
        chapters=chapter_data,
        contents=contents,
        images=images,
        section_form=section_form
    )

@admin.route('/user/<int:user_id>/unlock', methods=['POST'])
@roles_required('admin')  # Ensure only admins can unlock
def unlock_user(user_id):
    user = User.query.get_or_404(user_id)
    try:
        user.failed_login_attempts = 0
        user.lockout_until = None
        db.session.commit()
        flash(f'Successfully unlocked {user.username}\'s account.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error unlocking account: {str(e)}', 'danger')
    
    return redirect(url_for('admin.manage_users'))

@admin.route('/user/<int:user_id>/delete', methods=['POST'])
@roles_required('admin')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    if 'admin' in [role.name for role in user.roles]:
        flash('Cannot delete an admin user, change their role first.', 'danger')
        return redirect(url_for('admin.manage_users'))
    
    db.session.delete(user)
    db.session.commit()
    flash(f'{user.username} deleted successfully!', 'success')
    return redirect(url_for('admin.manage_users'))