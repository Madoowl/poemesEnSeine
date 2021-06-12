import re
from flask import Blueprint
from flask.templating import render_template #help on organizing the app

auth = Blueprint('auth', __name__) #easier to name as filename

@auth.route('/login')
def login():
    return render_template("login.html",  text="testing", user="Madoowl")

@auth.route('/logout')
def logout():
    return "<p>logout<p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")