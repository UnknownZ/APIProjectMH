from models import db

class Location(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key = True)
    id_generation = db.Column(db.Integer, db.ForeignKey("generations.id"), nullable=False)
    name = db.Column(db.String(120), nullable = False, unique=True)
    generation = db.relationship("Generation", backref="generation")

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