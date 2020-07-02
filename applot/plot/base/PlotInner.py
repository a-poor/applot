
from ... import util, svg
from .PlotObject import PlotObject

class PlotInner(PlotObject):
    plot_type = None

    _pxmin = None
    _pymin = None
    _pxmax = None
    _pymax = None

    _ppad = 1

    def __init__(self,dxmin,dxmax,dymin,dymax,xdata,ydata):
        self.xdata = xdata
        self.ydata = ydata

        self.dxmin = xmin 
        self.xmax = xmax
        self.ymin = ymin 
        self.ymax = ymax
        self.computescale()

    def computescale(self):

        self.xscale = None
        self.yscale = None

    def __repr__(self):
        return f"<{self.plot_type} />"

    def toSvg(self):
        raise NotImplementedError

