from flask_wtf import FlaskForm #2
from wtforms import StringField,PasswordField,SubmitField #2
from wtforms.validators import DataRequired,Email #2

class UserLoginForm(FlaskForm):
#email,password,Submit from wtforms
    
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()

#Twitter Mock Form
class TForm(FlaskForm):
    tweet = StringField('Tweet', validators=[DataRequired()]) #content
    submit_button = SubmitField() #submit
