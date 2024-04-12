from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from ..dbase import db

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    usernamereg = StringField('Username', validators=[DataRequired()])
    passwordreg = StringField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirmpasswordreg = StringField('Confirm password', validators=[DataRequired(), Length(min=8, max=20), EqualTo('passwordreg')])
    emailreg = StringField('Email', validators=[DataRequired(), Email()])
    confirmemailreg = StringField('Confirm email', validators=[DataRequired(), EqualTo('emailreg')])
    submitreg = SubmitField('Register')



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