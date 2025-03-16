from app.extensions import db
from app.models.Message import Message


class MessageRepository:
    @staticmethod
    def create(message, ticket_id, sender_id):
        """
        Crée un nouveau message.
        """
        new_message = Message(message=message, ticket_id=ticket_id, sender_id=sender_id)
        db.session.add(new_message)
        db.session.commit()
        return new_message

    @staticmethod
    def get_all():
        """
        Récupère tous les messages.
        """
        return Message.query.all()

    @staticmethod
    def get_by_id(message_id):
        """
        Récupère un message par son ID.
        """
        return Message.query.get(message_id)

    @staticmethod
    def get_by_ticket_id(ticket_id):
        """
        Récupère tous les messages associés à un ticket.
        """
        return Message.query.filter_by(ticket_id=ticket_id).all()

    @staticmethod
    def get_by_sender_id(sender_id):
        """
        Récupère tous les messages envoyés par un utilisateur spécifique.
        """
        return Message.query.filter_by(sender_id=sender_id).all()

    @staticmethod
    def update(message_id, **kwargs):
        """
        Met à jour un message existant avec de nouveaux champs.
        """
        message = Message.query.get(message_id)
        if message:
            for key, value in kwargs.items():
                if hasattr(message, key):
                    setattr(message, key, value)
            db.session.commit()
        return message

    @staticmethod
    def delete(message_id):
        """
        Supprime un message par son ID.
        """
        message = Message.query.get(message_id)
        if message:
            db.session.delete(message)
            db.session.commit()
            return True
        return False
