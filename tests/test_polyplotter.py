"""
TODO: Write these tests
"""
import matplotlib.pyplot as plt
import numpy as np
import pytest
import shapely
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
from shapely import wkt  # required to access shapely.wkt
from shapely.geometry import LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon, box

from polyplotter import plotpoly as p


def test_empty_geom_collection():
    empty_shape = wkt.loads("GEOMETRYCOLLECTION EMPTY")


def test_simple_wkt():
    simple_poly_wkt = "POLYGON ((45 58, 46 59, 57 55, 54 46, 44 49, 46 53, 44 54, 45 58))"


def test_square_wkt():
    square_wkt = "POLYGON ((4 5, 5 5, 5 4, 4 4, 4 5))"


def test_simple_poly():
    simple_poly_wkt = "POLYGON ((45 58, 46 59, 57 55, 54 46, 44 49, 46 53, 44 54, 45 58))"
    simple_poly = wkt.loads(simple_poly_wkt)
    empty_shape = wkt.loads("GEOMETRYCOLLECTION EMPTY")
    empty_geometry_collection = empty_shape.intersection(simple_poly)


def test_ndarray_coords():
    coords = np.array(
        [
            [1389, 2300],
            [1390, 2301],
            [1394, 2305],
            [1368, 2306],
            [1374, 2300],
            [1379, 2299],
            [1383, 2299],
            [1389, 2300],
        ],
        dtype=np.int32,
    )

    soln = p(coords)

    # Create a polygon and add it to a patch collection
    polygon = Polygon(coords)
    patches = [polygon]

    # Create figure and axes
    fig, ax = plt.subplots()

    # Create a patch collection. With facecolor set to none, this will be a line plot.
    p = PatchCollection(patches, facecolor="none", edgecolor="black")

    # Add the collection to the plot
    ax.add_collection(p)

    # Automatically adjust view to the data
    ax.autoscale_view()

    plt.show()


if __name__ == "__main__":
    pytest.main([__file__])
