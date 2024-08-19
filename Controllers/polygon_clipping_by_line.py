import json
from shapely.geometry import Polygon, LineString
from shapely.ops import split
from Services.formatedGeoString import format_polygons_for_coordinates

# Função para converter a string de coordenadas em uma lista de tuplas
def parse_coordinates(coord_string):
  coord_string = coord_string.strip("[]")
  pairs = coord_string.split("),(")
  return [tuple(map(float, pair.strip("()").split(","))) for pair in pairs]

# Função para converter geometrias em objetos Polygon do Shapely
def serialize_geometry(geom):
  if geom.geom_type == 'Polygon':
    return Polygon(geom.exterior.coords)
  else:
    raise ValueError("Apenas geometrias do tipo Polygon podem ser serializadas.")

# Função para arredondar coordenadas para evitar pequenos deslocamentos
def round_coordinates(coords, precision=6):
  return [(round(x, precision), round(y, precision)) for x, y in coords]

def polygon_clipping_by_line(polygon, cutters):
  # Criar objetos Polygon e LineString
  polygon = Polygon(round_coordinates(polygon))
  polyline = LineString(round_coordinates(cutters))

  # Verificar se a linha cruza o polígono
  if not polygon.intersects(polyline):
      return {'error': 'Não existe cruzamento!'}

  # Dividir o polígono pela linha
  divided_polygons = split(polygon, polyline)

  # Arredondar coordenadas dos polígonos resultantes para evitar pequenos deslocamentos
  divided_polygons_list = [
      Polygon(round_coordinates(geom.exterior.coords)) for geom in divided_polygons.geoms
  ]

  # Formatar polígonos para SQL Server (opcional, depende do uso posterior)
  divides = format_polygons_for_coordinates(divided_polygons_list)

  return divides
