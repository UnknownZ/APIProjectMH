from flask import Blueprint, jsonify, request
from models.platform import Platform

api = Blueprint('platform_api', __name__)

@api.route("/platform", methods=['GET'])
def list_games():

    platforms = Platform.query.all()
    platforms = list(map(lambda platform: platform.serialize(), platforms))

    return jsonify(platforms), 200