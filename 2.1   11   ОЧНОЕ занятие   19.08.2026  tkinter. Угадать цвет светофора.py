from tkinter import *
import random
from tkinter import messagebox as mb


win = Tk()
win.geometry("600x200")
win.title("Угадай цвет светофора")


def random_color():
    pass


def check_color():
        my_color = color_var.get()
        pc_color = random.choice(['зеленый', 'желтый', 'красный'])

        if not my_color:
            mb.showwarning("Предупреждение!", "Заполните поле!")
            return

        if my_color == pc_color:
            res = "Вы угадали"
        else:
            res = f"Вы не угадали. Ваш выбор '{my_color}', выбор компьютера '{pc_color}'"

        answer = mb.askyesno("Вопрос", "Результат в метку?")
        if answer:
            l_res.config(text = res)
        else:
            l_res.config(text = "")
            mb.showinfo("Info", res)


color_var = StringVar(value = "зеленый")
rb1 = Radiobutton(win, text="зеленый", variable=color_var, value="зеленый")
rb1.pack()
rb2 = Radiobutton(win, text="желтый", variable=color_var, value="желтый")
rb2.pack()
rb3 = Radiobutton(win, text="красный", variable=color_var, value="красный")
rb3.pack()


# l = Label(win, text="Введите цвет светофора", width=30)
# l.pack()

# entry = Entry(win, width=30)
# entry.pack(pady=20)


button1 = Button(win, text = "Проверить", width=25, command = check_color)
button1.pack(pady = 20)


l_res = Label(win, text="")
l_res.pack()

mainloop()