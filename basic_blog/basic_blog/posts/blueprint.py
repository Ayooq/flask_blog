from flask import (
    Blueprint, render_template, request, redirect, url_for
)
from flask_security import login_required

from app import db
from models import Post, Tag
from posts.forms import PostForm


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Something wrong!')

        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/tag/<slug>')
def tag_reveal(slug):
    tag = Tag.query.filter(Tag.slug == slug).first_or_404()
    posts = tag.posts
    return render_template('posts/tag_reveal.html', posts=posts, tag=tag)


def search_query(q):
    posts = Post.query.filter(
        Post.title.ilike(f'%{q}%') |
        Post.body.ilike(f'%{q}%')
    )
    return posts


@posts.route('/')
@posts.route('/pages/<int:page>')
def index(page=1):
    q = request.args.get('q')
    posts = search_query(q) if q else Post.query.order_by(Post.created.desc())

    pages = posts.paginate(page=page, per_page=5)

    return render_template('posts/index.html', pages=pages)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)
