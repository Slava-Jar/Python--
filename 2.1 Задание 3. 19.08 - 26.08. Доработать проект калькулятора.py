from tkinter import *

from tkinter import messagebox as mb


def summ():
    s1 = e1.get()
    if not s1.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено число")
        return
    s2 = e2.get()
    if not s2.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено число")
        return

    slag1 = int(s1)
    slag2 = int(s2)
    summa = slag1 + slag2
    m1['text']= f"{s1} + {s2} = {str(summa)}"
    answer = mb.askretrycancel(title="Вопрос", message="Сложить еще два числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        m1['text']= ""
    else:
        window.destroy()


def multi():
    s1 = e1.get()
    if not s1.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено число")
        return # Возвращаемся из функции, если ввод некорректен
    s2 = e2.get()
    if not s2.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено число")
        return # Возвращаемся из функции, если ввод некорректен

    slag1 = int(s1)
    slag2 = int(s2)
    summa = slag1 * slag2
    m1['text']= f"{s1} * {s2} = {str(summa)}"
    answer = mb.askretrycancel(title="Вопрос", message="Умножить еще два числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        m1['text']= ""
    else:
        window.destroy()


def multi_3_num():
    s1 = e1.get()
    if not s1.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено число")
        return # Возвращаемся из функции, если ввод некорректен
    s2 = e2.get()
    if not s2.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено число")
        return # Возвращаемся из функции, если ввод некорректен

    #   ДОБАВЛЕНА ПЕРЕМЕННАЯ ДЛЯ ТРЕТЬЕГО ЧИСЛА
    s3 = e3.get()
    if not s3.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В третье поле должно быть введено число")
        return # Возвращаемся из функции, если ввод некорректен

    slag1 = int(s1)
    slag2 = int(s2)

    #   ТРЕТЬЕ ЧИСЛО ИЗ str ПЕРЕВОДИТСЯ В int
    slag3 = int(s3)

    summa = slag1 * slag2 * slag3
    m1['text']= f"{s1} * {s2} * {s3}= {str(summa)}"
    answer = mb.askretrycancel(title="Вопрос", message="Умножить еще три числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)

        #   УДАЛЕНИЕ ЧИСЛА ИЗ ОКНА ВВОДА ПОСЛЕ ПОДТВЕРЖДЕНИЯ ПОВТОРА ОПЕРАЦИИ
        e3.delete(0, END)
        m1['text']= ""
    else:
        window.destroy()


window = Tk()
window.title("Калькулятор")
m = Label(height=3, text="Введи два числа и нажми на кнопку для вычисления суммы")
m.pack()

e1 = Entry()
e1.pack()
e2 = Entry()
e2.pack()

   #   ДОБАВЛЕНО ПОЛЕ ВВОДА ТРЕТЬЕГО ЧИСЛА
e3 = Entry()
e3.pack()

b = Button(text="Сложить два числа", command=summ)
b.pack()
b1 = Button(text='Умножить два числа', command=multi)
b1.pack()

   #   ДОБАВЛЕНА КНОПКА УМНОЖЕНИЯ ТРЕХ ЧИСЕЛ
b3 = Button(text='Умножить три числа', command=multi_3_num)
b3.pack()

m1 = Label(height=3)
m1.pack()

window.mainloop()