from datetime import datetime

from app import db


class BaseModel(object):
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, onupdate=datetime.utcnow)
