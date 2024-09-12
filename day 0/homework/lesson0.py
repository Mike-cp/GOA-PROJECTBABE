from turtle import *

speed(10)
width(4)
color("black")
#walls
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

#pen up
penup()
goto(120, 0)
pendown()

#door
right(180)
forward(100)
right(90)
forward(40)
right(90)
forward(100)

#pen up for roof
penup()
goto(0, 200)
pendown()

#roof
left(150)
forward(200)

right(120)
forward(200)

#windows
penup()
goto(20,100)
pendown()

#window
color("gray")
left(60)
forward(70)
left(-90)
forward(40)
right(90)
forward(70)
right(90)
forward(40)
left(90)
left(90)
forward(20)
left(90)
forward(70)
left(90)
left(90)
forward(35)
left(90)
forward(20)
left(90)
left(90)
forward(40)

#door handel
penup()
goto(150,50)
pendown()
color("black")

left(90)
left(90)
forward(10)


exitonclick()

