from . import main
from flask import render_template, redirect, url_for, request, flash
from .forms import LoginForm, RegisterForm

@main.route('/', methods=['GET', 'POST'])
def index():
    username = None
    password = None
    form = LoginForm()
    return render_template('index.html', form=form, username=username, password=password)


