

class Element:
    name = None
    attributes = {}
    children = []

    # Default transformations
    _translate = (0,0)
    _scale = (1,1)
    _rotate = (0,0,0)
    
    # Element's transformations
    translate = (0,0)
    scale = (1,1)
    rotate = (0,0,0)
    
    def __init__(self,name=None,**kwargs):
        self.name = self.name if name is None else name
        if 'attributes' in kwargs:
            self.attributes = {
                **self.attributes,
                **kwargs['attributes']}
        if 'a' in kwargs:
            self.attributes = {
                **self.attributes,
                **kwargs['a']}
        if 'children' in kwargs:
            self.children = [
                *self.children,
                *kwargs['children']]
        if 'c' in kwargs:
            self.children = [
                *self.children,
                *kwargs['c']]
        
    def __repr__(self):
        return f"<Element:{self.name} attrs:{len(self.attributes)} chldrn:{len(self.children)}/>"
        
    def __str__(self):
        return self.render()
    
    def render(self):
        # Add transformations if necessary
        if "transform" not in self.attributes:
            transform = []
            if self.translate != self._translate:
                transform.append(f"translate{self.translate}")
            if self.scale != self._scale:
                transform.append(f"scale{self.scale}")
            if self.rotate != self._rotate:
                transform.append(f"rotate{self.rotate}")
            if transform:
                self.attributes['transform'] = " ".join(transform)
        # Create attribute string
        sattr = " ".join(f'{k}="{v}"' for k,v in self.attributes.items())
        if sattr: sattr = " " + sattr
        # Render string of children
        schildren = "".join(str(c) for c in self.children)
        # Format and return
        return f"<{self.name}{sattr}>{schildren}</{self.name}>"

    def addChild(self,c,*args):
        self.children.append(c)
        self.children.extend(args)
        return self
    
    def delChild(self,c):
        i = self.children.index(c)
        self.children.pop(i)
        return self

