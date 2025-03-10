from app.extensions import db
from app.models.Income import Income
from datetime import datetime, timezone


class IncomeRepository:
    @staticmethod
    def create(title, amount, user_id):
        """
        Crée un nouvel enregistrement de revenu.
        """
        income = Income(
            title=title,
            amount=amount,
            user_id=user_id,
            created_at=datetime.now(timezone.utc)
        )
        db.session.add(income)
        db.session.commit()
        return income

    @staticmethod
    def get_all():
        """
        Récupère tous les revenus.
        """
        return Income.query.all()

    @staticmethod
    def get_by_id(income_id):
        """
        Récupère un revenu par son ID.
        """
        return Income.query.get(income_id)

    @staticmethod
    def get_by_user_id(user_id):
        """
        Récupère tous les revenus d'un utilisateur.
        """
        return Income.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update(income_id, **kwargs):
        """
        Met à jour un revenu existant avec de nouveaux champs.
        """
        income = Income.query.get(income_id)
        if income:
            for key, value in kwargs.items():
                if hasattr(income, key):
                    setattr(income, key, value)
            db.session.commit()
        return income

    @staticmethod
    def delete(income_id):
        """
        Supprime un revenu par son ID.
        """
        income = Income.query.get(income_id)
        if income:
            db.session.delete(income)
            db.session.commit()
            return True
        return False
