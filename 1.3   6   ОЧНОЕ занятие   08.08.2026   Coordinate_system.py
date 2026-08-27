#ЗНАКОМСТВО С КООРДИНАТНОЙ СИСТЕМОЙ

from turtle import *   #   из библиотеки turtle импортируем все
# speed(1)
def draw_landscape() :
    penup()
    goto(-200,-200)
    pendown()
    color("green")
    begin_fill()
    for i in range(2) :
        forward(400)
        left(90)
        forward(150)
        left(90)
    end_fill()

draw_landscape()



def draw_sky() :
    penup()
    goto(-200,-50)
    pendown()
    color("lightblue")
    begin_fill()
    for i in range(2) :
        forward(400)
        left(90)
        forward(400)
        left(90)
    end_fill()

draw_sky()



def draw_sun() :
    penup()
    goto(140, 250)
    pendown()
    color("yellow")
    begin_fill()
    for i in range(18) :
        forward(40)
        left(100)
    end_fill()

draw_sun()



def draw_block_of_flats() :
    penup()
    goto(-150,-150)
    pendown()
    color("grey")
    begin_fill()
    for i in range(2) :
        forward(120)
        left(90)
        forward(180)
        left(90)
    penup()
    end_fill()

draw_block_of_flats()



penup()
goto(-130,-130)
pendown()



def draw_window() :
    color("yellow")
    begin_fill()
    for k in range(3) :
        for a in range(2) :
            for i in range(2) :
                forward(30)
                left(90)
                forward(30)
                left(90)

            penup()
            forward(50)
            pendown()

        penup()
        backward(100)
        left(90)
        forward(50)
        right(90)
        pendown()

    end_fill()

draw_window()



penup()
goto(50,-120)
pendown()



def draw_pharmacy() :
    color("white")
    begin_fill()
    for i in range(2) :
        forward(100)
        left(90)
        forward(100)
        left(90)

    end_fill()
draw_pharmacy()



penup()
goto(65,-60)
pendown()



def draw_cros() :
    color("red")
    pensize(5)
    begin_fill()
    forward(50)
    backward(25)
    left(90)
    forward(25)
    backward(50)
    hideturtle()

draw_cros()



exitonclick()
