from applot import util

class TestScale:
    def test_scale_1(self):
        s = util.make_scale(0,1,0,10)
        assert s(0.1) == 1

    def test_scale_2(self):
        s = util.make_scale(10,0,0,1)
        assert s(1) == 0.9

    def test_scale_3(self):
        s = util.make_scale(0,1,11,1)
        assert s(0.1) == 10

class TestExtent:
    def test_extent_1(self):
        arr = [2,3,1,2,4,3]
        assert util.extent(arr) == (1,4)

    def test_extent_2(self):
        arr = [1]
        assert util.extent(arr) == (1,1)

    def test_extent_3(self):
        arr = []
        assert util.extent(arr) == (None,None)

class TestArange:
    def test_arange_1(self):
        assert util.arange(5) == [0,1,2,3,4]

    def test_arange_2(self):
        assert util.arange(4,-1,-1) == [0,1,2,3,4][::-1]

    def test_arange_3(self):
        assert util.arange(0,10,2) == [0,2,4,6,8]

    def test_arange_4(self):
        assert util.arange(0,1,0.2) == [0.0,0.2,0.4,0.6,0.8]