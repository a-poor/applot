"""
PlotContext.py
created by Austin Poor

NOTE: A possible alternative implementation idea

Possible example usage...

data = pd.DataFrame({
    "x":np.arange(10),
    "x":np.arange(0,10,2),
    "category":[0]*6+[1]*4
})
with PlotContext() as plot:
    plot.data(
        x=data.x,
        y=data.y,
        color=data.category
        )
    plot.title("My sample plot")
    plot.xaxis(np.arange(10))
    plot.yaxis(np.arange(0,10,2))


"""

class PlotContext:
    def __init__(self):
        # Get possible starging args
        pass

    def __enter__(self):
        pass

    def __exit__(self,*exec):
        pass
