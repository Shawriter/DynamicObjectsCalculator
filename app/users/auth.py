from . import users
from flask import render_template, redirect, url_for, request, flash, g
from ..main.forms import LoginForm, RegisterForm
from app import login_manager
from .. import db

@login_manager.user_loader 
def _user_loader(user_id): 
    return db.User.query.get(int(user_id))

@users.route('/login', methods=['POST'])
def login(user, password, email):

    assert user and password and email
    
    def authenticate(user, password, email):
        try: 
            user = db.User.query.filter(db.User.username == email).first() 
            if user and user.check_password(password): 
                return user 
            return False
        except Exception as e:
            print(e)
            return False
        
    authenticate(user, password, email)
    return render_template('front.html')
    

@users.route('/register', methods=['GET', 'POST'])
def register():
    usernamereg = None
    passwordreg = None
    confirmpasswordreg = None
    emailreg = None
    confirmemailreg = None
    form = RegisterForm()
    if form.is_submitted() or form.validate_on_submit():
        flash('Registration complete', 'success')
        return redirect(url_for('main.index'))
    return render_template('registration.html', usernamereg=usernamereg, passwordreg=passwordreg, confirmpasswordreg=confirmpasswordreg, emailreg=emailreg, confirmemailreg=confirmemailreg, form=form)