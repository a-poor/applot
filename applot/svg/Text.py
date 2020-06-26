
from .Element import Element

class Text(Element):
    name = "text"

    def __init__(self,x,y,text,**kwargs):
        self.children = [text]
        super().__init__(self,**kwargs)
        self.attributes['x'] = x
        self.attributes['y'] = y

    