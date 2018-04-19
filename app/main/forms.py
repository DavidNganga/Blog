from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class BlogForm(FlaskForm):

    title = TextAreaField('Post blog',validators=[Required()])
   
    submit = SubmitField('Submit')