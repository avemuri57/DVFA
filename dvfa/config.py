import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
	SECRET_KEY = 'ThisIsASecret'
	DB_USERNAME='dbuser'
	DB_PASSWORD=''
	DATABASE_NAME='dvfa'
	DB_HOST=os.getenv('IP','0.0.0.0')
	DB_URI="mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME,DB_PASSWORD,DB_HOST,DATABASE_NAME) 
	SQLALCHEMY_DATABASE_URI = DB_URI	
	WTF_CSRF_ENABLED = True
	SECRET_KEY = 'you-will-never-guess'
