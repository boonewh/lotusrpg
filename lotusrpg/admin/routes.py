from flask import Blueprint, render_template, redirect, url_for, flash, request
from lotusrpg.models import db, Section, Content, User, Role
from lotusrpg.admin.forms import RuleForm
from flask_security import roles_required

admin = Blueprint('admin', __name__)

@admin.route('/dashboard')
def dashboard():
    sections = Section.query.all()
    return render_template('dashboard.html', sections=sections)

@admin.route('/add', methods=['GET', 'POST'])
def add_rule():
    form = RuleForm()
    if form.validate_on_submit():
        # Create a new Section
        section = Section(title=form.title.data, slug=form.slug.data)
        db.session.add(section)
        db.session.commit()

        # Create Content associated with the Section
        content = Content(
            section_id=section.id,
            content_type=form.content_type.data,
            content_order=form.content_order.data,
            content_data=form.content.data,
            style_class=form.style_class.data
        )
        db.session.add(content)
        db.session.commit()

        flash('Rule added successfully!', 'success')
        return redirect(url_for('admin.dashboard'))
    return render_template('add_rule.html', form=form)

@admin.route('/edit/<int:section_id>', methods=['GET', 'POST'])
def edit_rule(section_id):
    section = Section.query.get_or_404(section_id)
    content = Content.query.filter_by(section_id=section.id).first()
    form = RuleForm(
        title=section.title,
        slug=section.slug,
        content_type=content.content_type if content else None,
        content_order=content.content_order if content else None,
        content=content.content_data if content else None,
        style_class=content.style_class if content else None,
    )

    if form.validate_on_submit():
        # Update Section
        section.title = form.title.data
        section.slug = form.slug.data

        # Update Content
        if content:
            content.content_type = form.content_type.data
            content.content_order = form.content_order.data
            content.content_data = form.content.data
            content.style_class = form.style_class.data
        else:
            # If no content exists, create it
            new_content = Content(
                section_id=section.id,
                content_type=form.content_type.data,
                content_order=form.content_order.data,
                content_data=form.content.data,
                style_class=form.style_class.data
            )
            db.session.add(new_content)

        db.session.commit()
        flash('Rule updated successfully!', 'success')
        return redirect(url_for('admin.dashboard'))

    return render_template('edit_rule.html', form=form)

@admin.route('/delete/<int:section_id>', methods=['POST'])
def delete_rule(section_id):
    section = Section.query.get_or_404(section_id)
    content = Content.query.filter_by(section_id=section.id).all()

    # Delete associated content
    for item in content:
        db.session.delete(item)

    db.session.delete(section)
    db.session.commit()
    flash('Rule deleted successfully!', 'success')
    return redirect(url_for('admin.dashboard'))


@admin.route('/users')
@roles_required('admin')
def manage_users():
    search_query = request.args.get('search', '').strip()
    page = request.args.get('page', 1, type=int)
    
    if search_query:
        # Filter users by username or email (case insensitive)
        users = User.query.filter(
            User.username.ilike(f'%{search_query}%') | 
            User.email.ilike(f'%{search_query}%')
        ).paginate(page=page, per_page=10)
    else:
        # No search query, show all users
        users = User.query.paginate(page=page, per_page=10)
    
    return render_template('manage_users.html', users=users)


@admin.route('/user/<int:user_id>/ban', methods=['POST'])
@roles_required('admin')
def ban_user(user_id):
    user = User.query.get_or_404(user_id)
    user.is_banned = not user.is_banned  # Toggle ban status
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