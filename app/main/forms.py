#from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from ..database import db
#from ..users.auth import login

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')
    def validate(self): 

        if not super(LoginForm, self).validate(): 
            return False 
        else:
            return True
    

class RegisterForm(FlaskForm):
    usernamereg = StringField('Username', validators=[DataRequired()])
    passwordreg = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirmpasswordreg = PasswordField('Confirm password', validators=[DataRequired(), Length(min=8, max=20), EqualTo('passwordreg')])
    emailreg = StringField('Email', validators=[DataRequired(), Email()])
    confirmemailreg = StringField('Confirm email', validators=[DataRequired(), EqualTo('emailreg')])
    submitreg = SubmitField('Register')

    def validate_email(self, field):
        if db.User.query.filter_by(email=field.data.lower()).first():
            print('Email taken')

    def validate_username(self, field):
        if db.User.query.filter_by(username=field.data).first():
            print('Username taken')



class ImageForm(FlaskForm):
    file = FileField('Image', validators=[DataRequired()])
    submit = SubmitField('Upload')

class Content(FlaskForm):  
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ContentForm(FlaskForm): 
    title = StringField('Title', validators=[DataRequired()]) 
    body = TextAreaField('Body', validators=[DataRequired()]) 
    status = SelectField('Status', choices=[('draft', 'Draft'), ('published', 'Published')])
    def save_entry(self, entry):         
       self.populate_obj(entry)         
       entry.generate_slug()
       return entry