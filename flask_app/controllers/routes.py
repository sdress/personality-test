from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt        
from flask_app.models.model_name import Class_Name

bcrypt = Bcrypt(app)

@app.route('/')
def show_home_page():
    return render_template('index.html')

@app.route('/create-user', methods=['POST'])
def create_user():
    if not User.validate(request.form):
        return redirect('/')
    data = {
        'key': request.form['value'],
    }
    user_id = User.create(data)
    session['user_id'] = user_id
    return redirect('/wall')

@app.route('/dashboard')
def show_dashboard():
    if 'user_id' not in session:
        flash('You must be logged in to view')
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template('wall.html', user=User.get_from_id(data))