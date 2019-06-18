from flask_restful import Resource
from flask import jsonify


class HelloWorld(Resource):
  def get(self):
    return jsonify({"status": "success", "data": [1, 2, 3, 4]})
