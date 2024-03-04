from flask import Blueprint, jsonify, request
from models.location import Location

api = Blueprint('location_api', __name__)

@api.route("/location", methods=['GET'])
def list_games():

    locations = Location.query.all()
    locations = list(map(lambda location: location.serialize(), locations))

    return jsonify(locations), 200