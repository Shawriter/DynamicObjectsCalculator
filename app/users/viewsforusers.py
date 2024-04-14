from flask import Blueprint, render_template, redirect, url_for, flash, request
from ..main.forms import ImageForm
import os
from ..main.forms import ContentForm
from .. import db_conn
from werkzeug.utils import secure_filename
from . import users
from ..database.db import UserContent, Content
from .. import config
from flask_login import login_required



@users.route('/profile/<slug>', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html')


@users.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = ContentForm()
    return render_template('addanimalobject.html', form=form)


@users.route('/add', methods=['GET', 'POST']) 
@login_required
def create(): 
    if request.method == 'POST': 
        form = ContentForm(request.form) 
        
        if form.validate(): 
            entry = form.save_entry() 

            assert entry and db_conn.session is not None, 'object not found'
            #db_conn.session.add(entry) 
            #db_conn.session.commit() 
            #return redirect(url_for('entries.detail', slug=entry.slug)) 
    else: 
        form = ContentForm() 
        
    return render_template('addanimalobject.html', form=form, image_upload=image_upload)

@users.route('/', methods=['GET', 'POST']) 
@login_required
def edit(slug): 
    entry = Content.query.filter(Content.slug == slug).first_or_404() 
    if request.method == 'POST': 
        form = ContentForm(request.form, obj=entry) 
        if form.validate(): 
            entry = form.save_entry(entry) 

            assert entry and db_conn.session is not None, 'object not found'

            #db_conn.session.add(entry) 
            #db_conn.session.commit() 
            return redirect(url_for('entries.detail', slug=entry.slug)) 
    else: 
        form = ContentForm(obj=entry) 
  
    return render_template('addanimalobject.html', entry=entry, form=form)

@users.route('/create', methods=['GET', 'POST'])
@login_required 
def image_upload(): 
    if request.method == 'POST': 
        form = ImageForm(request.form) 
        image_file = request.files['file'] 
        filename = os.path.join(config['development'].IMAGES_DIR, 
                                    secure_filename(image_file.filename)) 
            
        assert image_file and filename is not None, 'file and filename not found' 

        image_file.save(filename) 
        flash('Saved %s' % os.path.basename(filename), 'success') 
        return redirect(url_for('main.index')) 
  
    return render_template('index.html', form=form)

