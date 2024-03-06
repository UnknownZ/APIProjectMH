from models import db

#juego - monstruo
game_monster = db.table("game_monster"),
db.Column("game_id", db.Integer, db.ForeignKey('game_id', ondelete="CASCADE"), primary_key=True),
db.Column("monster_id", db.Integer, db.ForeignKey('monster_id', ondelete="CASCADE"), primary_key=True)

#juego - plataforma
game_platform = db.table("game_platform"),
db.Column("game_id", db.Integer, db.ForeignKey('game_id', ondelete="CASCADE"), primary_key=True),
db.Column("platform_id", db.Integer, db.ForeignKey('platform_id', ondelete="CASCADE"), primary_key=True)

#juego - locacion
game_location = db.table("game_location"),
db.Column("game_id", db.Integer, db.ForeignKey('game_id', ondelete="CASCADE"), primary_key=True),
db.Column("location_id", db.Integer, db.ForeignKey('location_id', ondelete="CASCADE"), primary_key=True)

#locacion - monstruo
location_monster = db.table("location_monster"),
db.Column('monster_id', db.Integer, db.ForeignKey('monster_id', ondelete='CASCADE'), primary_key=True),
db.Column('location_id', db.Integer, db.ForeignKey('location_id', ondelete='CASCADE'), primary_key=True),