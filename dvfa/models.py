from flask_login import UserMixin
from .common import db

# Patient -> 'patient'
class Patient(db.Model, UserMixin):
	#__tablename__ = "patients"

	id = db.Column(db.Integer,primary_key=True)
	firstname = db.Column(db.String(80))
	lastname = db.Column(db.String(80))
	username = db.Column(db.String(80),unique=True)
	email = db.Column(db.String(80),unique=True)
	password = db.Column(db.String(80),unique=True)
	ccn = db.Column(db.String(16),unique=True)
	ssn = db.Column(db.String(10),unique=True)

	def __init__(self):
		pass
	