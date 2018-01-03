from flask import Flask

from flask_mongoengine import MongoEngine
#assign global variable db
db=MongoEngine()

def create_app():
        
    app = Flask(__name__)
    
    app.config.from_pyfile('settings.py')
    
    #initialize database for application
    db.init_app(app)
    
    from user.views import user_app
    
    app.register_blueprint(user_app)
    
    return app
