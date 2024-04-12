from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
import os
#from .. import db
#from ..main.extradecorators import slugify_decorator
basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev_database.db')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

#engine = create_engine(SQLALCHEMY_DATABASE_URI)
#@slugify_decorator
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    slug = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.slug = self.generate_slug()


    def get_id(self): 
        return str(self.id) 
  
    def is_authenticated(self): 
        return True 
    
    def is_anonymous(self): 
        return False

    @property
    def password(self):
        raise AttributeError('password: ')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        return self.password_hash

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @classmethod 
    def create_new_user(cls, username, password,  email, **kwargs): 
        assert username and password and email, 'username, password, email are required'
        return User(username=username, password_hash=User.password(password), email=email,**kwargs)
    
    def __str__(self) -> str:
        return f'<User {self.slug!r}>'

    
    def __repr__(self):
        return f'<User {self.name!r}>'''


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String, unique=True, nullable=False)

class UserRole(db.Model):
    __tablename__ = 'user_roles'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)



#@slugify_decorator
class UserContent(db.Model):
    __tablename__ = 'user_content'

    content_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

 
#@slugify_decorator
class Content(db.Model):

    __tablename__ = 'content'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    public_content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Content {self.name!r}>'


with app.app_context():
    db.create_all()