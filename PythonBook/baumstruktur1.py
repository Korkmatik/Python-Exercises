from turtle import *

def baum(x):
    if x < 5: return
    else:
        forward(x)
        left(90)
        baum(x/2)
        right(180)
        baum(x/2)
        left(90)
        back(x)
    return

speed(0)
left(90)
baum(100)
hideturtle()
