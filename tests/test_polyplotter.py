"""
TODO: Add more tests
"""
import matplotlib
import numpy as np
import pytest
from shapely import wkt  # required to access shapely.wkt

from polyplotter import plotpoly as p

matplotlib.use("Agg")  # non-iteractive usage so the graphs don't pop up


def test_empty_geom_collection():
    empty_shape = wkt.loads("GEOMETRYCOLLECTION EMPTY")
    p(empty_shape)


def test_simple_wkt():
    simple_poly_wkt = "POLYGON ((45 58, 46 59, 57 55, 54 46, 44 49, 46 53, 44 54, 45 58))"
    p(simple_poly_wkt)


def test_square_wkt():
    square_wkt = "POLYGON ((4 5, 5 5, 5 4, 4 4, 4 5))"
    p(square_wkt)


def test_simple_poly():
    simple_poly_wkt = "POLYGON ((45 58, 46 59, 57 55, 54 46, 44 49, 46 53, 44 54, 45 58))"
    simple_poly = wkt.loads(simple_poly_wkt)
    empty_shape = wkt.loads("GEOMETRYCOLLECTION EMPTY")
    empty_geometry_collection = empty_shape.intersection(simple_poly)
    p(empty_geometry_collection)


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
    p(coords)


if __name__ == "__main__":
    pytest.main([__file__])