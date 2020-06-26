
from . import base
from .. import svg

class ScatterPlot(base.PlotInner):
    plot_type = "ScatterPlot"

    # def __init__(self,**kwargs):
    #     super().__init__(**kwargs)
    
    def toSvg(self):
        g = svg.Group(a={'id':'inner-plot'})

        return g

