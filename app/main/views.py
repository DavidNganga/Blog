from flask import render_template,redirect, url_for
from . import main
from ..models import Post,Comment
from .forms import BlogForm,CommentForm
from flask_wtf import FlaskForm
from .. import db
from flask_login import current_user




@main.route('/',methods = ['GET','POST'])
def index():
    Blogs = Post.query.all()
    Blogs.reverse()

    return render_template('index.html',Blogs = Blogs)


@main.route('/blog', methods=['GET', 'POST'])
def blog():
    
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        
        new_post = Post(title = blog_form.p_body.data,body = blog_form.review.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.blog'))
    return render_template('new_blog.html',blog_form=blog_form)



# @main.route('/comment', methods=['GET', 'POST'])
# def comment():



    
@main.route('/post/<id>', methods=['GET', 'POST'])
def post(id):
    posts = Post.query.filter_by(id=id)
    comments = Comment.query.filter_by(id=id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        
        new_comment = Comment(body = comment_form.review.data)
        db.session.add(new_comment)
        db.session.commit()
       
        return redirect(url_for('main.post',id=id))
    allcomments = Comment.query.all()
    print(allcomments)
       
     

    return render_template('posts.html',posts=posts,comment_form=comment_form,comments=comments,allcomments=allcomments)
    









    








