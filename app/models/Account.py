import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy.dialects.postgresql import UUID

from app.extensions import db

if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model
else:
    Model = db.Model


class Account(Model):
    __tablename__ = "account"
    id = db.Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    title = db.Column(db.String(150), unique=False, nullable=False)
    owner_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
    )
    user = db.relationship("User", backref="accounts", passive_deletes=True)

    created_at = db.Column(
        db.TIMESTAMP, unique=False, nullable=False, default=datetime.now(timezone.utc)
    )

    def to_json(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "owner_id": str(self.owner_id),  # Convertir en chaîne
            "created_at": self.created_at.isoformat(),  # Formater en ISO
        }

    def __repr__(self):
        return (
            f"<Account(id={self.id}, "
            f"title='{self.title}', "
            f"owner_id={self.owner_id}, "
            f"created_at={self.created_at})>"
        )
