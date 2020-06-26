
def make_scale(dmin,dmax,rmin,rmax):
    dextent = dmax - dmin
    rextent = rmax - rmin
    sfactor = rextent / dextent
    def scale(n):
        return (n - dmin) * sfactor + rmin
    return scale


