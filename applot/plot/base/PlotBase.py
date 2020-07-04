
from ... import util, svg
from .PlotTitle import PlotTitle
from .PlotAxis import PlotAxis
from .PlotInner import PlotInner
from .PlotObject import PlotObject
from .PlotGrid import PlotGrid
from .PlotBg import PlotBg

class PlotBase(PlotObject):
    plot_name  = "PlotBase"

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

    # Title
    _title_x = 15
    _title_y = 40
    _title_font_size = 28
    # Subtitle
    _subtitle_x = 15
    _subtitle_y = 70
    _subtitle_font_size = 18
    # Caption
    _caption_x = 15
    _caption_y = 385
    _caption_font_size = 10

    # Default n axis ticks
    _n_xticks = 5
    _n_yticks = 5

    

    # Arguments should be corresponding PlotObjects or svgs
    # def __init__(self,title=None,axis=None,inner=None,grid=None,bg=None):
    
    def __init__(self,x,y,color="black",xticks=None,yticks=None,title=None,subtitle=None,caption=None,**kwargs):
        assert len(x) == len(y)
        self.x = x
        self.y = y
        self.color = color if len(color) == len(x) else [color for _ in x]
        
        self.xticks = xticks
        self.yticks = yticks

        self.title = title
        self.subtitle = subtitle
        self.caption = caption

        for k,v in kwargs.items():
            setattr(self,k,v)

        self.setPlotObjects()

    def __repr__(self):
        return f"<applot.{self.plot_name}>"

    def setPlotObjects(self):
        self._title = PlotTitle(self.title)
        self._axis = PlotAxis() #(self.xticks,self.yticks)
        self._inner = None
        self._grid = PlotGrid()
        self._bg = PlotBg()

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

