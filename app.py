from flask import Flask, request,render_template

app = Flask(__name__)

@app.route('/')
def index():
	return 'Login Page'

@app.route('/about')
def about():
	return 'About Page'

@app.route('/register')
def register():
	return 'Registration Page'

#Restricted Routes
@app.route('/profile')
def profile():
	return 'Profile Based on Users Role'

@app.route('/settings')
def settings():
	return 'profile Settings'





if __name__ == '__main__':
	app.run(debug=True)
