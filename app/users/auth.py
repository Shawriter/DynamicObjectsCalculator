from . import users
from flask import render_template, redirect, url_for, request, flash, g
from ..main.forms import LoginForm, RegisterForm
from app import login_manager
from flask_login import login_user, logout_user, login_required, current_user
from ..database import db
from .. import db_conn

@login_manager.user_loader 
def _user_loader(user_id): 
    return db.User.query.get(int(user_id))

@users.route('/login', methods=['POST'])
def login():
    print("IN LOGIN FUNCTION")
    user = request.form.get('username')
    password = request.form.get('password')
    print(user, password)
    def login_final(username): 
        if request.method == "POST": 
            form = LoginForm() 
        try:
            print("TRYING")
            print(request.form)
            if form.validate(): 
                    print("VALIDATING")
                    login_user(username) 
                    print("LOGGING IN")
                    flash("Successfully logged in" , "success") 
                    print("FLASHING")
                    
                    return redirect(url_for('main.front'))
            else: 
                print(form.errors)
                form = LoginForm() 
                return render_template('index.html', form=form)
        except Exception as e:
            print(e)
            return False
    
    def authenticate(user, password):
        try: 
            print("USER AUTHENTICATING")
            user = db.User.query.filter_by(username=user).first() 
            print(type(user))
            #print(user.password)
            if user and user.check_password(password): 
                print("HELLO")
                print(type(user))
                
                return login_final(user)
                
            
        except Exception as e:
            print(e)
            return False
        
    response = authenticate(user, password)
    if response:
        return response
    else:
        form = LoginForm()
        return render_template('404.html')


@users.route('/logout/', methods=['GET', 'POST'])
@login_required
def logout():
    
    if current_user.is_authenticated:
        logout_user() 
        flash('You have been logged out.', 'success') 
    else:
        flash('You were not logged in.', 'danger')
        return redirect(url_for('main.index'))
    return redirect(url_for('main.index'))


@users.route('/register', methods=['GET', 'POST'])
def register():
    print("Register")
    usernamereg = None
    passwordreg = None
    confirmpasswordreg = None
    emailreg = None
    confirmemailreg = None
    form = RegisterForm()
    print("Register")
    if form.is_submitted():
        print("Submitted")
        try:
            user = db.User.create_new_user(form.usernamereg.data, form.passwordreg.data, form.emailreg.data)
            print("Creating1")
            db_conn.session.add(user)
            db_conn.session.commit()
            flash('Registration complete', 'success')
        except Exception as e:
            print("Error")
            print(e)
            flash('Registration failed', 'danger')
    return render_template('registration.html', usernamereg=usernamereg, passwordreg=passwordreg, confirmpasswordreg=confirmpasswordreg, emailreg=emailreg, confirmemailreg=confirmemailreg, form=form)