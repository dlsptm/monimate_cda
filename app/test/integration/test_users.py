import os

import pytest
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate

from app.extensions import bcrypt, db
from app.routes.users import users


def create_test_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        static_url_path="/",
    )
    app.secret_key = os.getenv("SECRET_KEY")

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL_TEST")
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
    # Nettoyage de la base de données après chaque test
    with app.app_context():
        db.drop_all()  # Supprime toutes les tables après chaque test
        db.create_all()  # Crée les tables (optionnel mais généralement utilisé)


# Fixture pour créer un client de test


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
    assert response.status_code == 201
    assert b"User registered" in response.data


def test_register_existing_email(client):
    """Test d'un enregistrement avec un email déjà existant"""
    user_data = {
        "email": "testusers@example.com",
        "password": "password123",
        "username": "testuser",
    }
    client.post("/register", json=user_data)

    response = client.post("/register", json=user_data)
    assert response.status_code == 409  # Conflit : email déjà enregistré
    assert b"Email already registered" in response.data


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
    assert response.status_code == 200
    assert b"Login successful" in response.data


def test_login_user_not_found(client):
    """Test de la connexion avec un utilisateur qui n'existe pas"""
    response = client.post(
        "/login", json={"email": "nonexistent@example.com", "password": "password123"}
    )
    assert response.status_code == 404
    assert b"Wrong Email or Password" in response.data


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
    assert response.status_code == 404
    assert b"Wrong Email or Password" in response.data


if __name__ == "__main__":
    pytest.main()
