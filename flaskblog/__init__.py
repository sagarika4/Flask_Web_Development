from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
import bcrypt
from flaskblog.config import Config


# 3 forward slashes mean relative path
db=SQLAlchemy()
login_manager=LoginManager()
login_manager.login_view='users.login'
login_manager.login_message_category='info'

mail=Mail()

from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main



def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)
	app.register_blueprint(users)
	app.register_blueprint(posts)
	app.register_blueprint(main)

	return app
