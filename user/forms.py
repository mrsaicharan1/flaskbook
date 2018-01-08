from flask_wtf import form
from wtf_form import validators,StringField,PasswordField
from wtfforms.fields.html5 import Emailfield

class RegisterForm(Form):
    first_name=StringField('First Name',[validators.Required()])
    last_name=StrngField('Last Name',[validators.Required()])
    email=EmailField('Email Address',[valiators.Required()])
    username=StringField('username',[validators.Required(),validators.length(min=4,max=25)])
    password=PasswordField('New password',[validators.DataRequired(),validators.EqualTo('confirm',message='Passwords must match'),validators.length(min=4,max=25)])
    confirm=PasswordField('Repeat password')