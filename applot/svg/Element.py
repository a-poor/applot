

class Element:
    name = None
    attributes = {}
    children = []
    
    def __init__(self,name=None,**kwargs):
        self.name = self.name if name is None else name
        if 'attributes' in kwargs:
            self.attributes = {
                **self.attributes,
                **kwargs['attributes']}
        if 'children' in kwargs:
            self.children = [
                *self.children,
                *kwargs['children']]
        
    def __repr__(self):
        return f"<Element:{self.name} attrs:{len(self.attributes)} chldrn:{len(self.children)}/>"
        
    def __str__(self):
        return self.render()
    
    def render(self):
        sattr = " ".join(f'{k}="{v}"' for k,v in self.attributes.items())
        if sattr: sattr = " " + sattr
        schildren = "".join(str(c) for c in self.children)
        return f"<{self.name}{sattr}>{schildren}</{self.name}>"

    def addChild(self,c,*args):
        self.children.append(c)
        self.children.extend(args)
        return self
    
    def delChild(self,c):
        i = self.children.index(c)
        self.children.pop(i)
        return self
            
    
    def setChildren(self,c):
        self.children = c
        return self

