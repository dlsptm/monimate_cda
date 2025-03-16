import uuid
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger
from sqlalchemy.dialects.postgresql import UUID

from app.extensions import db

if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model
else:
    Model = db.Model


class Category(Model):
    __tablename__ = "category"
    id = db.Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    title = db.Column(db.String(90), unique=False, nullable=False)
    icon = db.Column(db.String(90), unique=False, nullable=False)
    amount = db.Column(BigInteger, nullable=False)
    account_id = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("account.id"), nullable=False
    )

    def to_json(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "icon": self.icon,
            "amount": self.amount,
            "account_id": self.account_id,
        }

    def __repr__(self):
        return (
            f"<Category(id={self.id}, "
            f"title='{self.title}', "
            f"icon='{self.icon}', "
            f"amount={self.amount}, "
            f"account_id={self.account_id})>"
        )
