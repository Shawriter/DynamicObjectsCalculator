from . import main
from flask import render_template, redirect, url_for, request, flash, jsonify
from .. import db_conn
from ..main.forms import LoginForm, RegisterForm
from ..database import db
from .. import db_conn
from flask_login import logout_user, login_required

@main.route('/', methods=['GET', 'POST'])
def index():
    username = None
    password = None
    form = LoginForm()
    return render_template('index.html', form=form)

@main.route('/front', methods=['GET', 'POST'])
@login_required
def front():
    return render_template('front.html')



@main.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/search', methods=['GET', 'POST'])
@login_required
def search(*args, **kwargs): 
    search = request.args.get('q')
    query = db_conn.session.query(db.Content)
    pictures = db_conn.session.query(db.Picture)
    print(query)
    if search:
        query = query.filter(db.Content.title.contains(search))
        pictures = pictures.filter(db.Picture.content_id.in_(query.with_entities(db.Content.id)))
    results = query.all()
    pictures = pictures.all()
    print(type(pictures), type(results))
    zipped_data = zip(pictures, results)
    return search_results(zipped_data)

@main.route('/search-results', methods=['GET', 'POST'])
def search_results(results):
    return render_template('search_results.html', results=results)


