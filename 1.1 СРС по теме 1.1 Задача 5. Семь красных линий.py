from turtle import *

colormode(255)
pensize(5)
shape('turtle')
speed(5)

penup()
goto(-400, 400)
pendown()

for gor_step in range(3) :
    if gor_step == 2 :
        pencolor(0, 255, 0)
    else :
        pencolor(255, 0, 0)
    forward(100)
    penup()
    right(90)
    forward(100)
    left(90)
    pendown()

for vert_step in range(3) :
    if vert_step == 2 :
        pencolor(0, 255, 0)
    else:
        pencolor(255, 0, 0)
    left(90)
    forward(100)
    penup()
    right(90)
    forward(100)
    pendown()

penup()
goto(0, 0)
pendown()

# нарисовать силуэт котенка


mainloop()