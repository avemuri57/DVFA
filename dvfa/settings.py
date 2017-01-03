import os

SECRET_KEY = 'ThisIsASecret'
Debug=True
DB_USERNAME='dbuser'
DB_PASSWORD=''
DATABASE_NAME='dvfa'
DB_HOST=os.getenv('IP','0.0.0.0')
DB_URI="mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME,DB_PASSWORD,DB_HOST,DATABASE_NAME) 
SQLALCHEMY_DATABASE_URI = DB_URI