#from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from ..database import db
#from ..users.auth import login
#from ..users import helpers

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

class DropDown(FlaskForm):

    @staticmethod
    def get_families() -> list:
        
        all_families = [
            ('Apidae', 'Bees'),
            ('Accipitridae', 'Hawks, Eagles'),
            ('Ambystomatidae', 'Mole Salamanders'),
            ('Anatidae', 'Ducks, Geese, Swans'),
            ('Bufonidae', 'Toads'),
            ('Bovidae', 'Cattle, Goats, Sheep'),
            ('Canidae', 'Dogs'),
            ('Cheloniidae', 'Sea Turtles'),
            ('Cervidae', 'Deer'),
            ('Cichlidae', 'Cichlids'),
            ('Columbidae', 'Pigeons, Doves'),
            ('Crocodylidae', 'Crocodiles'),
            ('Cyprinidae', 'Carps, Minnows'),
            ('Drosophilidae', 'Fruit Flies'),
            ('Elephantidae', 'Elephants'),
            ('Equidae', 'Horses, Zebras'),
            ('Falconidae', 'Falcons'),
            ('Felidae', 'Cats'),
            ('Formicidae', 'Ants'),
            ('Gobiidae', 'Gobies'),
            ('Haemulidae', 'Grunts, Sweetlips'),
            ('Hominidae', 'Great Apes, including Humans'),
            ('Hylidae', 'Tree Frogs'),
            ('Lepidoptera', 'Butterflies, Moths'),
            ('Passeridae', 'Sparrows'),
            ('Psittacidae', 'Parrots'),
            ('Pythonidae', 'Pythons'),
            ('Ranidae', 'True Frogs'),
            ('Salmonidae', 'Salmons, Trouts'),
            ('Scarabaeidae', 'Scarab Beetles'),
            ('Scombridae', 'Mackerels, Tunas'),
            ('Strigidae', 'Owls'),
            ('Tetraodontidae', 'Pufferfishes'),
            ('Testudinidae', 'Tortoises'),
            ('Tettigoniidae', 'Katydids'),
            ('Ursidae', 'Bears'),
            ('Viperidae', 'Vipers'),
            ('NOT LISTED', 'Not Listed')
        ]
        
        all_families_sorted = sorted(all_families, key=lambda x: x[1])
        #print(all_families_sorted)
        return all_families_sorted
       

class ContentForm(FlaskForm): 
    title = StringField('Title', validators=[DataRequired()]) 
    body = TextAreaField('Body', validators=[DataRequired()]) 
    family = SelectField('Family', choices=DropDown.get_families())

    
    def save_entry(self, entry):         
       self.populate_obj(entry)         
       entry.generate_slug()
       return entry