from flask import abort, request, Blueprint, jsonify
import json
import ast

from Services.polygon_clipping_by_line import polygon_clipping_by_line
from Services.refacto_polygons import Refactor_polygons

# Função para converter a string de coordenadas em uma lista de tuplas
def parse_coordinates(coord_string):
  coord_string = coord_string.strip("[]")
  pairs = coord_string.split("),(")
  return [tuple(map(float, pair.strip("()").split(","))) for pair in pairs]

REQUEST_API = Blueprint('request_clipping', __name__)

@REQUEST_API.route('/clipping_by_line', methods=['POST'])
def clipping_by_line(): 
  objeto = request.get_data() 
  js_obj = json.loads(objeto)

  polygon = parse_coordinates(js_obj["polygon"])
  cutters = parse_coordinates(js_obj["cutters"])

  return polygon_clipping_by_line(polygon, cutters)


@REQUEST_API.route('/refactor_poly_vertices', methods=['POST'])
def refactor_poly_vertices(): 
  try:
    # Obtém os dados da solicitação como bytes
    objeto = request.get_data()

    # Decodifica os bytes para uma string
    json_str = objeto.decode('utf-8')

    # Remove caracteres de controle inválidos e espaços extras
    json_str = json_str.replace('\n', '').replace('\r', '').replace('\t', '')

    # Imprime a string JSON recebida para depuração
    print("Recebido JSON:")
    print(json_str)

    # Converte a string JSON para um objeto Python
    js_obj = json.loads(json_str)
    
    # Acessa o campo 'polygon' do objeto
    polygon_strings = js_obj.get('polygon', [])
    
    # Processa cada string de polígono
    polygons = []
    for polygon_str in polygon_strings:
        try:
            # Usa ast.literal_eval para converter a string para uma lista de tuplas
            polygon = ast.literal_eval(polygon_str)
            # Verifica se é uma lista de tuplas
            if isinstance(polygon, list) and all(isinstance(coord, tuple) and len(coord) == 2 for coord in polygon):
                polygons.append(polygon)
            else:
                raise ValueError("Formato de coordenadas inválido.")
        except (SyntaxError, ValueError) as e:
            return jsonify({"error": f"Erro ao processar o polígono: {e}"}), 400

    # Retorna a lista de polígonos processada
    return Refactor_polygons(polygons)

  except json.JSONDecodeError as e:
    return jsonify({"error": f"Erro ao decodificar JSON: {e}"}), 400

  return "Teste"