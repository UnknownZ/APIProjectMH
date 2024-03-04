from flask import Blueprint, jsonify, request
from models.generation import Generation

api = Blueprint('generation_api', __name__)

@api.route("/generation", methods=['GET'])
def list_games():

    generations = Generation.query.all()
    generations = list(map(lambda generation: generation.serialize(), generations))

    return jsonify(generations), 200