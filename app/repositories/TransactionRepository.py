from app.extensions import db
from app.models.Transaction import Transaction


class TransactionRepository:
    @staticmethod
    def create(
        title,
        location,
        amount,
        category_id,
        invoice,
        payment_option_id,
        is_monthly,
        user_id,
        account_id,
    ):
        """
        Crée une nouvelle transaction avec les informations données.
        """
        new_transaction = Transaction(
            title=title,
            location=location,
            amount=amount,
            category_id=category_id,
            invoice=invoice,
            payment_option_id=payment_option_id,
            is_monthly=is_monthly,
            user_id=user_id,
            account_id=account_id,
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
