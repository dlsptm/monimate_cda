import json
import os

import pytest
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate

from app.extensions import bcrypt, db
from app.routes.users import users


def create_test_app():
    load_dotenv()
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        static_url_path="/",
    )
    app.secret_key = os.getenv("SECRET_KEY")

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL_TEST",'postgresql://postgres:postgres@database/monimate_test')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["DEBUG"] = True

    db.init_app(app)
    bcrypt.init_app(app)

    if "users" not in [bp.name for bp in app.blueprints.values()]:
        app.register_blueprint(users)

    login_manager = LoginManager()
    login_manager.init_app(app)

    Migrate(app, db)
    CORS(app)
    return app


@pytest.fixture(scope="function")
def app():
    """Fixture pour créer l'application Flask pour les tests."""
    app = create_test_app()
    yield app
    # Nettoyage de la base de données après chaque tests
    with app.app_context():
        # Supprime toutes les tables après chaque tests
        db.drop_all()
        # Crée les tables (optionnel mais généralement utilisé)
        db.create_all()


# Fixture pour créer un client de tests
@pytest.fixture(scope="function")
def client(app):
    return app.test_client()


def test_register_success(client):
    """Test de l'enregistrement d'un utilisateur"""
    response = client.post(
        "/register",
        json={
            "email": "testusers@example.com",
            "password": "password123",
            "username": "testuser",
            "is_active": True,
        },
    )

    assert response.status_code == 201  # nosec

    response_data = json.loads(response.data)

    assert response_data["success"] == "User registered"  # nosec


def test_register_existing_email(client):
    """Test d'un enregistrement avec un email déjà existant"""
    user_data = {
        "email": "testusers@example.com",
        "password": "password123",
        "username": "testuser",
        "is_active": True,
    }
    response = client.post("/register", json=user_data)
    assert response.status_code == 201  # nosec

    response = client.post("/register", json=user_data)
    assert response.status_code == 409  # nosec
    assert b"Email already registered" in response.data  # nosec


def test_login_success(client):
    """Test de la connexion avec des identifiants valides"""
    user_data = {
        "email": "testusers@example.com",
        "password": "password123",
        "username": "testuser",
        "is_active": True,
    }
    client.post("/register", json=user_data)

    response = client.post(
        "/login", json={"email": user_data["email"], "password": user_data["password"]}
    )
    assert response.status_code == 200  # nosec
    assert b"Login successful" in response.data  # nosec


def test_login_user_not_found(client):
    """Test de la connexion avec un utilisateur qui n'existe pas"""
    response = client.post(
        "/login", json={"email": "nonexistent@example.com", "password": "password123"}
    )
    assert response.status_code == 404  # nosec
    assert b"Wrong Email or Password" in response.data  # nosec


def test_login_invalid_password(client):
    """Test de la connexion avec un mot de passe incorrect"""
    user_data = {
        "email": "testusers@example.com",
        "password": "password123",
        "username": "testuser",
    }
    client.post("/register", json=user_data)

    response = client.post(
        "/login", json={"email": user_data["email"], "password": "wrongpassword"}
    )
    assert response.status_code == 404  # nosec
    assert b"Wrong Email or Password" in response.data  # nosec


if __name__ == "__main__":
    pytest.main()
