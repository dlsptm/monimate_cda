import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate

from app.extensions import bcrypt, db
from app.repositories.UserRepository import UserRepository as user_repository
from app.routes.categories import categories
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

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "postgresql://dlsptm:dlsptm@database/monimate_test"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True

    db.init_app(app)
    bcrypt.init_app(app)

    if "users" not in [bp.name for bp in app.blueprints.values()]:
        app.register_blueprint(users)

    if "categories" not in [bp.name for bp in app.blueprints.values()]:
        app.register_blueprint(categories)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return user_repository.get_by_id(user_id)

    Migrate(app, db)
    CORS(app)
    return app
