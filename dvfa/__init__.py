import sys
from flask import Flask
from flask_rbac import RBAC
from flask_login import LoginManager
from config import Config
from flask_sqlalchemy import SQLAlchemy

sys.dont_write_bytecode = True

app = Flask(__name__)
app.config.from_object(Config())

from .views import *
from .common import *

db.init_app(app)
rbac.init_app(app)
login_manager.init_app(app)



login_manager.login_view = "login"

@login_manager.user_loader
def load_user(id):
	return Patient.query.filter_by(id=id).first()