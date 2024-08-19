from flask import abort, request, Blueprint
import json


from Controllers.polygon_clipping_by_line import polygon_clipping_by_line

# Função para converter a string de coordenadas em uma lista de tuplas
def parse_coordinates(coord_string):
  coord_string = coord_string.strip("[]")
  pairs = coord_string.split("),(")
  return [tuple(map(float, pair.strip("()").split(","))) for pair in pairs]

REQUEST_API = Blueprint('request_api', __name__)
def get_blueprint():
  """Return the blueprint for the main app module"""
  return REQUEST_API

@REQUEST_API.route('/clipping_by_line', methods=['POST'])
def clipping_by_line(): 
  objeto = request.get_data() 
  js_obj = json.loads(objeto)

  polygon = parse_coordinates(js_obj["polygon"])
  cutters = parse_coordinates(js_obj["cutters"])

  return polygon_clipping_by_line(polygon, cutters)