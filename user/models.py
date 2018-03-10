from application import db
from utilities.common import utc_now_ts as now
from flask_mongoalchemy import MongoAlchemy
from mongoengine import signals

class User(db.Document):
    username = db.StringField(db_field='u',required=True)
    password = db.StringField(db_field='p',required=True)
    email = db.EmailField(db_field='e',required=True)
    first_name = db.StringField(db_field='fn',max_length=20)
    last_name = db.StringField(db_field='ln',max_length=20)
    created = db.IntField(db_field='cr',default=now())
    bio = db.StringField(db_field='b',max_length=160)
  
    meta =
    {
        'indexes' : [ 'username' , 'email' , '-created' ]
    }