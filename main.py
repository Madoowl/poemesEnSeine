from website import create_app

app = create_app()

if __name__ == '__main__': #assure the running of the web server when running command 
    app.run(debug=True) #hot auto load, to be put off on deployement