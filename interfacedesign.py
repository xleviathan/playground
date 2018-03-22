import turtle
import math
t = turtle.Turtle()
def square(t,l):
    for i in range(4):
        t.fd(l)
        t.lt(90)
def polygon(t,l,n):
    for each in range(n):
        t.fd(l)
        t.lt(int(360/n))
def circle(t,r):
    circumference = 2*(math.pi)*r
    polygon(t,l=circumference/360,n=360)
def arc(t,r,angle):
    arc_length = 2 * math.pi * r * angle /360
    n =  int(arc_length/3) + 1
    step_length = arc_length /3
    step_angle = angle/n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
arc(t,5,270)
turtle.mainloop()