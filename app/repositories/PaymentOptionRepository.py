from app.extensions import db
from app.models.PaymentOption import PaymentOption


class PaymentOptionRepository:
    @staticmethod
    def create(installment, frequency, due_date=None):
        """
        Crée une nouvelle option de paiement avec un montant d'installment, une fréquence et une date d'échéance.
        """
        new_payment_option = PaymentOption(
            installment=installment,
            frequency=frequency,
            due_date=due_date
        )
        db.session.add(new_payment_option)
        db.session.commit()
        return new_payment_option

    @staticmethod
    def get_all():
        """
        Récupère toutes les options de paiement.
        """
        return PaymentOption.query.all()

    @staticmethod
    def get_by_id(payment_option_id):
        """
        Récupère une option de paiement par son ID.
        """
        return PaymentOption.query.get(payment_option_id)

    @staticmethod
    def get_by_frequency(frequency):
        """
        Récupère toutes les options de paiement avec une fréquence spécifique.
        """
        return PaymentOption.query.filter_by(frequency=frequency).all()

    @staticmethod
    def update(payment_option_id, **kwargs):
        """
        Met à jour une option de paiement existante avec de nouveaux champs.
        """
        payment_option = PaymentOption.query.get(payment_option_id)
        if payment_option:
            for key, value in kwargs.items():
                if hasattr(payment_option, key):
                    setattr(payment_option, key, value)
            db.session.commit()
        return payment_option

    @staticmethod
    def delete(payment_option_id):
        """
        Supprime une option de paiement par son ID.
        """
        payment_option = PaymentOption.query.get(payment_option_id)
        if payment_option:
            db.session.delete(payment_option)
            db.session.commit()
            return True
        return False
