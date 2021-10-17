# from forms import TForm
from twitter_mock.models import Tweet, User, db
from flask import Blueprint, render_template,request,redirect,url_for #1
from flask_login import login_required, current_user
site = Blueprint('site', __name__, template_folder='site_templates') #1 create site BP
from twitter_mock.forms import TForm


"""
IN the above code, some arguments are specified when creating the Blueprint object
This first argument 'site', is the Blueprint's name,
this will be used by flasks routing mechanism.
The second parameter __name__, is the BP's import name,
which flask uses to locate resources
"""
#1 index decor func
@site.route('/', methods = ['GET', 'POST']) 
def home():
    tweets = Tweet.query.all()
    return render_template('index.html', tweets = tweets)

#1 profile decor func
@site.route('/explore')
@login_required
def explore():
    users=User.query.all()
    return render_template('explore.html', users=users)

@site.route('/createtweet', methods=['GET', 'POST'])
@login_required
def createtweet():
    form = TForm() 
    if request.method == 'POST' and form.validate():
        tweet = form.tweet.data
        user_id = current_user.id 
        print(tweet)
        tweet = Tweet(tweet, user_id)
        db.session.add(tweet)
        db.session.commit()
        return redirect(url_for('site.home'))
    return render_template("createtweet.html", form = form)


