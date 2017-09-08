class vert:
    "Hilbert curve vertex"
    def __init__(self,rotation,half):
        self.rot = rotation%360
        self.half=half
    def __str__(self):
        return "v.{}.{}".format(self.rot,self.half)

class side:
    "Hilbert curve side"
    def __init__(self,rotation):
        self.rot=rotation%360
    def __str__(self):
        return "s.{}".format(self.rot)

class constant:
    "Hilbert curve constant form"
    #universal constant:
    class regular:
        u_constant_reg = [vert(90,1),side(0),vert(0,1),side(90),vert(0,2),side(180),vert(270,2)]
        def __init__(self,rotation=0):
            self.rot=rotation
            self.form = [vert(90+rotation,1),side(rotation),vert(rotation,1),side(90+rotation),vert(rotation,2),side(180+rotation),vert(270+rotation,2)]
        def __str__(self):
            return [str(x) for x in self.form]
    class goofy:
        u_constant_reg = [vert(270,1),side(0),vert(0,1),side(270),vert(0,2),side(180),vert(90,2)]
        def __init__(self,rotation=0):
            self.rot=rotation
            self.form = [vert(270+rotation,1),side(rotation),vert(rotation,1),side(270+rotation),vert(rotation,2),side(180+rotation),vert(90+rotation,2)]
        def __str__(self):
            return [str(x) for x in self.form]

        
def hilbertGen(n):
    curve=constant.regular(0).form
    for q in range(n-1):
        vertsFound = []
        for i,j in enumerate(curve):
            if type(j) == vert:
                if j.half == 1:
                    vertsFound.append([i,j.rot,(curve[i+1].rot-j.rot)==90])
                else:
                    vertsFound.append([i,j.rot,(curve[i-1].rot-j.rot)==90])

        vertsFound.reverse()
        for m in vertsFound:
            if m[2]:
                curve[m[0]+1:m[0]+1] = constant.regular(m[1]).form
                del curve[m[0]]
            else:
                curve[m[0]+1:m[0]+1] = constant.goofy(m[1]).form
                del curve[m[0]]
    return curve