from flask_mongoalchemy import MongoAlchemy
from mongoengine import signals

from application import db
from utilities.common import utc_now_ts as now

class User(db.Document):
    username = db.StringField(db_field='u',required=True)
    password = db.StringField(db_field='p',required=True)
    email = db.EmailField(db_field='e',required=True)
    first_name = db.StringField(db_field='fn',max_length=20)
    last_name = db.StringField(db_field='ln',max_length=20)
    created = db.IntField(db_field='cr',default=now())
    bio = db.StringField(db_field='b',max_length=160)
    
 #   @classmethod # decorator used to save the credentials in lowercase
  #  def pre_save(cls, sender, document, **kwargs):
   #     document.username = document.username.lower()
    #    email.username = email.username.lower() 

# signals.pre_save.connect(User.pre_save, sender = User)