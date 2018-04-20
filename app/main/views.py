from flask import render_template,redirect, url_for
from . import main
from ..models import Blog
from .forms import BlogForm
from flask_wtf import FlaskForm
from .. import db




@main.route('/',methods = ['GET','POST'])
def index():

        
    form = BlogForm()
    
    if form.validate_on_submit():
         blog = form.blog.data
         new_Blog = Blog(blog.id,blog)
         new_Blog.save_Blog()
    return redirect(url_for('main.blog'))

    return render_template('index.html',blog_form=form)


@main.route('/blog',methods = ['GET','POST']) 
def blog():
    title = "post blog"
    blog = BlogForm()
    if blog.validate_on_submit():
        # blog = Blog(title = Blo.Entry.data,blog=Blog.Entry.data)
        db.session.add(blog)
        db.session.commit()
        print(blog)
        return redirect(url_for('main.blog'))
        all = Blog.query.all()
        allprint(all)

    return render_template('new_blog.html',blog_form=blog)
      