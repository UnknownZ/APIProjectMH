from flask import Blueprint, jsonify, request
from models.monster import Monster

api = Blueprint('monster_api', __name__)

@api.route("/monster", methods=['GET'])
def list_games():

    monsters = Monster.query.all()
    monsters = list(map(lambda monster: monster.serialize(), monsters))

    return jsonify(monsters), 200