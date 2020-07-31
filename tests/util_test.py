
from applot import util

def test_scale_1():
    s = util.make_scale(0,1,0,10)
    assert s(0.1) == 1

def test_scale_2():
    s = util.make_scale(10,0,0,1)
    assert s(1) == 0.9

def test_scale_3():
    s = util.make_scale(0,1,11,1)
    assert s(0.1) == 10


def test_extent_1():
    arr = [2,3,1,2,4,3]
    assert util.extent(arr) == (1,4)

def test_extent_2():
    arr = [1]
    assert util.extent(arr) == (1,1)

def test_extent_3():
    arr = []
    assert util.extent(arr) == (None,None)

