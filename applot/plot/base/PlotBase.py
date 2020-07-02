
from ... import util, svg
from .PlotTitle import PlotTitle
from .PlotAxis import PlotAxis
from .PlotInner import PlotInner
from .PlotObject import PlotObject

class PlotBase(PlotObject):
    def __init__(self,title=None,axis=None,inner=None,grid=None,bg=None):
        self.title = title
        self.axis = axis
        self.inner = inner
        self.grid = grid
        self.bg = bg

    def toSvg(self):
        canv = svg.SVG("0 0 400 600")
        valid = lambda o: (
            isinstance(o,PlotObject) or 
            isinstance(o,svg.Element))
        if valid(self.bg):
            canv.children.append(self.bg)
        if valid(self.grid):
            canv.children.append(self.grid)
        if valid(self.inner):
            canv.children.append(self.inner)
        if valid(self.axis):
            canv.children.append(self.axis)
        if valid(self.title):
            canv.children.append(self.title)
        return canv

    def save(self,filename,filemode="w"):
        with open(filename,filemode) as f:
            f.write(self.render())

