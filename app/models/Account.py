from app.extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone


class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    title = db.Column(db.String(150), unique=False, nullable=False)
    owner_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, unique=False, nullable=False, default=datetime.now(timezone.utc))

    def to_json(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'owner_id': self.owner_id,
            'created_at': self.created_at,
        }

    def __repr__(self):
        return f"<Account(id={self.id}, title='{self.title}', owner_id={self.owner_id}, created_at={self.created_at})>"