from flask import Blueprint, render_template, request, flash #help on organizing the app

auth = Blueprint('auth', __name__) #easier to name as filename

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)    
    if request.method =='POST':
        pass
    elif request.method == 'GET':
        pass

    return render_template("login.html",  text="testing", user="Madoowl")

@auth.route('/logout')
def logout():
    return "<p>logout<p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method =='POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) <3:
            flash('email must be greater than 4 caracters', category='error')
        elif len(firstName) <2:
            flash('first name must be greater than 2 caracters', category='error')
        elif password1 != password2:
            flash('passwords do not match', category='error')
        elif len(password1)<7:
            flash('Password must be greater than 7 caracters', category='error')
        #TODO vérification regex
        else:
            flash('account created', category='success')
            # add user to DB

    elif request.method == 'GET':
        pass
    
    return render_template("sign_up.html")