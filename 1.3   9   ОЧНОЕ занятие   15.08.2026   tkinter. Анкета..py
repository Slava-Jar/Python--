import tkinter as tk
import datetime


def date_brth_calc():
    name = entry_name.get()
    try:
        bthd = datetime.datetime.strptime(entry_date.get() , "%d.%m.%Y")

        now = datetime.datetime.now()

        age = now.year - bthd.year  # Сначала считаем возраст как разницу лет

        if (now.month, now.day) < (bthd.month, bthd.day):  # Корректируем, если день рождения ещё не наступил в этом году
            age -= 1
        if age % 10 == 1 and age % 100 != 11:  # Склонение слова «год» по правилам русского языка
            word = "год"
        elif age % 10 in (2, 3, 4) and age % 100 not in (12, 13, 14):
            word = "года"
        else:
            word = "лет"

        result_text = f"{name},вам {age} {word}"
        number.set(result_text)  # Сохраняем готовую фразу

            #   изначально лейбл выводится без текста
        l_result.config(text = f"{name},вам {age} {word}")



    except ValueError:
        print("Ошибка даты")


win = tk.Tk()
win.geometry("800x600")
win.title("Анкета")


   #   StringVar() (место IntVar) для сохранения текста
number = tk.StringVar(value="Результат появится здесь")


label1 = tk.Label(win, text = "Имя:", font = ("Arial", 12), height=3, width=30)
label1.pack()

entry_name = tk.Entry(win, width=30)
entry_name.pack(pady = 10)

label2 = tk.Label(win, text = "Дата рождения:", font = ("Arial", 12), height=3, width=30)
label2.pack(pady = 10)

entry_date = tk.Entry(win, width=30)
entry_date.pack(pady = 10)

button = tk.Button(win, text = "Возраст", height=3, width=30, command = date_brth_calc)
button.pack(pady = 10)

label_res = tk.Label(win, textvariable = number, bg = "lightblue", font = ("Arial", 12), height=3, width=24)
label_res.pack(pady = 10)

l_result = tk.Label(win, bg = "lightblue", font = ("Arial", 12), height=3, width=24)
l_result.pack(pady = 10)



tk.mainloop()