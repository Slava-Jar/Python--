from tkinter import *
from tkinter import messagebox as mb

win = Tk()
win.geometry("600x500")
win.title("Анкета студента")


def show_info():
    name = entry1.get()
    surname = entry2.get()
    group = entry3.get()
    age = entry4.get()
    sex = gender.get()
    about = txt.get(1.0, END)

    if not name or not surname or not group or not age:
        mb.showwarning("Warning", "Заполните обязательные поля")
    if not age.isdigit():
        mb.showwarning("Warning", "В поле возраст должны быть цифры")

    l5.config(text = f'Имя: {name} фамилия: {surname}, группа: {group}, возраст {age}, пол {sex}, О себе {about}')


def close_win():
    win.destroy()


def clear_all():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    l5.config(text = "")


header_frame = Frame(win)
header_frame.pack()

form_frame = Frame(win)
form_frame.pack()

text_frame = Frame(win)
text_frame.pack()

button_frame = Frame(win)
button_frame.pack()


l = Label(header_frame, text = "Анкета студента", width=30)
l.pack(pady = 10)


gender = StringVar(value="Мужской")   #   по умолчанию точка будет на кнопке "Мужской"

r_but1 = Radiobutton(form_frame, text="Мужской", variable=gender, value="Мужской")
r_but1.grid(column = 0, row = 4)

r_but2 = Radiobutton(form_frame, text="Женский", variable=gender, value="Женский")
r_but2.grid(column = 1, row = 4)


l1 = Label(form_frame,  text = "Имя", width=30)
l1.grid(column = 0, row = 0)
entry1 = Entry(form_frame, width=30)
entry1.grid(column = 1, row = 0)

l2 = Label(form_frame,  text = "Фамилия", width=30)
l2.grid(column = 0, row = 1)
entry2 = Entry(form_frame, width=30)
entry2.grid(column = 1, row = 1)

l3 = Label(form_frame,  text = "Группа", width=30)
l3.grid(column = 0, row = 2)
entry3 = Entry(form_frame, width=30)
entry3.grid(column = 1, row = 2)

l4 = Label(form_frame,  text = "Возраст", width=30)
l4.grid(column = 0, row = 3)
entry4 = Entry(form_frame, width=30)
entry4.grid(column = 1, row = 3)


button1 = Button(button_frame, text = "Показать данные", width=25, command = show_info)
button1.pack(pady = 10)

button2 = Button(button_frame, text = "Выход", width=25, command = close_win)
button2.pack(pady = 10)

button3 = Button(button_frame, text = "Очистить", width=25, command = clear_all)
button3.pack(pady = 10)


l5 = Label(win,  text = "")
l5.pack()

l6 = Label(text_frame, text = "О себе")
l6.pack()

txt = Text(text_frame, width = 30, height = 8)
txt.pack(side = LEFT)

scr = Scrollbar(text_frame, command = txt.yview)
scr.pack(side = LEFT, fill = Y)
txt.config(yscrollcommand = scr.set)

mainloop()