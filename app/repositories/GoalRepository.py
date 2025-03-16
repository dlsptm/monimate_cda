from datetime import date

from app.enums.GoalStatusEnum import GoalStatusEnum
from app.extensions import db
from app.models.Goal import Goal


class GoalRepository:
    @staticmethod
    def create(title, amount, deadline, status, user_id):
        """
        Crée un nouvel objectif.
        """
        goal = Goal(
            title=title,
            amount=amount,
            deadline=deadline if deadline else date.today(),
            status=status,
            user_id=user_id,
        )
        db.session.add(goal)
        db.session.commit()
        return goal

    @staticmethod
    def get_all():
        """
        Récupère tous les objectifs.
        """
        return Goal.query.all()

    @staticmethod
    def get_by_id(goal_id):
        """
        Récupère un objectif par son ID.
        """
        return Goal.query.get(goal_id)

    @staticmethod
    def get_by_user_id(user_id):
        """
        Récupère tous les objectifs liés à un utilisateur.
        """
        return Goal.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update(goal_id, **kwargs):
        """
        Met à jour les champs spécifiés d'un objectif existant.
        """
        goal = Goal.query.get(goal_id)
        if goal:
            for key, value in kwargs.items():
                if hasattr(goal, key):
                    setattr(goal, key, value)
            db.session.commit()
        return goal

    @staticmethod
    def update_status(goal_id, new_status: GoalStatusEnum):
        """
        Met à jour le statut d'un objectif.
        """
        goal = Goal.query.get(goal_id)
        if goal:
            goal.status = new_status
            db.session.commit()
        return goal

    @staticmethod
    def delete(goal_id):
        """
        Supprime un objectif par son ID.
        """
        goal = Goal.query.get(goal_id)
        if goal:
            db.session.delete(goal)
            db.session.commit()
            return True
        return False
