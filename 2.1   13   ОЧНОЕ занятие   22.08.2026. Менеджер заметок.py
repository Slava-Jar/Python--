import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def add_note():
    try:
        file = fd.askopenfilename(filetypes=[("Text", "*.txt"), ("All", "*.*")])           #   ?
        if not file:
            return
        with open(file, "r", encoding="utf-8") as file:
            note = file.read()
            txt.insert(tk.END, note)                 #   ?
    except Exception as er:                          #   ?
        mb.showerror("Ошибка", er)              #   ?



def clear_note():
    answer = mb.askyesno(title = "Вопрос", message = "Удалить все заметки?")
    if answer:
        txt.delete(1.0, tk.END)


def save_note():
    try:
        file = fd.asksaveasfilename(filetypes=[("Text", "*.txt")])           #   ?
        if not file:
            return
        with open(file, "w", encoding="utf-8") as file:
            note = txt.get(1.0, tk.END)       #   берем все из текстового поля от начала до конца
            file.write(note)                         #   записываем в файл
            mb.showinfo("Info", "Файл успешно сохранен")
    except Exception as er:                          #   исключить все ошибки
        mb.showerror("Ошибка", er)              #   ?


win = tk.Tk()
win.geometry("1000x400")
win.title("Менеджер заметок")


txt_frame = tk.Frame(win)
txt_frame.pack(padx=10, side = tk.LEFT)

button_frame = tk.Frame(win)
button_frame.pack(padx=10, side = tk.RIGHT)


txt = tk.Text(txt_frame, width = 65, height = 20,  bg = "lightyellow", wrap = tk.WORD)   #   wrap=tk.WORD переноси по словам, а не по буквам
txt.pack(side = tk.LEFT)

scr = tk.Scrollbar(txt_frame, command = txt.yview)   #   ?   txt.yview
scr.pack(side = tk.LEFT, fill = tk.Y)                #   ?   fill = tk.Y
txt.config(yscrollcommand = scr.set)                 #   ?   yscrollcommand   scr.set


def info_spr():
    mb.showinfo("Info", "Приложение 'Менеджер заметок'")

mainmenu = tk.Menu(win)                                             #   создано меню
win.config(menu=mainmenu)
filemenu = tk.Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = "Добавить заметку", command=add_note)
filemenu.add_command(label = "Очистить", command=clear_note)
filemenu.add_command(label = "Выгрузить в файл", command=save_note)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = win.destroy)

mainmenu.add_cascade(label="File", menu = filemenu)


info_menu = tk.Menu(mainmenu, tearoff = 0)
info_menu.add_command(label = "About", command=info_spr)

mainmenu.add_cascade(label="Info", menu = info_menu)


# button1 = tk.Button(button_frame, text = "Добавить заметку", width = 25, command=add_note)
# button1.grid(padx = 10, pady=5, column = 1, row = 0)
#
# spacer = tk.Label(button_frame, width=1, padx=0)  #   зазор между кнопками
# spacer.grid(row=0, column=2)
#
# button2 = tk.Button(button_frame, text = "Очистить", width = 25, command=clear_note)
# button2.grid(padx = 10, pady=5, column = 3, row = 0)
#
# button3 = tk.Button(button_frame, text = "Выгрузить в файл", width = 25, command=save_note)
# button3.grid(padx = 10, pady=5, column = 1, row = 2)


button_frame.grid_columnconfigure(0, weight=1)           #   ?
button_frame.grid_columnconfigure(4, weight=1)           #   ?
tk.mainloop()