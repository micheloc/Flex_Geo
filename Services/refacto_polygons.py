import json
import uuid
from shapely.geometry import Polygon, mapping
from shapely.geometry import Polygon, Point, LineString
from shapely.ops import nearest_points

def format_polygon_output(polygon, name="ZM - POLI AREA"):
    """
    Formata a saída de um polígono ajustado para o formato desejado.
    """
    # Gerando IDs únicos
    objID = str(uuid.uuid4())
    id_ = str(uuid.uuid4())
    
    # Calculando o centro do polígono
    centroid = list(polygon.centroid.coords)[0]
    center_legend = json.dumps({"center": [centroid[1], centroid[0]]})
    
    # Convertendo o polígono para geoJSON
    geo_json = json.dumps({
        "type": "Polygon",
        "centroid": [centroid[1], centroid[0]],
        "coordinates": [[(y, x) for x, y in polygon.exterior.coords]]
    })
    
    # Calculando área e tamanho do polígono
    area = round(polygon.area, 2)  # Exemplo de cálculo da área, ajustar conforme necessário
    
    # Montando o dicionário de saída
    output = {
        "objID": objID,
        "id": id_,
        "nome": name,
        "file": name,
        "legendColor": "#FFFFFF",
        "setLegend": "",
        "field": {
            "TALHAO": name,
            "ZONA": "ZM 1",
            "ZONA_AREA": f"ZM 1 {area} Ha",
            "AREA": area,
            "PONTOS": len(polygon.exterior.coords),
            "CODIGO_ZM": 1,
            "ZM_CODIGO": "ZM_1 - 1"
        },
        "rotulo": [
            "SEM LEGENDA",
            "TALHAO",
            "ZONA",
            "ZONA_AREA",
            "AREA",
            "PONTOS",
            "CODIGO_ZM",
            "ZM_CODIGO"
        ],
        "color": None,
        "geoString": polygon.wkt,
        "centerLegend": center_legend,
        "geoJson": geo_json,
        "tamanho": area,
        "type": "Polygon"
    }
    
    return output

def Refactor_polygons(poly):
  # Gerando a saída formatada para cada polígono
  formatted_outputs = [format_polygon_output(Polygon(polygon)) for polygon in poly]

  return formatted_outputs;
