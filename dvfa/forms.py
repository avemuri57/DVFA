from flask_wtf import Form
from wtforms import TextField

class LoginForm(Form):
	username = TextField("Username")
	password = TextField("Password")