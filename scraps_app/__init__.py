from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from scraps_app.config import Config
import os
''' init for project. Creates a flask app and db instance'''
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)



###########################
# Authentication
###########################


bcrypt = Bcrypt(app) 

###########################
# Blueprints
###########################

from scraps_app.main.routes import main
app.register_blueprint(main)

from scraps_app.auth.routes import auth
app.register_blueprint(auth)

with app.app_context():
    db.create_all()