
from .Element import Element

class SVG(Element):
    name = "svg"

    def __init__(self,viewBox="0 0 100 100",*args):
        super().__init__(*args)
        self.attributes['viewBox'] = viewBox

        