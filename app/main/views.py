from flask import render_template,redirect, url_for
from . import main
from ..models import Post
from .forms import BlogForm
from flask_wtf import FlaskForm
from .. import db
from flask_login import current_user




@main.route('/',methods = ['GET','POST'])
def index():

    return render_template('index.html')


@main.route('/blog', methods=['GET', 'POST'])
def blog():
    
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        
        new_post = Post(body = blog_form.review.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.blog'))
    return render_template('new_blog.html',blog_form=blog_form)





