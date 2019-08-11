from flask import jsonify, Blueprint

from . import API_PREFIX

rest_blueprint = Blueprint("rest_blueprint", __name__)


@rest_blueprint.route(f"/{API_PREFIX}/example1", methods=["GET"])
def example1():
    return jsonify({"data": {"jradek": 123}})


@rest_blueprint.route(f"/{API_PREFIX}/example2", methods=["GET"])
def example2():
    return jsonify({"data": [1, 2, 3]})
