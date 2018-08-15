from turtle import *

def baum(x):
    if x < 5: return
    else:
        forward(x)
        left(45)
        baum(x/2)
        right(90)
        baum(x/2)
        left(45)
        back(x)
    return

speed(2)
left(90)
baum(100)
hideturtle()
