from app.extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Invoice(db.Model):
    __tablename__ = 'invoice'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    title = db.Column(db.String(90), unique=False, nullable=False)
    link = db.Column(db.String(140), unique=False, nullable=False)
    transaction_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('transaction.id'), nullable=False)

    def to_json(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'link': self.link,
            'transaction_id':self.transaction_id
        }

    def __repr__(self):
        return f"<Invoice(id={self.id or 'N/A'}, title='{self.title}', link='{self.link}', transaction_id={self.transaction_id or 'N/A'})>"
