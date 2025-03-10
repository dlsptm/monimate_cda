from app.extensions import db
from app.models.Ticket import Ticket


class TicketRepository:
    @staticmethod
    def create(subject, status, user_id):
        """
        Crée un nouveau ticket avec un sujet, un statut et un utilisateur.
        """
        new_ticket = Ticket(
            subject=subject,
            status=status,
            user_id=user_id
        )
        db.session.add(new_ticket)
        db.session.commit()
        return new_ticket

    @staticmethod
    def get_all():
        """
        Récupère tous les tickets.
        """
        return Ticket.query.all()

    @staticmethod
    def get_by_id(ticket_id):
        """
        Récupère un ticket spécifique par son ID.
        """
        return Ticket.query.get(ticket_id)

    @staticmethod
    def get_by_user(user_id):
        """
        Récupère tous les tickets d'un utilisateur spécifique.
        """
        return Ticket.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update(ticket_id, **kwargs):
        """
        Met à jour un ticket existant avec de nouveaux champs.
        """
        ticket = Ticket.query.get(ticket_id)
        if ticket:
            for key, value in kwargs.items():
                if hasattr(ticket, key):
                    setattr(ticket, key, value)
            db.session.commit()
        return ticket

    @staticmethod
    def delete(ticket_id):
        """
        Supprime un ticket par son ID.
        """
        ticket = Ticket.query.get(ticket_id)
        if ticket:
            db.session.delete(ticket)
            db.session.commit()
            return True
        return False
