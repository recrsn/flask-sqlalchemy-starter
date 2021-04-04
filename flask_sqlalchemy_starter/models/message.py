from sqlalchemy import func

from ..db import db


class Message(db.Model):
    id = db.Column(db.String(48), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(), nullable=False)

    created_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def get(message_id):
        return Message.query.get(message_id)
