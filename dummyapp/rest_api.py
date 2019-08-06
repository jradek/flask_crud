from flask import jsonify
from . import app_obj

API_PREFIX = "/api/v1"


@app_obj.route(f"{API_PREFIX}/example", methods=["GET"])
def example():
    return jsonify({"jradek": 123})
