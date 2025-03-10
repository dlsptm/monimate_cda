from app.extensions import db
from app.models.Participant import Participant


class ParticipantRepository:
    @staticmethod
    def create(user_id, account_id):
        """
        Crée un nouveau participant associé à un utilisateur et un compte.
        """
        new_participant = Participant(
            user_id=user_id,
            account_id=account_id
        )
        db.session.add(new_participant)
        db.session.commit()
        return new_participant

    @staticmethod
    def get_all():
        """
        Récupère tous les participants.
        """
        return Participant.query.all()

    @staticmethod
    def get_by_id(participant_id):
        """
        Récupère un participant par son ID.
        """
        return Participant.query.get(participant_id)

    @staticmethod
    def get_by_account_id(account_id):
        """
        Récupère tous les participants associés à un compte spécifique.
        """
        return Participant.query.filter_by(account_id=account_id).all()

    @staticmethod
    def get_by_user_id(user_id):
        """
        Récupère tous les participants associés à un utilisateur spécifique.
        """
        return Participant.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update(participant_id, **kwargs):
        """
        Met à jour un participant existant avec de nouveaux champs.
        """
        participant = Participant.query.get(participant_id)
        if participant:
            for key, value in kwargs.items():
                if hasattr(participant, key):
                    setattr(participant, key, value)
            db.session.commit()
        return participant

    @staticmethod
    def delete(participant_id):
        """
        Supprime un participant par son ID.
        """
        participant = Participant.query.get(participant_id)
        if participant:
            db.session.delete(participant)
            db.session.commit()
            return True
        return False
