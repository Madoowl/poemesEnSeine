import sqlalchemy
from . import db #import db object from . aka current folder

from flask_login import UserMixin #custom class for the user class manage authentification credentials
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #oneToMany Relation
    #TODO add id from places
    

class User(db.Model, UserMixin): #user Model
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #list of all the notes'id from one user