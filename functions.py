import math
def area(radius):
    a = math.pi * radius **2
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
def distance(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
