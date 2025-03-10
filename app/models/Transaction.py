from app.extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone


class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    title = db.Column(db.String(100), unique=False, nullable=False)
    location = db.Column(db.String(100), unique=False, nullable=False)
    amount = db.Column(db.Double, unique=False, nullable=False)
    category_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('category.id'), nullable=False)
    invoice = db.Column(db.String(160), unique=False, nullable=False)
    payment_option_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('payment_option.id'), nullable=False)
    is_monthly = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    user_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    account_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('account.id'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, unique=False, nullable=False, default=datetime.now(timezone.utc))

    def to_json(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'location' : self.location,
            'amount' : self.amount,
            'category_id' : self.category_id,
            'invoice' :self.invoice,
            'payment_option_id' : self.payment_option,
            'is_monthly' : self.is_monthly,
            'user_id' : self.user_id,
            'account_id' : self.account_id,
            'created_at' : self.created_at
        }

    def __repr__(self):
        return f"<Transaction(id={self.id or 'N/A'}, title='{self.title}', location='{self.location}', amount={self.amount}, category_id={self.category_id}, invoice='{self.invoice}', payment_option_id={self.payment_option_id}, is_monthly={self.is_monthly}, user_id={self.user_id}, account_id={self.account_id}, created_at={self.created_at})>"
