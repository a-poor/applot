
from . import base
from .. import svg, util
from .colors import colors

class ScatterPlot(base.PlotBase):
    def __init__(self,x,y,color='black',**kwargs):
        self.x = x
        self.y = y
        self.color = color

        xrange = min(x), max(x) #NOTE: if xmin, xmax in kwargs
        yrange = min(y), max(y) #NOTE: if ymin, ymax in kwargs

        # base.PlotInner._layout

        # xscale
        # yscale

        # xticks
        # yticks

        if "nticks" in kwargs:
            self.nticks = kwargs


        if radius in kwargs:
            radius = kwargs['radius']
        else:
            radius=None
        if title in kwargs:
            title = kwargs['title']
        else:
            title=None

    def toSvg(self):
        pass

