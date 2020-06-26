
from .. import util, svg
from .PlotObject import PlotObject

class PlotTitle(PlotObject):
    x = 3
    y = 8
    font_size = 5
    font_family = "Helvetica"
    font_weight = "bold"
    font_fill = "black"
    
    def __init__(self,title,**kwargs):
        self.title = title
        super().__init__(**kwargs)

    def render(self):
        title = svg.Text(self.x,self.y,self.title)
        if self.font_size:
            title.attributes['font-size'] = self.font_size
        if self.font_family:
            title.attributes['font-family'] = self.font_family
        if self.font_weight:
            title.attributes['font-weight'] = self.font_weight
        if self.font_fill:
            title.attributes['fill'] = self.font_fill
        wrapper = svg.Group(a={'id':'plot-title'})
        wrapper.addChild(title)
        return wrapper.render()

