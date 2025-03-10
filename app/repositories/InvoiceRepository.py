from app.extensions import db
from app.models.Invoice import Invoice

class InvoiceRepository:
    @staticmethod
    def create(title, link, transaction_id):
        """
        Crée une nouvelle facture.
        """
        invoice = Invoice(
            title=title,
            link=link,
            transaction_id=transaction_id
        )
        db.session.add(invoice)
        db.session.commit()
        return invoice

    @staticmethod
    def get_all():
        """
        Récupère toutes les factures.
        """
        return Invoice.query.all()

    @staticmethod
    def get_by_id(invoice_id):
        """
        Récupère une facture par son ID.
        """
        return Invoice.query.get(invoice_id)

    @staticmethod
    def get_by_transaction_id(transaction_id):
        """
        Récupère toutes les factures d'une transaction spécifique.
        """
        return Invoice.query.filter_by(transaction_id=transaction_id).all()

    @staticmethod
    def update(invoice_id, **kwargs):
        """
        Met à jour une facture existante avec de nouveaux champs.
        """
        invoice = Invoice.query.get(invoice_id)
        if invoice:
            for key, value in kwargs.items():
                if hasattr(invoice, key):
                    setattr(invoice, key, value)
            db.session.commit()
        return invoice

    @staticmethod
    def delete(invoice_id):
        """
        Supprime une facture par son ID.
        """
        invoice = Invoice.query.get(invoice_id)
        if invoice:
            db.session.delete(invoice)
            db.session.commit()
            return True
        return False
