import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID

from app import db

if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model
else:
    Model = db.Model


class User(Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(90), unique=False, nullable=False)
    password = db.Column(db.Text, unique=False, nullable=False)
    is_active = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    role = db.Column(db.JSON, unique=False, nullable=False, default=["ROLE_USER"])
    created_at = db.Column(
        db.TIMESTAMP, unique=False, nullable=False, default=datetime.now(timezone.utc)
    )
    last_active = db.Column(db.DateTime, nullable=True, default=None)

    def to_json(self):
        return {
            "id": str(self.id),
            "email": self.email,
            "username": self.username,
            "is_active": self.is_active,
            "role": self.role,
            "created_at": self.created_at,
            "last_active": self.last_active,
        }

    def __repr__(self):
        return (
            f"<User(id={self.id}, "
            f"email={self.email}, "
            f"username={self.username}, "
            f"active={self.is_active}, "
            f"role={self.role})>"
        )

    def get_id(self):
        return self.id
