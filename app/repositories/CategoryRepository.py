from app.extensions import db
from app.models.Category import Category


class CategoryRepository:
    @staticmethod
    def create(title, icon, amount, account_id):
        """
        Crée une nouvelle catégorie.
        """
        category = Category(
            title=title, icon=icon, amount=amount, account_id=account_id
        )
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def get_all():
        """
        Récupère toutes les catégories.
        """
        return Category.query.all()

    @staticmethod
    def get_by_id(category_id):
        """
        Récupère une catégorie par son ID.
        """
        return Category.query.get(category_id)

    @staticmethod
    def get_by_account(account_id):
        """
        Récupère toutes les catégories associées à un compte donné.
        """
        return Category.query.filter_by(account_id=account_id).all()

    @staticmethod
    def update(category_id, **kwargs):
        """
        Met à jour une catégorie existante.
        """
        category = Category.query.get(category_id)
        if category:
            for key, value in kwargs.items():
                if hasattr(category, key):
                    setattr(category, key, value)
            db.session.commit()
        return category

    @staticmethod
    def delete(category_id):
        """
        Supprime une catégorie par son ID.
        """
        category = Category.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            return True
        return False
