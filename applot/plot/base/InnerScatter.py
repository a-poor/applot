
from .PlotInner import PlotInner
from ... import svg

class InnerScatter(PlotInner):
    plot_type = "InnerScatter"

    # def __init__(self,**kwargs):
    #     super().__init__(**kwargs)
    
    def toSvg(self):
        g = svg.Group(a={'id':'inner-plot'})

        return g

