from flask import Blueprint, render_template, redirect, url_for, flash, request
from ..main.forms import ImageForm
import os
from werkzeug.utils import secure_filename
from . import users
from . import app


@users.route('/post/', methods=['GET', 'POST']) 
def image_upload(): 
    if request.method == 'POST': 
        form = ImageForm(request.form) 
        if form.validate(): 
            image_file = request.files['file'] 
            filename = os.path.join(app.config['IMAGES_DIR'], 
                                    secure_filename(image_file.filename)) 
            image_file.save(filename) 
            flash('Saved %s' % os.path.basename(filename), 'success') 
            return redirect(url_for('main.index')) 
    else: 
        form = ImageForm()

    return render_template('image_upload.html', form=form)

@users.route('/profile/', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')

