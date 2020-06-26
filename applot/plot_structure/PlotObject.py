

class PlotObject:
    
    def __str__(self):
        return self.render()

    def render(self):
        raise NotImplementedError

