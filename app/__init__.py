import importlib
import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate

# Importing extensions
from app.extensions import bcrypt, db
# Importing blueprints
from app.routes.users import users

load_dotenv()


def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        static_url_path="/",
    )
    app.secret_key = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints
    if "users" not in app.blueprints:
        app.register_blueprint(users)

    # LoginManager setup
    login_manager = LoginManager()
    login_manager.init_app(app)
    user_repository = importlib.import_module("app.repositories.UserRepository")

    @login_manager.user_loader
    def load_user(user_id):
        return user_repository.get_by_id(user_id)

    # Initialize Migrate
    Migrate(app, db)
    # Enable CORS
    CORS(app)

    return app
