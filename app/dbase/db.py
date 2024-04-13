from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
import os
import slugify
from .. import db_conn
from ..main.extradecorators import slugify_decorator
import re


#@slugify_decorator
class User(UserMixin, db_conn.Model):
    __tablename__ = 'users'

    id = db_conn.Column(db_conn.Integer, primary_key=True)
    username = db_conn.Column(db_conn.String, unique=True, nullable=False)
    password_hash = db_conn.Column(db_conn.String, nullable=False)
    email = db_conn.Column(db_conn.String, unique=True, nullable=False)
    #slug = db_conn.Column(db_conn.String, unique=True, nullable=False)
    created_at = db_conn.Column(db_conn.DateTime, default=db_conn.func.current_timestamp())
    updated_at = db_conn.Column(db_conn.DateTime, default=db_conn.func.current_timestamp(), onupdate=db_conn.func.current_timestamp())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.slug = self.generate_slug()

    @property
    def password(self):

        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):

        self.password_hash = generate_password_hash(password)
        return self.password_hash

    def verify_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)

    def check_password(self, password) -> bool:
        return self.verify_password(password)
        
    @classmethod 
    def create_new_user(cls, username, password,  email, **kwargs) -> object: 
        assert username and password and email, 'username, password, email are required'
        print('Creating new user', username, password, email)
        user = User(username=username, email=email)
        user.password = password
        print("Creating")
        return user
    
    def __str__(self) -> str:
        return f'<User {self.slug!r}>'

    
    def __repr__(self):
        return f'<User {self.name!r}>'''


class Role(db_conn.Model):
    __tablename__ = 'roles'

    id = db_conn.Column(db_conn.Integer, primary_key=True)
    role_name = db_conn.Column(db_conn.String, unique=True, nullable=False)

class UserRole(db_conn.Model):
    __tablename__ = 'user_roles'

    user_id = db_conn.Column(db_conn.Integer, db_conn.ForeignKey('users.id'), primary_key=True)
    role_id = db_conn.Column(db_conn.Integer, db_conn.ForeignKey('roles.id'), primary_key=True)



@slugify_decorator
class UserContent(db_conn.Model):
    __tablename__ = 'user_content'

    content_id = db_conn.Column(db_conn.Integer, primary_key=True)
    user_id = db_conn.Column(db_conn.Integer, db_conn.ForeignKey('users.id'), nullable=False)
    content = db_conn.Column(db_conn.Text, nullable=False)
    created_at = db_conn.Column(db_conn.DateTime, default=db_conn.func.current_timestamp())

 
@slugify_decorator
class Content(db_conn.Model):

    __tablename__ = 'content'

    id = db_conn.Column(db_conn.Integer, primary_key=True)
    name = db_conn.Column(db_conn.String, nullable=False)
    public_content = db_conn.Column(db_conn.Text, nullable=False)

    def __repr__(self):
        return f'<Content {self.name!r}>'
