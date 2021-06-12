from flask import Flask

def create_app():
    app= Flask(__name__) #initialize Flask
    app.config['SECRET_KEY'] = 'my secret key' # TODO secure cookies from session data, look up needed

    return app #TODO make a global ?
    

