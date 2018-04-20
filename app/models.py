from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(60))
    password = db.Column(db.String(60))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    # password_hash = db.Column(db.String(255))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    

@property
def password(self):
            raise AttributeError('You cannot read the password attribute')

@password.setter
def password(self, password):
            self.pass_secure = generate_password_hash(password)


def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

class Blog:

    all_blogs = []

def __init__(self,id,blog):
        self.id = id
        self.blog = blog


def save_blog(self):
        Blog.all_blogs.append(self)


@classmethod
def clear_blogs(cls):
        Blog.all_blogs.clear()

@classmethod
def get_blogs(cls,id):
    response = []
    for blog in cls.all_blogs:
        if blog.id == id:
            response.append(blog)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
 
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))



def __repr__(self):
    return f'User {self.username}'


