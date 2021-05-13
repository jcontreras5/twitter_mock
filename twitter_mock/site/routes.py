# from forms import TForm
from flask import Blueprint, render_template #1
from flask_login import login_required
site = Blueprint('site', __name__, template_folder='site_templates') #1 create site BP

"""
IN the above code, some arguments are specified when creating the Blueprint object
This first argument 'site', is the Blueprint's name,
this will be used by flasks routing mechanism.
The second parameter __name__, is the BP's import name,
which flask uses to locate resources
"""
#1 index decor func
@site.route('/') 
def home():
    return render_template('index.html')

#1 profile decor func
@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

# @site.route('/createtweet', methods=['GET','POST'])
# @login_required
# def createtweet():
#     form = TForm() #9 parentheses 
#     if request.method == 'POST' and form.validate():
#         tweet = form.tweet.data
#         user_id = current_user.id #10 change to username
#         print(tweet)
#         tweet = Post(title, tweet, user_id)
#         db.session.add(post) #1 post typo
#         db.session.commit()
#         return redirect(url_for('site.createtweet'))
#     return render_template("createtweet.html", form = form)

