from app.extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone
from ..enums.TicketStatusEnum import TicketStatusEnum


class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    subject = db.Column(db.String(90), unique=False, nullable=False)
    status = db.Column(db.Enum(TicketStatusEnum), nullable=False)
    user_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, unique=False, nullable=False, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.TIMESTAMP, unique=False, nullable=False, default=datetime.now(timezone.utc))


    def to_json(self):
        return {
            'id': str(self.id),
            'subject': self.subject,
            'status':self.status,
            'user_id':self.user_id,
            'created_at':self.created_at,
            'updated_at':self.updated_at,
        }

    def __repr__(self):
        return f"<Ticket(id={self.id or 'N/A'}, subject='{self.subject}', status={self.status or 'N/A'}, user_id={self.user_id or 'N/A'}, created_at={self.created_at or 'N/A'}, updated_at={self.updated_at or 'N/A'})>"
