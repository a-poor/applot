
from .PlotInner import PlotInner
from ... import svg

class InnerScatter(PlotInner):
    plot_type = "InnerScatter"

    def __init__(self,xs,ys,color,radius,**kwargs):
        assert len(xs) == len(ys)
        super().__init__(**kwargs)
        self.xs = xs
        self.ys = ys
        n = len(xs)
        if isinstance(color,"string"):
            self.c = [color for _ in range(n)]
        else: self.c = color
        if (not hasattr(radius,'__iter__') 
            or isinstance(radius,str)):
            self.r = [radius for _ in range(n)]
        else: self.r = radius
    
    def toSvg(self):
        g = svg.Group(a={'id':'inner-plot'})
        iterable = zip(
            self.xs,self.ys,
            self.c,self.r
        )
        g.children = [
            svg.Circle(x,y,r,a={'fill':c})
            for x, y, c, r in iterable
        ]
        return g

