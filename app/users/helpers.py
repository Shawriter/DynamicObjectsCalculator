from flask import render_template, request 
from ..database import db
from ..database.db import Content, UserContent, Picture
from .. import db_conn



class ContentHelpers:

    def __init__(self):
        pass

    @staticmethod
    def get_content(flag, slugified): 

        pictures = db_conn.session.query(Picture).all()
        contents = db_conn.session.query(Content).all()
        
        if flag is True: # I set this to prevent unnecessary queries
            content = Content.query.filter_by(title=slugified).first_or_404()
            picture = Picture.query.filter_by(content_id=content.id).first()
            picture_URI = picture.picture_url_slug
            zipped_data_detailed = zip(pictures, contents)
            return content, picture_URI, zipped_data_detailed
        
        zipped_data = zip(pictures, contents)
        
        return zipped_data