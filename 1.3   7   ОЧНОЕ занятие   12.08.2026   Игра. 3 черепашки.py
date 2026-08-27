import turtle
from turtle import *
from time import sleep
from random import *



""" 
Игра "Поймай черепашку"

На игровом поле находится 3 черепашки разных цветов. Каждая черепашка самостоятельно движется вперед.
Игрок может нажимать на черепашек мышкой.
При нажатии на черепашку она должна:

1. переместиться в случайную точку игрового поля
2. повернуться на случайный угол
3. продолжить движение
Игра продолжается до тех пор, пока черепашка не выйдет за границы игрового поля.
При завершении игры черепашка должа остановиться и на экране должно появиться сообщение "Игра окончена".

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



#   создаём черепашек
t1 = Turtle()
t1.color("red")
t1.shape("turtle")
t1.width(5)

t2 = Turtle()
t2.color("yellow")
t2.shape("turtle")
t2.width(5)

t3 = Turtle()
t3.color("purple")
t3.shape("turtle")
t3.width(5)



#   создаем функцию, которая при нажатии на черепашку
#   отправляет ее в произвольную точку -300<x<300 -300<у<300
#   поворачивает на произвольный угол от 0 до 180
def catcht1(x, y):
    t1.penup()
    t1.goto(randint(-300, 300), randint(-300, 300))
    t1.pendown()
    t1.left(randint(0, 180))

def catcht2(x, y):
    t2.penup()
    t2.goto(randint(-300, 300), randint(-300, 300))
    t2.pendown()
    t2.left(randint(0, 180))

def catcht3(x, y):
    t3.penup()
    t3.goto(randint(-300, 300), randint(-300, 300))
    t3.pendown()
    t3.left(randint(0, 180))



#   создаем функцию, которая останавливает игру
#   если черепашка вышла за границы поля 600 / 600
def game_over():
    t1_outside = abs(t1.xcor()) > w or abs(t1.ycor()) > h
    t2_outside = abs(t2.xcor()) > w or abs(t2.ycor()) > h
    t3_outside = abs(t3.xcor()) > w or abs(t3.ycor()) > h
    print(t1_outside, t2_outside, t3_outside)
    print(t1.xcor(), t1.ycor(), t2.xcor(), t2.ycor(), t3.xcor(), t3.ycor())
    return t1_outside or t2_outside or t3_outside


#   при нажатии на черепашку активируется функция catcht1
t1.onclick(catcht1)
t2.onclick(catcht2)
t3.onclick(catcht3)



#   пока выполняются условия цикл продолжается -
#   черепашка движется вперед на 7 пикселей
#   и замирает на 0,2 секунды (from time import sleep)
t2.left(120)
t3.right(120)
# while gamefinish1(t1) != True and gamefinish2(t2) != True and gamefinish3(t3) != True:
while game_over() != True:
    t1.forward(7)
    t2.forward(7)
    t3.forward(7)
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

t2.clear()
t2.penup()
t2.goto(-50, 0)
t2.write("Игра окончена!", font=("Arial", 30))
t2.pendown()
t2.hideturtle()

t3.clear()
t3.penup()
t3.goto(-50, 0)
t3.write("Игра окончена!", font=("Arial", 30))
t3.pendown()
t3.hideturtle()

#   не закрывать окно с черепашкой
mainloop()





