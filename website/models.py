import sqlalchemy
from . import db #import db object from . aka current folder

from flask_login import UserMixin #custom class for the user class manage authentification credentials
from sqlalchemy.sql import func

import pandas as pd
import json


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #oneToMany Relation
    #join to a public API with a link
    
    #topos_id = db.Column(db.Integer,db.ForeignKey('topos.id')) #onToMany relatio
    #TODO add id from places
    

class User(db.Model, UserMixin): #user Model
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #list of all the notes'id from one user
    role =  db.Column(db.Integer,unique=False) #geestion des droits utilisateurs

    # TODO add open data file ? add topos table ? - normalisation 1 ? choix technique ?
# class Topos(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255)) #étiquette
#     city = db.Column(db.String(50))
#     details = db.Column(db.String(500))
#     notes = db.relationship('Note')

    

