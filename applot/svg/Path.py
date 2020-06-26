
from .Element import Element

class Path(Element):
    name = "path"

    def __init__(self,d,**kwargs):
        super().__init__(self,**kwargs)
        self.attributes['d'] = d

    