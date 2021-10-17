from flask_wtf import FlaskForm #2
from wtforms import StringField,PasswordField,SubmitField #2
from wtforms.validators import DataRequired,Email #2
from flask_login import UserMixin

class UserLoginForm(FlaskForm,UserMixin):
#email,password,Submit from wtforms
    
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()

#Twitter Mock Form
class TForm(FlaskForm):
    tweet = StringField(validators=[DataRequired()]) #content
    submit_button = SubmitField() #submit
