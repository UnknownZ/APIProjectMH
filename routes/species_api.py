from flask import Blueprint, jsonify, request
from models.species import Species

api = Blueprint('species_api', __name__)

@api.route("/species", methods=['GET'])
def list_games():

    species_list = Species.query.all()
    species_list = list(map(lambda species: species.serialize(), species_list))

    return jsonify(species_list), 200