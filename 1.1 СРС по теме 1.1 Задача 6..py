from turtle import *

shape('turtle')
colormode(255)
pensize(3)
speed(3)

ht()

for r in range(40, 0, -10) :
    for i in range(6) :
        pencolor(255, 0, r * 6)
        fillcolor(0, r * 6, 255)
        begin_fill()
        circle(r)
        end_fill()
        penup()
        fd(20)
        rt(90)
        fd(20)
        lt(90)
        pendown()
        right(60)   #   тк черепашка возвращается в одно и то же место ее нужно просто повернуть на нужный угол


mainloop()