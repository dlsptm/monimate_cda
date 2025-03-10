from app.extensions import db
from app.models.User import User
from app.models.Account import Account
import uuid

class UserRepository:

    def __init__(self, bcrypt_instance):
        self.bcrypt = bcrypt_instance

    @staticmethod
    def create(email, username, password, role=None, last_active=None, is_active=False,):
        """
             Crée un nouvel utilisateur avec les informations données.
        """
        try:
            if role is None:
                role = ["ROLE_USER"]

            new_user = User(
                id=str(uuid.uuid4()),
                email=email,
                username=username,
                password=password,
                is_active=is_active,
                role=role,
                last_active=last_active
            )

            default_account = Account()
            default_account.title = "Compte " + username
            default_account.owner_id = new_user.get_id()

            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as e:
            db.session.rollback()
            print(f"Erreur lors de la création de l'utilisateur : {e}")
            return None


    @staticmethod
    def get_all():
        """
        Récupère tous les utilisateurs.
        """
        return User.query.all()


    @staticmethod
    def get_by_id(user_id):
        """
        Récupère un utilisateur spécifique par son ID.
        """
        return User.query.get(user_id)


    @staticmethod
    def get_by_email(email):
        """
        Récupère un utilisateur spécifique par son email.
        """
        return User.query.filter_by(email=email).first()


    @staticmethod
    def update(user_id, **kwargs):
        """
        Met à jour un utilisateur existant avec de nouveaux champs.
        """
        user = User.query.get(user_id)
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            db.session.commit()
        return user


    @staticmethod
    def delete(user_id):
        """
        Supprime un utilisateur par son ID.
        """
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False