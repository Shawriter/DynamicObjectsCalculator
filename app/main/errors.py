from . import main
from flask import render_template, redirect, url_for, request


@main.errorhandler(404)
def errorhandler(e):
    return render_template('404.html', e=e)