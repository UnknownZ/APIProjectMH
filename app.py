import os
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from models import db

from models.game import Game
from models.generation import Generation
from models.location import Location
from models.monster import Monster
from models.platform import Platform
from models.species import Species

from dotenv import load_dotenv
from rutas import api

from routes.monster_api import api as api_monster
from routes.location_api import api as api_location
from routes.generation_api import api as api_generation
from routes.game_api import api as api_game
from routes.platform_api import api as api_platform
from routes.species_api import api as api_species

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

db.init_app(app)
Migrate(app, db)
CORS(app)

app.register_blueprint(api_game, url_prefix='/api')
app.register_blueprint(api_monster, url_prefix='/api')
app.register_blueprint(api_location, url_prefix='/api')
app.register_blueprint(api_generation, url_prefix='/api')
app.register_blueprint(api_platform, url_prefix='/api')
app.register_blueprint(api_species, url_prefix='/api')


@app.route("/")
def hello_world():
    return "<p>Welcome to the Monster Hunter API</p>"