from tkinter import *
import turtle
turtle.mode("logo")
turtle.hideturtle()
turtle.speed(0)
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

def drawHilbertRaw(hilbertCurve,size,n):
    length = size/((2**n)-1)
    for i in hilbertCurve:
        if type(i) == side:
            turtle.setheading(i.rot)
            turtle.forward(length)
def save_turtle(loc):
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file=loc)

def drawHilbert(n,length):
    "wrapper for [hilbertGen()] and [exportTurtleEPS()]"
    drawHilbertRaw(hilbertGen(n),length,n)

window=turtle.Screen()
window.screensize()
window.setup(width=1.0,height=1.0)
def cascadeFrom8():
    #1
    turtle.penup()
    turtle.setpos(-451,-151)
    turtle.pencolor("#872121")
    turtle.pendown()
    turtle.speed(1)
    turtle.width(50)
    drawHilbert(1,301)

    #2
    turtle.penup()
    turtle.setpos(-526,-226)
    turtle.pencolor("#877c21")
    turtle.pendown()
    turtle.speed(3)
    turtle.width(25)
    drawHilbert(2,452)

    #3
    turtle.penup()
    turtle.setpos(-564,-264)
    turtle.pencolor("#378721")
    turtle.pendown()
    turtle.speed(6)
    turtle.width(10)
    drawHilbert(3,527)

    #4
    turtle.penup()
    turtle.setpos(-582,-282)
    turtle.pencolor("#21875f")
    turtle.pendown()
    turtle.speed(10)
    turtle.width(7)
    drawHilbert(4,565)
    

    #5
    turtle.penup()
    turtle.setpos(-592,-292)
    turtle.pencolor("#217487")
    turtle.pendown()
    turtle.speed(0)
    turtle.width(3)
    drawHilbert(5,584)
    
    #6
    turtle.penup()
    turtle.setpos(-596,-296)
    turtle.pencolor("#213887")
    turtle.pendown()
    turtle.width(2)
    drawHilbert(6,593)

    #7
    turtle.penup()
    turtle.setpos(-599,-299)
    turtle.pencolor("#542187")
    turtle.pendown()
    turtle.width(1)
    drawHilbert(7,598)
    
    #8
    turtle.penup()
    turtle.setpos(-600,-300)
    turtle.pencolor("#87216d")
    turtle.pendown()
    drawHilbert(8,600)
    
if __name__ == '__main__':
    cascadeFrom8()

