from flask import jsonify

from . import app_obj, API_PREFIX


@app_obj.route(f"/{API_PREFIX}/example1", methods=["GET"])
def example1():
    return jsonify({"data": {"jradek": 123}})


@app_obj.route(f"/{API_PREFIX}/example2", methods=["GET"])
def example2():
    return jsonify({"data": [1, 2, 3]})
