import re
from flask import Blueprint, render_template #help on organizing the app

views = Blueprint('views', __name__) #easier to name as filename

@views.route('/') #decorator to main page
def home():
    return  render_template("home.html") 
    #pass