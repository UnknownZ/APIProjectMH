from models import db
from models.relations import game_monster, game_location, game_platform
from datetime import datetime

class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False, unique=True)
    launch_date = db.Column(db.DateTime(), default=datetime.now)
    generation = db.relationship("Generation", backref="generations")

def serialize(self):
    return {
        "id": self.id,
        "name" : self.name,
        "launch date": self.launch_date,
        "generation" : self.generation,
    }

def save(self):
    db.session.add(self)
    db.session.commit()

def update(self):
    db.session.commit()

def delete(self):
    db.session.delete(self)
    db.session.commit()