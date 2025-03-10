from app.extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    message = db.Column(db.Text, unique=False, nullable=False)
    ticket_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('ticket.id'), nullable=False)
    sender_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, unique=False, nullable=False, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.TIMESTAMP, unique=False, nullable=False, default=datetime.now(timezone.utc))


    def to_json(self):
        return {
            'id': str(self.id),
            'message': self.message,
            'ticket_id':self.ticket_id,
            'sender_id':self.sender_id,
            'created_at':self.created_at,
            'updated_at':self.updated_at,
        }

    def __repr__(self):
        return f"<Message(id={self.id or 'N/A'}, message='{self.message[:20]}...', ticket_id={self.ticket_id or 'N/A'}, sender_id={self.sender_id or 'N/A'}, created_at={self.created_at or 'N/A'}, updated_at={self.updated_at or 'N/A'})>"
