from flask import render_template
from . import main
from ..models import Blog
from .forms import BlogForm



@main.route('/',methods = ['GET','POST'])
def index():

        
    form = BlogForm()
    # blog = form.blog.data
    if form.validate_on_submit():
        new_blog = Blog(blog.id,blog)
        new_blog.save_blog()
        return redirect(url_for('blog',id = blog.id ))

    return render_template('index.html',blog_form=form)

    # return render_template('new_blog.html',title = title, blog_form = form)
