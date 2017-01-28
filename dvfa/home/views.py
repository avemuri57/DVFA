from dvfa import app
from flask import render_template,url_for,redirect
from flask_wtf import Form


@app.route('/')
def index():
	return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
	next = flask.request.args.get('next')
	return flask.redirect(next or flask.url_for('index'))

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

