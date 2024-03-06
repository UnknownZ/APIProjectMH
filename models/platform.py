from models import db
from datetime import datetime

class Platform(db.Model):
    __tablename__ = "platforms"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False, unique=True)
    launch_date = db.Column(db.DateTime(), default=datetime.now)
    code = db.Column(db.String(3), nullable = False, unique=True)

def serialize(self):
    return {
        "id": self.id,
        "name" : self.name,
        "code": self.code,
    }

def save(self):
    db.session.add(self)
    db.session.commit()

def update(self):
    db.session.commit()

def delete(self):
    db.session.delete(self)
    db.session.commit()