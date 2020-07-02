
from ... import util, svg
from .PlotTitle import PlotTitle
from .PlotAxis import PlotAxis
from .PlotInner import PlotInner
from .PlotObject import PlotObject

class PlotBase(PlotObject):
    # Default w & h
    _width = 600
    _height = 400

    # Default inner plot positions
    _pxmin = 80
    _pymin = 110
    _pxmax = 565
    _pymax = 300
    _tick_pad = 10
    _ax_pad = 1

    # Default n axis ticks
    _n_xticks = 5
    _n_yticks = 5

    

    # Arguments should be corresponding PlotObjects or svgs
    def __init__(self,title=None,axis=None,inner=None,grid=None,bg=None):
        self._title = title
        self._axis = axis
        self._inner = inner
        self._grid = grid
        self._bg = bg
        # self.width = self._width
        # self.height = self._height

    def toSvg(self):
        canv = svg.SVG(
            f"0 0 {self._width} {self._height}",
            a={'width': self._width}
            )
        valid = lambda o: (
            isinstance(o,PlotObject) or 
            isinstance(o,svg.Element))
        if valid(self._bg):
            canv.children.append(self._bg)
        if valid(self._grid):
            canv.children.append(self._grid)
        if valid(self._inner):
            canv.children.append(self._inner)
        if valid(self._axis):
            canv.children.append(self._axis)
        if valid(self._title):
            canv.children.append(self._title)
        return canv

    def save(self,filename,filemode="w"):
        with open(filename,filemode) as f:
            f.write(self.render())

