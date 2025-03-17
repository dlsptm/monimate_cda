from app.extensions import db
from app.models.UserPreference import UserPreference


class UserPreferenceRepository:
    @staticmethod
    def create(user_type, preference, user_id, account_id):
        """
        Crée une nouvelle préférence utilisateur.
        """
        new_preference = UserPreference(
            type=user_type, preference=preference, user_id=user_id, account_id=account_id
        )
        db.session.add(new_preference)
        db.session.commit()
        return new_preference

    @staticmethod
    def get_all():
        """
        Récupère toutes les préférences utilisateur.
        """
        return UserPreference.query.all()

    @staticmethod
    def get_by_id(preference_id):
        """
        Récupère une préférence utilisateur par son ID.
        """
        return UserPreference.query.get(preference_id)

    @staticmethod
    def get_by_user_and_account(user_id, account_id):
        """
        Récupère une préférence utilisateur en fonction de l'ID utilisateur et de l'ID du compte.
        """
        return UserPreference.query.filter_by(
            user_id=user_id, account_id=account_id
        ).all()

    @staticmethod
    def update(preference_id, **kwargs):
        """
        Met à jour une préférence utilisateur existante.
        """
        preference = UserPreference.query.get(preference_id)
        if preference:
            for key, value in kwargs.items():
                if hasattr(preference, key):
                    setattr(preference, key, value)
            db.session.commit()
        return preference

    @staticmethod
    def delete(preference_id):
        """
        Supprime une préférence utilisateur par son ID.
        """
        preference = UserPreference.query.get(preference_id)
        if preference:
            db.session.delete(preference)
            db.session.commit()
            return True
        return False
