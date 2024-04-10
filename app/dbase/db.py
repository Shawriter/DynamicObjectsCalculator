from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
import os
from .. import db
import datetime, re 
from slugify import slugify

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


    @property
    def password(self):
        raise AttributeError('password: ')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
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

def slugify_decorator(cls):

    class slugWrapper(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.generate_slug()

        @staticmethod
        def slugify(s):
            return re.sub('[^\w]+', '-', s).lower()

        def generate_slug(self):
            self.slug = ''
            if self.content:
                self.slug = self.slugify(self.content)
            return self.slug

        def __repr__(self):
            return f'<{self.__class__.__name__} {self.content!r}>'
    
    return slugWrapper

@slugify_decorator
class UserContent(db.Model):
    __tablename__ = 'user_content'

    content_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

 
@slugify_decorator
class Content(db.Model):

    __tablename__ = 'content'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    public_content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Content {self.name!r}>'

