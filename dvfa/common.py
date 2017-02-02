from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_rbac import RBAC


db = SQLAlchemy()
login_manager = LoginManager()
rbac = RBAC()