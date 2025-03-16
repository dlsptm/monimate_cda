from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required, login_user, logout_user

from app.extensions import bcrypt
from app.repositories.UserRepository import UserRepository as user_repository

users = Blueprint("users", __name__)


@users.route("/admin/users")
@login_required
def index():
    if not current_user and current_user.is_admin:
        return jsonify({"error": "Access denied"}), 403

    all_users = user_repository.get_all()
    return jsonify({"users": [user.to_json() for user in all_users], "success": "User"})


@users.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No JSON received"}), 400

        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        is_active = data.get("is_active", False)

        if not email or not password or not username:
            return jsonify({"error": "Email, Username, and Password are required"}), 400

        existing_user = user_repository.get_by_email(email)
        if existing_user:
            return jsonify({"error": "Email already registered"}), 409

        password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
        user_repository.create(
            email=email, username=username, password=password_hash, is_active=is_active
        )

        return jsonify({"success": "User registered"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@users.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No JSON received"}), 400

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        user = user_repository.get_by_email(email)
        if user and bcrypt.check_password_hash(user.password, password):
            if user.is_active:
                now = datetime.now(ZoneInfo("Europe/Paris"))
                user_repository.update(user.id, last_active=now)
                login_user(user)
                return jsonify({"success": "Login successful"}), 200
            return jsonify({"error": "User not activated"}), 403

        return jsonify({"error": "Wrong Email or Password"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@users.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return jsonify({"success": "Logout successful"}), 200


@users.route("/user/<int:user_id>/delete", methods=["DELETE"])
def delete_user(user_id):
    try:
        user = user_repository.get_by_id(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        user_repository.delete(user_id)

        return jsonify({"success": "User deleted"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
