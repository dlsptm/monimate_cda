from app.extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone


class UserPreference(db.Model):
    __tablename__ = 'user_preference'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    type = db.Column(db.String(100), unique=False, nullable=False)
    preference = db.Column(db.JSON, unique=False, nullable=False)
    user_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    account_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('account.id'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, unique=False, nullable=False, default=datetime.now(timezone.utc))

    def to_json(self):
        return {
            'id': self.id,
            'type': self.type,
            'preference': self.preference,
            'user_id': self.user_id,
            'account_id': self.account_id,
            'created_at': self.created_at
        }

    def __repr__(self):
        return f"<UserPreference(id={self.id}, type='{self.type}', preference={self.preference}, user_id={self.user_id}, account_id={self.account_id}, created_at={self.created_at})>"
