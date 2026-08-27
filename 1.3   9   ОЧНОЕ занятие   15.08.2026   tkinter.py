import tkinter as tk


   #   функция для кнопки (при нажатии на кнопку текст меняется на указанный в функции)
def replace():

   #   number.get() — метод, который читает (получает) текущее числовое значение из переменной number
   #   + 5 — математическая операция сложения. К полученному числу прибавляется 5.
   #   number.set(...) — метод, который записывает (устанавливает) новое значение обратно в переменную number.
   #   Вызов number.get() вернёт 0.
   #   Выражение number.get() + 5 посчитает 0 + 5 = 5.
   #   number.set(5) запишет 5 обратно в переменную.

    number.set(number.get() +5)

def plus_1():
    number.set(number.get() + 1)

def minus_1():
    number.set(number.get() - 1)

   #   функция забирает все из поля ввода и выводит в консоль
def print_entry():
    print(entry.get())




   #   создано окно
win = tk.Tk()


   #   заданы размеры окна
win.geometry("1000x400")


   #   задано наименование окна
win.title("Рабочее окно")

   #   создана управляющая переменная (control variable) типа целое число для работы с виджетами в Tkinter
   #   tk.IntVar() - конструктор класса, который создает переменную для хранения целых чисел (int)
   #   value = 0 — начальное значение переменной. Если этот параметр не указать, по умолчанию будет 0
   #   number — имя (ссылка), по которому вы будете обращаться к этой переменной в коде
number = tk.IntVar(value = 0)


fr_center = tk.Frame(win)
fr_center.pack()

fr_left = tk.Frame(fr_center)
fr_left.pack(side="left")

fr_right = tk.Frame(fr_center)
fr_right.pack(side="right")



   #   создан лейбл, задан его шрифт и размер шрифта, надпись внутри лейбла сдвинута влево w (west)
label = tk.Label(fr_left, textvariable = number, fg = "darkblue", bg = "lightblue", font = ("Arial", 16), height=3, width=30, anchor="w")


   #   лейбл проявлен в окне win, сдвинут по y на 30 пикселей, выравнен по левому краю side и по центру по вертикали (pady = (20, 20))
label.pack(pady = 10, padx = 40)


   #   создана кнопка, заданы ее размеры, задана команда (если reglace(), то выполнится сразу без нажатия кнопки)
button1 = tk.Button(fr_right, text = "+5", height=3, width=30, command = replace)


   #   кнопка проявлена в окне
button1.pack(pady = 10)


button2 = tk.Button(fr_right, text = "+1", height=3, width=30, command = plus_1)
button2.pack(pady = 10)

button3 = tk.Button(fr_right, text = "-1", height=3, width=30, command = minus_1)
button3.pack(pady = 10)

   #   создано и проявлено поле ввода
entry = tk.Entry(fr_left, width=30)
entry.pack(pady = 10)

button4 = tk.Button(fr_right, text = "Вывести в консоль", height=3, width=30, command = print_entry)
button4.pack(pady = 10)






tk.mainloop()