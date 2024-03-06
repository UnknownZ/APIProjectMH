from models import db
from models.relations import game_monster

class Monster(db.Model):
    __tablename__ = "monsters"
    id = db.Column(db.Integer, primary_key = True)
    id_generation = db.Column(db.Integer, db.ForeignKey("generations.id"), nullable=False)
    name = db.Column(db.String(120), nullable = False, unique=True)
    flagship = db.Column(db.Boolean, nullable = False)
    id_species = db.Column(db.Integer, db.ForeignKey('species.id'), nullable = False)
    species = db.relationship("Species", backref = "species")
    generation = db.relationship("Generation", backref="generations")

def serialize(self):
    return {
        "id": self.id,
        "name" : self.name,
        "is flagship": self.flagship,
        "species" : self.species,
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