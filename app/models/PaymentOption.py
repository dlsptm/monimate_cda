import uuid
from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy.dialects.postgresql import UUID

from app.extensions import db

from ..enums.payment_frequency_enum import PaymentFrequencyEnum

if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model
else:
    Model = db.Model


class PaymentOption(Model):
    __tablename__ = "payment_option"
    id = db.Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    installment = db.Column(db.Integer, nullable=True)
    frequency = db.Column(db.Enum(PaymentFrequencyEnum), nullable=True)
    due_date = db.Column(db.Date, nullable=True, default=date.today)

    def to_json(self):
        return {
            "id": str(self.id),
            "installment": self.installment,
            "frequency": self.frequency,
            "due_date": self.due_date,
        }

    def __repr__(self):
        return (
            f"<PaymentOption(id={self.id or 'N/A'}, "
            f"installment={self.installment or 'N/A'}, "
            f"frequency={self.frequency or 'N/A'}, "
            f"due_date={self.due_date or 'N/A'})>"
        )
