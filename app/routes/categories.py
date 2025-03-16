from flask import Blueprint, render_template

from app.repositories.CategoryRepository import \
    CategoryRepository as category_repository

categories = Blueprint("categories", __name__)


@categories.route("/category/<account>")
def index():
    all_users = category_repository.get_all()
    return render_template("index.html", users=all_users)
