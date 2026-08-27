import turtle
from turtle import *
from time import sleep
from random import *




"""
Здание к окнами. Цикл рисования окон с функцией.

# def windows():
#     color("red")
#     begin_fill()
#     for i in range(2):
#         forward(15)
#         left(90)
#         forward(15)
#         left(90)
#     end_fill()
#
# penup()
# goto(-170, -170)
# pendown()
# color("grey")
# begin_fill()
#
# for i in range(2):
#     forward(100)
#     left(90)
#     forward(200)
#     left(90)
#
# end_fill()
#
# for row in range(6):
#     for column in range(2):
#         penup()
#         goto(-145 + column * 30, -145 + row * 30)
#         print(xcor(), ycor())
#         pendown()
#         windows()
"""



""" 
Игра "Поймай черепашку"

На игровом поле находится черепашка красного цвета. Она самостоятельно движется вперед.
Игрок может нажимать на черепашку мышкой.
При нажатии на черепашку она должна:

1. переместиться в случайную точку игрового поля
2. повернуться на случайный угол
3. продолжить движение

Игра продолжается до тех пор, пока одна из черепашек не выйдет за границы игрового поля.
При завершении игры все черепашки должы остановиться и на экране должно появиться сообщение "Игра окончена".

"""



#   задаем ширину и высоту
w = 300
h = 300



#   создаем игровое поле
penup()
goto(-300, -300)
pendown()
color("lightgreen")
begin_fill()
for i in range(4):
    forward(w * 2)
    left(90)
end_fill()



#   создаём черепашку
t1 = Turtle()
t1.color("red")
t1.shape("turtle")
t1.width(5)



#   создаем функцию, которая при нажатии на черепашку
#   отправляет ее в произвольную точку -300<x<300 -300<у<300
#   поворачивает на произвольный угол от 0 до 180
def catcht1(x, y):
    t1.penup()
    t1.goto(randint(-300, 300), randint(-300, 300))
    t1.pendown()
    t1.left(randint(0, 180))



#   создаем функцию, которая останавливает игру
#   если черепашка вышла за границы поля 600 / 600
def gameFinish(t1):
    t1_outside = abs(t1.xcor()) > w or abs(t1.ycor()) > h
    print(t1_outside)
    print(t1.xcor(), t1.ycor())
    return t1_outside



#   при нажатии на черепашку активируется функция catcht1
t1.onclick(catcht1)



#   пока выполняются условия цикл продолжается -
#   черепашка движется вперед на 7 пикселей
#   и замирает на 0,2 секунды (from time import sleep)
while gameFinish(t1) != True :
    t1.forward(7)
    sleep(0.2)



#   очистка поля
#   перемещение черепашки в конечную точку
#   вывод надписи "Игра окончена"
#   скрытие черепашки
t1.clear()
t1.penup()
t1.goto(-50, 0)
t1.write("Игра окончена!", font=("Arial", 30))
t1.pendown()
t1.hideturtle()

#   не закрывать окно с черепашкой
mainloop()
