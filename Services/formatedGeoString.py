from shapely.geometry import Polygon, LineString

def format_polygons_for_sql_server(polygons):
  result = []
  for polygon in polygons:
    if isinstance(polygon, Polygon):
      coordinates = ', '.join(' '.join(map(str, coord)) for coord in polygon.exterior.coords)
      result.append("geometry::STPolyFromText('POLYGON(({}))', 4326)".format(coordinates))
  return result

def format_points_for_sql_server(centroids):
  result = []
  for centroid in centroids:
    x, y = centroid.x, centroid.y
    result.append("geometry::STPointFromText('POINT({0} {1})', 4326)".format(x, y))
  return result


def format_polygons_for_coordinates(polygons):
    coordinates = []
    for polygon in polygons:
        if isinstance(polygon, Polygon):
            # Extrair as coordenadas do exterior do polígono
            coord = [list(coord) for coord in polygon.exterior.coords]
            coordinates.append(coord)
    return coordinates