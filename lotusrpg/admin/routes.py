from flask import Blueprint, render_template, redirect, url_for, flash, request
from lotusrpg.admin.forms import RuleForm
from lotusrpg.models import Rule
from lotusrpg import db

admin = Blueprint('admin', __name__)

@admin.route('/dashboard')
def dashboard():
    rules = Rule.query.all()
    return render_template('admin/dashboard.html', rules=rules)

@admin.route('/add', methods=['GET', 'POST'])
def add_rule():
    form = RuleForm()
    if form.validate_on_submit():
        rule = Rule(title=form.title.data, content=form.content.data)
        db.session.add(rule)
        db.session.commit()
        flash('Rule added successfully!', 'success')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/add_rule.html', form=form)

@admin.route('/edit/<int:rule_id>', methods=['GET', 'POST'])
def edit_rule(rule_id):
    rule = Rule.query.get_or_404(rule_id)
    form = RuleForm(obj=rule)
    if form.validate_on_submit():
        rule.title = form.title.data
        rule.content = form.content.data
        db.session.commit()
        flash('Rule updated successfully!', 'success')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/edit_rule.html', form=form)

@admin.route('/delete/<int:rule_id>', methods=['POST'])
def delete_rule(rule_id):
    rule = Rule.query.get_or_404(rule_id)
    db.session.delete(rule)
    db.session.commit()
    flash('Rule deleted successfully!', 'success')
    return redirect(url_for('admin.dashboard'))