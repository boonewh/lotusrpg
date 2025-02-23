from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import current_user
from lotusrpg.models import Post, Comment, User
from lotusrpg import db
from lotusrpg.forum.forms import PostForm, CommentForm 
from flask_security import auth_required, roles_required



forum = Blueprint('forum', __name__)

@forum.route('/forums')
@auth_required()
def forums():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('forums.html', posts=posts)

@forum.route('/post/new', methods=['GET', 'POST'])
@auth_required()
@roles_required('admin')
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('forum.forums'))
    return render_template('create_post.html', form=form, legend='Create Post')

@forum.route('/post/<int:post_id>', methods=['GET', 'POST'])
@auth_required()
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment(content=form.content.data, user_id=current_user.id, post_id=post.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('forum.post', post_id=post.id))
    
    page = request.args.get('page', 1, type=int)
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.date_posted).paginate(page=page, per_page=5)

    return render_template('post.html', post=post, comments=comments.items, form=form, pagination=comments)



@forum.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@auth_required()
@roles_required('admin')
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        return redirect(url_for('forum.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', form=form, legend='Update Post')

@forum.route('/post/<int:post_id>/delete', methods=['POST'])
@auth_required()
@roles_required('admin')
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('forums'))

@forum.route('/comment/<int:comment_id>/delete', methods=['POST'])
@auth_required()
@roles_required('admin')
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('forum.post', post_id=comment.post_id))

@forum.route('/comment/<int:comment_id>/edit', methods=['GET', 'POST'])
@auth_required()
@roles_required('admin')
def edit_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.user_id != current_user.id:
        abort(403)
    form = CommentForm()
    if form.validate_on_submit():
        comment.content = form.content.data
        db.session.commit()
        flash('Your comment has been updated!', 'success')
        return redirect(url_for('forum.post', post_id=comment.post_id))
    elif request.method == 'GET':
        form.content.data = comment.content
    return render_template('edit_comment.html', form=form, comment=comment)

@forum.route("/user/<string:username>")
@auth_required()
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('user_posts.html', posts=posts, user=user)