import turtle
t = turtle.Turtle()  # создаём черепашку
# t.speed(.6)
t.shape('turtle')  #  определяем форму крсора - черепашка
turtle.colormode(255)  # включаем RGB-режим: цвета от 0 до 255

r = 255
g = 0
b = 0

pen_r = 0
pen_g = 255
pen_b = 0

for i in range(50, 9, -20) :
    t.begin_fill()  #  начало заполнения круга
    t.fillcolor(r, g, b)
    t.pencolor(pen_r, pen_g, pen_b)
    t.width(8)  #  ширина пера. Можно и так pensize(8)
    t.circle(i)  #  рисуем круг радиус 50
    t.end_fill()  #  крнец заполнения цветом
    t.penup()  # поднять перо
    t.backward(i * 2)  # движение назад на 100

    r -= 100
    g += 100
    b += 100

    pen_r += 100
    pen_g -= 100
    pen_b += 100

    t.pendown()


turtle.done()  #  оставить окно открытым




