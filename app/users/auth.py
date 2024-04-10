from . import users
from flask import render_template, redirect, url_for, request, flash
from ..main.forms import LoginForm, RegisterForm

@users.route('/login', methods=['POST'])
def login():
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