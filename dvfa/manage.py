import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
from dvfa import app
from dvfa.common import db
from dvfa.models import *

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


manager.add_command("runserver",Server(
	use_debugger=True,
	use_reloader=True,
	host=os.getenv("IP",'0.0.0.0'),
	port = int(os.getenv('PORT',8082))
	) 
)

if __name__ == "__main__":
	manager.run()