from flask import Blueprint, render_template, redirect, url_for, flash, request
from ..main.forms import ImageForm, ContentForm
import os
from .. import db_conn
from werkzeug.utils import secure_filename
from . import users
from ..database.db import UserContent, Content, Picture
from .. import config


from flask_login import login_required, current_user
import datetime
from . import helpers

@users.route('/profile/<slugified>', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html')


@users.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = ContentForm()
    return render_template('addanimalobject.html', form=form)


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
        
        filenamedb =  "/uploads/" + secure_filename(image_file.filename)

        #assert image_file and filename is not None, 'file and filename not found' 

        #print(filenamedb, 'filename and filenamedb')

        try:
            query = db_conn.session.query(Content).filter_by(title=Content.title).first()
            if image_file and filename != None:

                new_content = Content(name=title, title=title, public_content=public_content, species=species)
                new_content.image_path = filenamedb

                if query is title:
                    flash('Content already exists', 'alert')
                    return redirect(url_for('users.add'))
                else:
                    db_conn.session.add(new_content)
                    db_conn.session.commit() 

                if os.path.exists(image_file.filename):
                    new_filename = secure_filename(image_file.filename + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    new_content_image = Picture(content_id=new_content.id, picture_url_slug=new_filename)

                    db_conn.session.add(new_content_image)
                    db_conn.session.commit()
                    image_file.save(new_filename)
                else:
                    new_content_image = Picture(content_id=new_content.id, picture_url_slug=filenamedb) #content_id is a constraint
            
                    db_conn.session.add(new_content_image)
                    db_conn.session.commit()
                    image_file.save(filename) 
            else:
                flash('No file selected', 'alert')
                return redirect(url_for('users.add'))
             
        except Exception as e:
            print(e)
            db_conn.session.rollback()
            flash('Error saving content', 'error')
            return redirect(url_for('users.content'))


        
        flash('Saved content! Content is displayed in the animal list.', 'success') 
        return redirect(url_for('users.add')) 
  
    return render_template('index.html')


@users.route('/contents', methods=['GET', 'POST'])
def content():
 
    zipped_data = helpers.ContentHelpers.get_content(False, None)

    return render_template('animal_list.html',contents=zipped_data)



@users.route('/<slugified>', methods=['GET', 'POST'])
def content_detail(slugified):
    

    content, picture_URI, zipped_data_detailed = helpers.ContentHelpers.get_content(True, slugified)
    
    return render_template('object_detail.html', content=content, title=slugified, picture=picture_URI, contents=zipped_data_detailed)


@users.route('/next/<slugified>/<next_flag>', methods=['GET', 'POST'])
def next_previous(slugified, next_flag):
   
    content, picture_URI, zipped_data_detailed = helpers.ContentHelpers.get_content(True, slugified)

    previous_animal = slugified
    #print(slugified)
    #print(type(content))
    try:

        if next_flag == 'True':
            i = 0
            contents_dict = None
            content_list = []
            picture_list = []
            #print(zipped_data_detailed)
            for picture, contents in zipped_data_detailed:
                i += 1
                #print(contents.title, picture.picture_url_slug)
                content_list.append(contents.title)
                picture_list.append(picture.picture_url_slug)

                
            for i in range(len(content_list)):

                if content_list[i] == previous_animal:
                    next_animal = content_list.index(previous_animal)+1
                    next_picture = picture_list.index('/uploads/' + previous_animal.lower() + '.jpg')+1
                    #print(contents.title, previous_animal)
                    next_animal_title = content_list[next_animal]
                    
                    next_animal_picture = picture_list[next_picture]

                    next_picture_2 = next_animal_picture.lstrip('/')
              
                    
    except Exception as e:
            print(e)
            return render_template('object_detail.html', content=content, title=slugified, picture=picture_URI)
    
    return redirect(url_for('users.iter_route',next_animal_picture=next_picture_2, slugified=next_animal_title))
    

@users.route('/<slugified>', methods=['GET', 'POST'])
def iter_route(slugified):
    content = Content.query.filter_by(title=slugified).first_or_404()
    picture = Picture.query.filter_by(content_id=content.id).first()
    picture_URI = picture.picture_url_slug
    print(slugified,content, picture_URI)
    return render_template('object_detail.html', content=content, title=slugified, picture=picture_URI)
