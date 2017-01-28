from flask import Flask
from flask_login import LoginManager
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

from home import views

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)