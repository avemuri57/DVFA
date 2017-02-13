from dvfa import app
from flask import render_template,url_for,redirect,request
from flask_login import current_user, login_user, logout_user, login_required
from wtforms import Form, BooleanField, TextField, validators
from .forms import *
from .models import Patient
from .common import db

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		form1 = LoginForm(request.form)
		print(form1.username)
		form = request.form
		p = authenticate(form['username'],form['password'])

		if p is None:
			return redirect('/')

		login_user(p)
		return render_template('index.html')

	return render_template('login.html')

# 
@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect('/')



@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/register')
def register():
	return 'Registration Page'

#Restricted Routes
@app.route('/dashboard')
def dashboard():
	return render_template('index.html')

@app.route('/settings')
def settings():
	return 'profile Settings'

#Admin routes
@app.route('/YWRtaW5pc3RyYXRvcg==')
@login_required
def admin_login():
	print(current_user.firstname)
	return 'admin login panel'

def authenticate(username,password):
	p = Patient.query.filter_by(username=username,password=password).first()
	return p


