from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError
from flask_wtf.file import FileField, FileAllowed
import re

from models import user

class RegisterForm(Form):
    first_name=StringField('First Name',[validators.Required()])
    last_name=StringField('Last Name',[validators.Required()])
    email=EmailField('Email Address',[validators.Required()])
    username=StringField('username',[validators.Required(),validators.length(min=4,max=25)])
    password=PasswordField('New password',[validators.DataRequired(),validators.EqualTo('confirm',message='Passwords must match'),validators.length(min=4,max=25)])
    confirm=PasswordField('Repeat password')