from turtle import *


def draw_squre(x,y):
    penup()
    goto(x,y)
    pendown()

    for i in range(4):
        forward(200)
        left(90)

draw_squre(100,100)
draw_squre(-300,100)
draw_squre(-300,-300)
draw_squre(100,-300)
