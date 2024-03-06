from models import db

class Generation(db.Model):
    __tablename__ = "generations"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False, unique=True)

def serialize(self):
    return {
        "id": self.id,
        "name" : self.name,
    }

def save(self):
    db.session.add(self)
    db.session.commit()

def update(self):
    db.session.commit()

def delete(self):
    db.session.delete(self)
    db.session.commit()