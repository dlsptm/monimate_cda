from app.extensions import db
from app.models.Account import Account


class AccountRepository:
    @staticmethod
    def create(title, owner_id):
        """
        Crée une nouvelle entrée Account dans la base de données.
        """
        account = Account(title=title, owner_id=owner_id)
        db.session.add(account)
        db.session.commit()
        return account

    @staticmethod
    def get_all():
        """
        Récupère tous les comptes.
        """
        return Account.query.all()

    @staticmethod
    def get_by_id(account_id):
        """
        Récupère un compte par son ID.
        """
        return Account.query.get(account_id)

    @staticmethod
    def update(account_id, **kwargs):
        """
        Met à jour un compte existant avec des champs fournis.
        """
        account = Account.query.get(account_id)
        if account:
            for key, value in kwargs.items():
                if hasattr(account, key):
                    setattr(account, key, value)
            db.session.commit()
        return account

    @staticmethod
    def delete(account_id):
        """
        Supprime un compte par son ID.
        """
        account = Account.query.get(account_id)
        if account:
            db.session.delete(account)
            db.session.commit()
            return True
        return False
