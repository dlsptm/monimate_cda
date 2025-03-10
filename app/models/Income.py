from back.app.extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import BigInteger
from datetime import datetime, timezone


amount = db.Column(BigInteger, nullable=False)


class Income(db.Model):
    __tablename__ = 'income'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    title = db.Column(db.String(90), unique=False, nullable=False)
    amount = db.Column(BigInteger, nullable=False)
    user_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, unique=False, nullable=False, default=datetime.now(timezone.utc))


    def to_json(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'amount':self.amount,
            'user_id':self.user_id,
            'created_at':self.created_at,
        }

    def __repr__(self):
        return f"<Income(id={self.id or 'N/A'}, title='{self.title}', amount={self.amount}, user_id={self.user_id or 'N/A'}, created_at={self.created_at or 'N/A'})>"
