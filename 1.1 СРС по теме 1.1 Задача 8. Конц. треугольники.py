from turtle import *

shape('turtle')
colormode(255)
pensize(3)
speed(5)

ht()

for r in range(40, 0, -10) :
    for i in range(6) :
        pencolor(255, 0, r * 6)
        fillcolor(0, r * 6, 255)
        begin_fill()

        for step in range(3) :
            fd(r)
            lt(120)
        rt(60)

        end_fill()

mainloop()