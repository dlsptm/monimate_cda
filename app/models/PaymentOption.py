from app.extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
from ..enums.PaymentFrequencyEnum import PaymentFrequencyEnum
from datetime import date

class PaymentOption(db.Model):
    __tablename__ = 'payment_option'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    installment = db.Column(db.Integer, nullable=True)
    frequency = db.Column(db.Enum(PaymentFrequencyEnum), nullable=True)
    due_date = db.Column(db.Date, nullable=True, default=date.today)

    def to_json(self):
        return {
            'id': str(self.id),
            'installment': self.installment,
            'frequency': self.frequency,
            'due_date':self.due_date
        }

    def __repr__(self):
        return f"<PaymentOption(id={self.id or 'N/A'}, installment={self.installment or 'N/A'}, frequency={self.frequency or 'N/A'}, due_date={self.due_date or 'N/A'})>"
