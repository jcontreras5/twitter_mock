from flask import Blueprint, render_template #1 
from flask import flash, redirect,url_for #3
from flask import request #2
from twitter_mock.forms import UserLoginForm #2 USL class
from twitter_mock.models import User,db,check_password_hash
from flask_login import login_user, logout_user, current_user, login_required #3 importing db and user class

auth = Blueprint('auth', __name__, template_folder='auth_templates') #1 auth BP class

@auth.route('/signup', methods = ['GET', 'POST']) #1 auth signup rte decor fun
def signup():
    form = UserLoginForm() #ins of ULF class as form
    # return render_template('signup.html', form = form)  #2 connected signup forms to html by form var
    try:
        if request.method == 'POST' and form.validate_on_submit(): # 2 request goes to template and grabs info from form
            email = form.email.data # 2 user input email
            password = form.password.data #2 user input email
            # print(email,password)

            user = User(email, password=password)#3
            db.session.add(user)#3
            db.session.commit()#3 one commit push to db

            #if no errors,then flash,(requires html call) via {msg}
            flash(f'You have successfully created account {email}','user-created')
            #redirect 
            return redirect(url_for('site.home'))
    
    except:
        raise Exception('Invalid form data: please check form')

    return render_template('signup.html', form = form)