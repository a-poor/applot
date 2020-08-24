
from ... import svg
from .PlotObject import PlotObject
# from .PlotGrid import PlotGrid
# from .PlotBg import PlotBg

class PlotBase:
    _default_positions = {
        'title': ( 4, 3,92, 7),
        'inner': (16,12,80,70),
        'xaxis': (16,83,80,10),
        'yaxis': ( 4,12,11,70)
    }

    # _aspect_ratio = (1,1)
    _width = 500

    def __init__(self,**kwargs):
        self.title = None
        self.inner = None
        self.xaxis = None
        self.yaxis = None
        
        if 'title' in kwargs:
            self.title = kwargs['title']
        if 'inner' in kwargs:
            self.inner = kwargs['inner']
        if 'xaxis' in kwargs:
            self.xaxis = kwargs['xaxis']
        if 'yaxis' in kwargs:
            self.yaxis = kwargs['yaxis']

        # self.bg_color = "#f0f0f0"
        # self.aspect_ratio = self._aspect_ratio[:]
        self.width = self._width

    def __str__(self):
        return str(self.toSVG())

    def render(self): 
        return self.__str__()

    def toSVG(self):
        # viewbox = 
        child_elements = [
            self.title,
            self.inner,
            self.xaxis,
            self.yaxis
        ]
        c = [c for c in child_elements if c is not None]
        return svg.SVG(c=c,a={'width':self.width})

    def reshuffle(self):
        pass
