from flask import Blueprint, render_template, redirect, url_for, flash, request
from lotusrpg.models import db, Section, Content
from lotusrpg.admin.forms import RuleForm

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
