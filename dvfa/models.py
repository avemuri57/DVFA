from .common import db

# Patient -> 'patient'
class Patient(db.Model):
	#__tablename__ = "patients"

	id = db.Column(db.Integer,primary_key=True)
	firstname = db.Column(db.String(80))
	lastname = db.Column(db.String(80))
	username = db.Column(db.String(80),unique=True)
	email = db.Column(db.String(80),unique=True)
	password = db.Column(db.String(80),unique=True)
	ccn = db.Column(db.String(16),unique=True)
	ssn = db.Column(db.String(10),unique=True)

	def __init__(self,firstname,lastname,username,password,email,ccn,ssn):
		self.firstname=firstname
		self.lastname=lastname
		self.username=username
		self.password=password #Stored in plain-text
		self.email=email
		self.ccn=ccn
		self.ssn=ssn