
# Import collections of geometric objects + bounding box
from shapely.geometry import MultiPoint, MultiLineString, MultiPolygon, box

from shapely.geometry import Point, LineString, Polygon
import shapely

empty_shape = shapely.wkt.loads('GEOMETRYCOLLECTION EMPTY')
simple_poly_wkt = 'POLYGON ((45 58, 46 59, 57 55, 54 46, 44 49, 46 53, 44 54, 45 58))'
square_wkt = 'POLYGON ((4 5, 5 5, 5 4, 4 4, 4 5))'

simple_poly = shapely.wkt.loads(simple_poly_wkt)

empty_geometry_collection = empty_shape.intersection(simple_poly)
