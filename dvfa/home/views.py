from dvfa import app
from flask import render_template,url_for,redirect,request
from wtforms import Form, BooleanField, TextField, validators


@app.route('/')
def index():
	return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
	#form LoginForm(request.POST)
	if request.method == 'POST':
		return render_template('index.html')

	return render_template('login.html')

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
def admin_login():
	return 'admin login panel'

