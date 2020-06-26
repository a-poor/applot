
from .. import util, svg
from .PlotTitle import PlotTitle
from .PlotAxis import PlotAxis
from .PlotInner import PlotInner
from .PlotObject import PlotObject

class PlotBase(PlotObject):
    def __init__(self,title=None,axis=None,inner=None):
        self.title = title
        self.axis = axis
        self.inner = inner

    def render(self):
        canv = svg.SVG()
        if isinstance(self.inner,PlotObject):
            canv.children.append(
                self.inner.render()
            )
        if isinstance(self.axis,PlotObject):
            canv.children.append(
                self.axis.render()
            )
        if isinstance(self.title,PlotObject):
            canv.children.append(
                self.title.render()
            )
        return canv.render()

    def save(self,filename,filemode="w"):
        with open(filename,filemode) as f:
            f.write(self.render())



