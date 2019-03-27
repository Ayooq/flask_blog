from flask import render_template

from admin import app
from posts.blueprint import posts


@app.route('/')
def index():
    name = 'Влад'
    return render_template('index.html', n=name)


app.register_blueprint(posts, url_prefix='/blog')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
