import re
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.json import jsonify #help on organizing the app

from flask_login import login_required, current_user
from .models import Note, User
from . import db
import json

from sqlalchemy import select

views = Blueprint('views', __name__) #easier to name as filename

@views.route('/', methods=['GET','POST']) #decorator to main page
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 5:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    print(current_user.get_id())
    return render_template("home.html", user=current_user, user_id=current_user.get_id()) 
    
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if str(note.user_id) == current_user.get_id():
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route(f'/update-note/<int:id>', methods=['POST','GET'])
def update_note(id):
    note = Note.query.filter_by(id=id).first()
    print(note)
    
    if request.method == 'POST':
        if note.user_id == current_user :
            new_note = request.form.get('note')
            note.data = new_note
            db.session.commit()
            flash('update executed', category='success')
            return render_template("home.html", user=current_user)
        else:
            flash('Not yours to edit...', category='error')
            return redirect(url_for('views.home'))
    else :
        flash('On your way to edit, sure?', category='message')
        
        return render_template("update.html", user=current_user, note=note)


# @views.route('/add-topos',methods=['POST','GET'])
# @login_required
# def add_topos():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         city = request.form.get('city')
#         details = request.form.get('details')

#     topos = Topos.query.filter_by(name=name).first()
#     if topos:
#         flash('This site already exists!', category='error')
#     else:
#         new_topos= Topos(name=name, city=city,details=details)

#     return render_template("topos.html", user=current_user)