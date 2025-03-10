from app.extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import BigInteger

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    title = db.Column(db.String(90), unique=False, nullable=False)
    icon = db.Column(db.String(90), unique=False, nullable=False)
    amount = db.Column(BigInteger, nullable=False)
    account_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('account.id'), nullable=False)

    def to_json(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'icon': self.icon,
            'amount':self.amount,
            'account_id':self.account_id,
        }

    def __repr__(self):
        return f"<Category(id={self.id}, title='{self.title}', icon='{self.icon}', amount={self.amount}, account_id={self.account_id})>"
