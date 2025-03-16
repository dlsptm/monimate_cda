import uuid
from datetime import date, datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger
from sqlalchemy.dialects.postgresql import UUID

from app.extensions import db

from ..enums.GoalStatusEnum import GoalStatusEnum

if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model
else:
    Model = db.Model


class Goal(Model):
    __tablename__ = "goal"
    id = db.Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    title = db.Column(db.String(90), unique=False, nullable=False)
    amount = db.Column(BigInteger, nullable=False)
    deadline = db.Column(db.Date, nullable=True, default=date.today)
    status = db.Column(db.Enum(GoalStatusEnum), nullable=False)
    user_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(
        db.TIMESTAMP, unique=False, nullable=False, default=datetime.now(timezone.utc)
    )

    def to_json(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "amount": self.amount,
            "deadline": self.deadline,
            "status": self.status,
            "user_id": self.user_id,
            "created_at": self.created_at,
        }

    def __repr__(self):
        return (
            f"<Goal(id={self.id or 'N/A'}, "
            f"title='{self.title}', "
            f"amount={self.amount}, "
            f"deadline={self.deadline or 'N/A'}, "
            f"status={self.status.name if self.status else 'N/A'}, "
            f"user_id={self.user_id or 'N/A'}, created_at={self.created_at or 'N/A'})>"
        )
