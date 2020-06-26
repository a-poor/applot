
from .Element import Element

class Circle(Element):
    name = "circle"

    def __init__(self,cx,cy,r,**kwargs):
        super().__init__(self,**kwargs)
        self.attributes['cx'] = cx
        self.attributes['cy'] = cy
        self.attributes['r'] = r

    