from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):

    # p_body = StringField(' title',validators=[Required()])
    review = TextAreaField('blog', validators=[Required()])
    submit = SubmitField('Submit')