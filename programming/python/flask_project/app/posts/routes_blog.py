from flask import Blueprint, redirect, url_for
from flask import render_template
from models import Post, Tag, User, Comment
from flask import request
from .forms import PostFrom, CommentForm
from app import db, ckeditor
from flask_login import login_required, current_user
from app import captcha


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    q = request.args.get('q')
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    if q:
        post = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)) #.all()
    else:
        post = Post.query.order_by(Post.create.desc())
    pages = post.paginate(page=page, per_page=11)
    return render_template('posts/index.html', pages=pages)


@posts.route('/create', methods=['POST', 'GET'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        tags = str(request.form['tags'])
        data_tags = tags.split(',')
        user = User.query.filter_by(id=int(current_user.get_id())).first()
        try:
            post = Post(title=title, body=body, author=user)
            if len(data_tags) > 1:
                for tag in data_tags:
                    tag = Tag(name=tag)
                    post.tags.append(tag)
            else:
                tag = Tag(name=tags)
                post.tags.append(tag)
            db.session.add(post)
            db.session.commit()
        except:
            print('Данные не сохранились...')

        return redirect(url_for('posts.index'))
    form = PostFrom()
    return render_template('/posts/create_post.html', form=form)


@posts.route('/<slug>/edit', methods=['POST', 'GET'])
@login_required
def edit_post(slug):
    find_post = Post.query.filter(Post.slug == slug).first()
    if request.method == 'POST':
        form = PostFrom(formdata=request.form, obj=find_post)
        form.populate_obj(find_post)
        db.session.commit()
        return redirect(url_for('posts.post_detail', slug=find_post.slug))
    form = PostFrom(obj=find_post)
    return render_template('posts/edit.html', find_post=find_post, form=form)


@posts.route('/<slug>', methods=['POST', 'GET'])
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    tags = post.tags
    comments = post.comments
    comments.reverse()
    if request.method == 'POST':
        if captcha.validate():
            username = request.form['username']
            body = request.form['body']
            try:
                comment = Comment(username=username, body=body)
                post.comments.append(comment)
                db.session.add(post)
                db.session.commit()
            except:
                print('Комментарий не записался...')
        else:
            return redirect(url_for('posts.post_detail', slug=slug))
        return redirect(url_for('posts.post_detail', slug=slug))
    warning = 'Неправильные цифры в капче'
    form = CommentForm()
    return render_template('/posts/post_detail.html', post=post, tags=tags, comments=comments, form=form, warning=warning)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    post = tag.posts.all()
    return render_template('/posts/tag_detail.html', tag=tag, post=post)