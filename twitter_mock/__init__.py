#1.1
from flask import Flask  
from config import Config

#1.2
from .site.routes import site 
from .authentication.routes import auth 

# #1.3
from twitter_mock.models import db as root_db ,login_manager
from flask_migrate import Migrate #moves data betwen FLASK and DB via .env, stores changes of models as well
from twitter_mock import models #3 make models available to whole 

#1.1
app = Flask(__name__)
app.config.from_object(Config)

#1.2
app.register_blueprint(site) #1 site bp init
app.register_blueprint(auth) #1 auth bp init

#1.3
root_db.init_app(app) #3 db init
migrate = Migrate(app,root_db) #3 pass in app and db
login_manager.init_app(app)#3
login_manager.login_view = 'auth.signin' #3 specify rte for non authroized user

