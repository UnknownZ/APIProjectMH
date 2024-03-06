from models import db

#juego - monstruo
game_monster = db.Table("game_monster",
db.Column("id_game", db.Integer, db.ForeignKey('games.id', ondelete="CASCADE"), primary_key=True),
db.Column("id_monster", db.Integer, db.ForeignKey('monsters.id', ondelete="CASCADE"), primary_key=True)
)
#juego - plataforma
game_platform = db.Table("game_platform",
db.Column("id_game", db.Integer, db.ForeignKey('games.id', ondelete="CASCADE"), primary_key=True),
db.Column("id_platform", db.Integer, db.ForeignKey('platforms.id', ondelete="CASCADE"), primary_key=True)
)
#juego - locacion
game_location = db.Table("game_location",
db.Column("id_game", db.Integer, db.ForeignKey('games.id', ondelete="CASCADE"), primary_key=True),
db.Column("id_location", db.Integer, db.ForeignKey('locations.id', ondelete="CASCADE"), primary_key=True)
)
#locacion - monstruo
location_monster = db.Table("location_monster",
db.Column('id_monster', db.Integer, db.ForeignKey('monsters.id', ondelete='CASCADE'), primary_key=True),
db.Column('id_location', db.Integer, db.ForeignKey('locations.id', ondelete='CASCADE'), primary_key=True)
)