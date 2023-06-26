from pytest import approx
from common.r3 import R3
from polyedr import Segment, Edge, Facet, Polyedr


def test_0():
    assert Polyedr(f"data/ccc.geom").without_draw() == 8


def test_1():
    assert Polyedr(f"data/ccc_1.geom").without_draw() == 0


def test_2():
    assert Polyedr(f"data/ccc_2.geom").without_draw() == 0


def test_3():
    assert Polyedr(f"data/ccc_3.geom").without_draw() == 0
