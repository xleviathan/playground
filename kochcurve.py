import turtle
def draw(t,length,n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t,length,n-1)
    t.rt(2*angle)
    draw(t,length,n-1)
    t.lt(angle)
    t.bk(length*n)
def koch_curve(t,x,a = 60 ,b =120):
    if x < 10.0:
        t.fd(x)
        return None
    koch_curve(t,x//3)
    t.lt(a)
    koch_curve(t,x//3)
    t.rt(b)
    koch_curve(t,x//3)
    t.lt(a)
    koch_curve(t,x//3)
bob = turtle.Turtle()
def snowflake(t,x):
    for each in range(3):
        koch_curve(t,x)
        t.lt(120)
snowflake(bob,50)