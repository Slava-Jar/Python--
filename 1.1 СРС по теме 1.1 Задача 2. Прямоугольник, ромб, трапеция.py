import turtle
t = turtle.Turtle()  # создаём черепашку
t.shape('turtle')  #  определяем форму крсора - черепашка
turtle.colormode(255)  # включаем RGB-режим: цвета от 0 до 255

t.fillcolor(0, 0, 255)
t.begin_fill()  # начало заполнения прямоугольника цветом

t.penup()

t.goto(0,0)

for _ in range(4) :
    t.forward(100)
    t.left(90)

t.end_fill()  # крнец заполнения прямоугольника цветом

t.goto(50, -100)
t.right(45)

t.fillcolor(0, 255, 255)
t.begin_fill()  # начало заполнения ромба цветом

for _ in range(4) :
      t.forward(100)
      t.right(90)

t.end_fill()  # крнец заполнения ромба цветом

t.goto(-40,200)  #  начало трапеции
t.left(45)  #  поворот черепашки в горизонталь

t.fillcolor(255, 0, 0)
t.begin_fill()  # начало заполнения трапеции цветом

t.fd(180)  #  вправо
t.left(120)  #  поворот
t.fd(100)  #вверх
t.left(60)  #  поворот
t.fd(80)  #  влево
t.left(60)  #  поворот
t.fd(100)  #  вниз

t.end_fill()  # крнец заполнения трапеции цветом

t.goto(0,0)

turtle.done()  #  оставить окно открытым
