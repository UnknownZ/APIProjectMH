from flask import Blueprint, jsonify, request
from models.game import Game

api = Blueprint('game_api', __name__)

@api.route("/game", methods=['GET'])
def list_games():

    games = Game.query.all()
    games = list(map(lambda game: game.serialize(), games))

    return jsonify(games), 200

