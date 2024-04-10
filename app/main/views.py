from . import main
from flask import render_template, redirect, url_for, request, flash
from .forms import LoginForm, RegisterForm

@main.route('/', methods=['GET', 'POST'])
def index():
    username = None
    password = None
    form = LoginForm()
    if form.is_submitted() or form.validate_on_submit():
        flash('Login successful', 'success') 
        return redirect(url_for('main.front'))
    return render_template('index.html', username=username, password=password, form=form)


@main.route('/front', methods=['GET', 'POST'])
def front():
    return render_template('front.html')
