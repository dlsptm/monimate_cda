from app.extensions import db
from app.models.Transaction import Transaction


class TransactionRepository:
    @staticmethod
    def create(transaction_data):
        """
        Crée une nouvelle transaction avec les informations données.
        """
        new_transaction = Transaction(
            title=transaction_data.get("title"),
            location=transaction_data.get("location"),
            amount=transaction_data.get("amount"),
            category_id=transaction_data.get("category_id"),
            invoice=transaction_data.get("invoice"),
            payment_option_id=transaction_data.get("payment_option_id"),
            is_monthly=transaction_data.get("is_monthly"),
            user_id=transaction_data.get("user_id"),
            account_id=transaction_data.get("account_id"),
        )
        db.session.add(new_transaction)
        db.session.commit()
        return new_transaction

    @staticmethod
    def get_all():
        """
        Récupère toutes les transactions.
        """
        return Transaction.query.all()

    @staticmethod
    def get_by_id(transaction_id):
        """
        Récupère une transaction spécifique par son ID.
        """
        return Transaction.query.get(transaction_id)

    @staticmethod
    def get_by_user(user_id):
        """
        Récupère toutes les transactions d'un utilisateur spécifique.
        """
        return Transaction.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update(transaction_id, **kwargs):
        """
        Met à jour une transaction existante avec de nouveaux champs.
        """
        transaction = Transaction.query.get(transaction_id)
        if transaction:
            for key, value in kwargs.items():
                if hasattr(transaction, key):
                    setattr(transaction, key, value)
            db.session.commit()
        return transaction

    @staticmethod
    def delete(transaction_id):
        """
        Supprime une transaction par son ID.
        """
        transaction = Transaction.query.get(transaction_id)
        if transaction:
            db.session.delete(transaction)
            db.session.commit()
            return True
        return False
