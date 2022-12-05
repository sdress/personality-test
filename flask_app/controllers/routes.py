from flask_app import app
from flask import render_template, redirect, request, session, flash
# from flask_bcrypt import Bcrypt        
# from flask_app.models.model_name import Class_Name

# bcrypt = Bcrypt(app)

@app.route('/')
def show_home_page():
    return render_template('index.html')
    # return f"Hello World"