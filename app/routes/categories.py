from flask import Blueprint, request, jsonify, render_template, flash, redirect, url_for
from app.repositories.CategoryRepository import CategoryRepository as category_repository



categories = Blueprint('categories', __name__)

@categories.route('/category/<account>')
def index():
    all_users = category_repository.get_all()
    return render_template('index.html', users=all_users)
