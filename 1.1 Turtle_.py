from turtle import *
# import turtle as t
colormode(255)  # разрешаем использовать режим RGB
shape('turtle')
color((117, 2, 84), (238, 242, 22))  # определение цвета пера и заполнения
pensize(4)  # ширина пера
speed(.5)  # cкорость пера (0-1_1. Знакомство с Python)

begin_fill()  # начало заполнения фигуры
for _ in range(2):
    fd(100)  #   движение вперёд на 100 пикселей (forward)
    lt(90)  # изменение угла движения влево на 90 град.
end_fill()  # завершение заполнения
# fillcolor('#16F21A')  # только цвет заполнения
# begin_fill()
# for _ in range(3):
#     fd(100)
#     lt(120)
# end_fill()
# fillcolor((238, 242, 22))
# fd(100)
# backward(100)  # движение назад без смены направления
# penup()  # поднять перо
# goto(-100, 100)  # перейти в координату
# pendown()  # опустить перо
# r = 191
# g = 33
# b = 142
# step = 0
# for i in range(200, 10, -20):
#     fillcolor(r, g, b)
#     for _ in range(6):
#         begin_fill()
#         for _ in range(3):
#             fd(i)
#             lt(120)
#         # circle(i)
#         end_fill()
#         rt(60)
#     r += 7
#     g += 6
#     b += 5
#
#     # penup()
#     # step -= 150
#     # goto(step, 0)
#     pendown()
# penup()
# goto(0, 0)
# pendown()
mainloop()