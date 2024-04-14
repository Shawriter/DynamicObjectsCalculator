from . import main
from flask import render_template, redirect, url_for, request, flash
from .. import db_conn
from ..main.forms import LoginForm, RegisterForm

@main.route('/', methods=['GET', 'POST'])
def index():
    username = None
    password = None
    form = LoginForm()
    return render_template('index.html', form=form)

@main.route('/front', methods=['GET', 'POST'])
def front():
    return render_template('front.html')



@main.route('/logout', methods=['GET', 'POST'])
def logout():
    return redirect(url_for('main.index'))



