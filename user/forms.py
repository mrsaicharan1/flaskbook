from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError
from flask_wtf.file import FileField, FileAllowed
import re
from models import User

class BaseUserForm(Form):
    first_name=StringField('First Name',[validators.Required()])
    last_name=StringField('Last Name',[validators.Required()])
    email=EmailField('Email Address',[validators.Required()])
    username=StringField('username',[validators.Required(),validators.length(min=4,max=25)])
    
class RegisterForm(BaseUserForm):
    password=PasswordField('New password',[validators.DataRequired(),validators.EqualTo('confirm',message='Passwords must match'),validators.length(min=4,max=25)])
    confirm=PasswordField('Repeat password')
    
    def validate_username(form,field):
        if User.objects.filter(username=field.data).first():
            raise ValidationError("username already exists")
        if not re.match(^[a-zA-Z0-9_-]{4,25}$,field.data):
            raise ValidationError("Invalid Username characters",field.data)
    
    def validate_email(form,field):
        if User.objects.filter(email=field.data).first():
            raise ValidationError("email already taken")


class LoginForm(Form):
    username=StringField('username',[validators.DataRequired()])
    password=PasswordField('password',[validators.DataRequired(),validators.length(min=4,max=25)])
    
class EditForm(BaseUserForm):
    pass        