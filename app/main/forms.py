from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):

    p_body = StringField(' title',validators=[Required()])
    review = TextAreaField('blog', validators=[Required()])
    submit = SubmitField('Submit')




class CommentForm(FlaskForm):

    
    review = TextAreaField('nobody gives a fuck about your opinion tbh but anyway..', validators=[Required()])
    submit = SubmitField('Submit')