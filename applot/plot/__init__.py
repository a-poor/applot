from .. import svg, util


from . import base

from .HBarPlot import HBarPlot
from .LinePlot import LinePlot
from .ScatterPlot import ScatterPlot
from .Slopegraph import Slopegraph
from .SqAreaPlot import SqAreaPlot
from .StackedHBarPlot import StackedHBarPlot
from .StackedVBarPlot import StackedVBarPlot
from .VBarPlot import VBarPlot


####### Make functions for plotting ########

# def _plot(x,y,):
#     return

# def scatter(x,y,color,size):
#     pass

def scatter(x,y):
    width = 600
    height = 400
    margin = {
        "top": 50,
        "bottom": 50,
        "left": 50,
        "right": 50
    }
    xscale = util.make_scale(
        *util.extent(x),
        margin["left"],
        width-margin["left"]
        )
    yscale = util.make_scale(
        *util.extent(x),
        margin["left"],
        width-margin["left"]
        )
