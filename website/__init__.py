from re import A
from flask import Flask

def create_app():
    app= Flask(__name__) #initialize Flask
    app.config['SECRET_KEY'] = 'my secret key' # TODO secure cookies from session data, look up needed

    from .views import views #importing the blueprint
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    
    return app #TODO make a global ?


