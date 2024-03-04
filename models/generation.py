from models import db

class Generation(db.Model):
    __tablename__ = "generations"
    id = db.Column(db.Integer, primary_key = True)
    identifier = db.Column(db.String(50), nullable = False, unique=True)

def serialize(self):
    return {
        "id": self.id,
        "identifier" : self.identifier,
    }

def save(self):
    db.session.add(self)
    db.session.commit()

def update(self):
    db.session.commit()

def delete(self):
    db.session.delete(self)
    db.session.commit()