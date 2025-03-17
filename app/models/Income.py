import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger
from sqlalchemy.dialects.postgresql import UUID

from app.extensions import db

amount = db.Column(BigInteger, nullable=False)

if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model
else:
    Model = db.Model

class Income(Model):
    __tablename__ = "income"
    id = db.Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    title = db.Column(db.String(90), unique=False, nullable=False)
    amount = db.Column(BigInteger, nullable=False)
    user_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(
        db.TIMESTAMP, unique=False, nullable=False, default=datetime.now(timezone.utc)
    )

    def to_json(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "amount": self.amount,
            "user_id": self.user_id,
            "created_at": self.created_at,
        }

    def __repr__(self):
        return f"<Income(id={self.id or 'N/A'}, title='{self.title}', amount={self.amount}, user_id={self.user_id or 'N/A'}, created_at={self.created_at or 'N/A'})>"
