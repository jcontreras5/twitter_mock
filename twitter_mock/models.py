from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
import uuid 

#Adding FLASK security from werkzeug :sha256 encryption
from werkzeug.security import generate_password_hash,check_password_hash  #3

#3 import secret module(inc python) for unique hex value for token
import secrets

#3 import for flask login class
from flask_login import UserMixin,LoginManager #3

db = SQLAlchemy() #3 init db class instance
login_manager = LoginManager() #inst LM class as var

# @login_manager.user_loader #gets id 
# def load_user(user_id): #take in user id
#     return User.query.get(user_id) #query db table and find user_id and store them in current session

class User(db.Model,UserMixin): #3 create class user and inherit  SQLA Models class 
    id = db.Column(db.String, primary_key = True)                       #3
    username = db.Column(db.String(150), nullable = False, default="") #3 nullable allows empty/none field
    email = db.Column(db.String(150), nullable = False)                 #3
    password = db.Column(db.String, nullable = False,default="")        #3
    token = db.Column(db.String,default="", unique = True)              #3 unique=SERIAL
    tweet = db.relationship('Tweet', backref='author', lazy = True) #4 if you do .user_token.author will join User and Tweet table and show the instance of matching id

#init class 
    def __init__(self,username,email,password,token=""):
        self.id = self.set_id() #use set_id method to get id
        self.username = username
        self.email = email 
        self.password = self.set_password(password) # set_password method takes in password from above class input
        self.token = self.set_token(24)  #method with length 24

    def set_id(self):
        return str(uuid.uuid4())

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_password(self, password): 
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f'{self.username} has been created with {self.email}'

class Tweet(db.Model):
    id = db.Column(db.String, primary_key=True)
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, content, user_id, id = ''):
        self.id = self.set_id()
        self.content = content
        self.user_id = user_id
        
    def __repr__(self):
        return f'{self.content} \n by {self.user_id}.'
        
    def set_id(self):
        return str(uuid.uuid4())
        