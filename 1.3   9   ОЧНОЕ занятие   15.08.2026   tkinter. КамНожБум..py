import tkinter as tk
import random

choices = ["Камень", "Ножницы", "Бумага"]


win = tk.Tk()
win.geometry("400x300")
win.title("Камень, ножницы, бумага")

result_label = tk.Label(win, text="Сделайте выбор", font=("Arial", 14))
result_label.pack(pady=10)

def play(user_choice):
    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        result = "Ничья!"
    elif (user_choice == "Камень" and comp_choice == "Ножницы") or \
         (user_choice == "Ножницы" and comp_choice == "Бумага") or \
         (user_choice == "Бумага" and comp_choice == "Камень"):
        result = "Вы выиграли!"
    else:
        result = "Вы проиграли!"

    result_label.config(
    text=f"Вы: {user_choice}\nКомпьютер: {comp_choice}\n{result}")


def choice_stone():
    play("Камень")

def choice_paper():
    play("Бумага")

def choice_scissors():
    play("Ножницы")


# l = tk.Label(win, text = "")
# l.pack(pady= 30)

b_stone = tk.Button(win, text = "Камень", width=20, command=choice_stone)
b_stone.pack(pady = 5)

b_paper = tk.Button(win, text = "Бумага", width=20, command=choice_paper)
b_paper.pack(pady = 5)


b_scissors = tk.Button(win, text = "Ножницы", width=20, command=choice_scissors)
b_scissors.pack(pady = 5)


tk.mainloop()