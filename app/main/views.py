from . import main
from flask import render_template, redirect, url_for, request, flash, jsonify
from .. import db_conn
from ..main.forms import LoginForm, RegisterForm
from ..database import db
from .. import db_conn

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

@main.route('/search', methods=['GET', 'POST'])
def search(*args, **kwargs): 
    search = request.args.get('q')
    query = db_conn.session.query(db.Content)
    print(query)
    if search:
        query = query.filter(db.Content.public_content.contains(search))
    results = query.all()
    print(results[0].title)
    return search_results(results)

@main.route('/search-results', methods=['GET', 'POST'])
def search_results(results):
    return render_template('search_results.html', results=results)
