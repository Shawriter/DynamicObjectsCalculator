from flask import Blueprint, render_template, redirect, url_for, flash, request
from ..main.forms import ImageForm, ContentForm
import os
from .. import db_conn
from werkzeug.utils import secure_filename
from . import users
from ..database.db import UserContent, Content, Picture
from .. import config
from flask_login import login_required, current_user



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
def image_upload():  
    if current_user.is_authenticated:
        print("User is authenticated")
        
    if request.method == 'POST': 

        content_form = ContentForm(request.form)

        title = content_form.title.data
        public_content = content_form.body.data
        species = content_form.family.data
        
        image_file = request.files['file'] 
        filename = os.path.join(config['development'].IMAGES_DIR, 
                                    secure_filename(image_file.filename)) 
        
        filenamedb =  config['development'].IMAGES_DIR + "\\" + secure_filename(image_file.filename)
        print(filenamedb, 'filename and filenamedb')

        new_content = Content(name=title, title=title, public_content=public_content, species=species)
        new_content.image_path = filenamedb
        db_conn.session.add(new_content)
        db_conn.session.commit() 

        new_content_image = Picture(content_id=new_content.id, picture_url_slug=filenamedb) #content_id is a constraint
        db_conn.session.add(new_content_image)
        db_conn.session.commit()

            
        assert image_file and filename is not None, 'file and filename not found' 

        image_file.save(filename) 
        flash('Saved %s' % os.path.basename(filename), 'success') 
        return redirect(url_for('users.content')) 
  
    return render_template('index.html')


@users.route('/contents', methods=['GET', 'POST'])
def content():
    pictures = db_conn.session.query(Picture).all()
    return render_template('animal_list.html', pictures=pictures)

