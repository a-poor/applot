
from ... import util, svg
from .PlotObject import PlotObject

class PlotInner(PlotObject):
    plot_type = None

    _xmin = None
    _ymin = None
    _xmax = None
    _ymax = None

    def __init__(self,xrange,yrange,xdata,ydata,xscale,yscale):
        self.xmin, self.xmax = xrange
        self.ymin, self.ymax = yrange
        self.xdata = xdata
        self.ydata = ydata
        self.xscale = xscale
        self.yscale = yscale

    def __repr__(self):
        return f"<{self.plot_type} />"

    def toSvg(self):
        raise NotImplementedError

