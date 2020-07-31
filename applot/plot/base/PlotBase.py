
from ... import svg
from .PlotObject import PlotObject

class PlotBase:
    _default_positions = {
        'title': {}
    }

    def __init__(self):
        self.title = None
        self.inner = None
        self.xaxis = None
        self.yaxis = None

        self.bg_color = "#f0f0f0"

    def __str__(self):
        return str(self.toSVG())

    def render(self): 
        return self.__str__()

    def toSVG(self):
        # Child classes should override this...
        raise NotImplementedError

    def addTitle(self,title):
        self.title = title
        return self

    def addInner(self,inner):
        self.inner = inner
        return self

    def addXAxis(self,axis):
        self.xaxis = axis
        return self
    
    def addYAxis(self,axis):
        self.yaxis = axis
        return self

    def reposition(self):
        pass
