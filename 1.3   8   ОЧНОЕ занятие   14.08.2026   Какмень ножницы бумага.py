"""
Задача 10. "Игра камень ножницы бумага."
Напишите программу, которая.

1. Запрашивает у пользователя выбор (камень, ножницы, бумага).
2. Случайным образом выбирает вариант для компьютера.
3. Определяет победителя (или ничью) и выводит результат.
4. Повторяет игру, пока пользователь не введет "Выход".

"""
import random



# while True:
#
#     us_choice = input('Выберите "Камень", "Ножницы", "Бумага" или "Выход": ')
#     pc_choice = random.choice(['Камень', 'Ножницы', 'Бумага'])
#
#     if us_choice == "Выход":
#         print('Игра окончена')
#         break
#
#     elif us_choice != "Камень" and us_choice !=  "Ножницы" and us_choice !=  "Бумага":
#         print("Ввод некорректных данных")
#
#     elif us_choice == pc_choice:
#         print('Ничья')
#
#
#     elif us_choice == "Камень" and pc_choice == "Ножницы":
#         print("Ты выиграл")
#
#     elif us_choice == "Камень" and pc_choice == "Бумага":
#         print("Ты проиграл")
#
#     elif us_choice == "Ножницы" and pc_choice == "Бумага":
#         print("Ты выиграл")
#
#     elif us_choice == "Ножницы" and pc_choice == "Камень":
#         print("Ты проиграл")
#
#     elif us_choice == "Бумага" and pc_choice == "Камень":
#         print("Ты выиграл")
#
#     elif us_choice == "Бумага" and pc_choice == "Ножницы":
#         print("Ты проиграл")


winners = {'Камень' : 'Ножницы', 'Ножницы' : 'Бумага', 'Бумага' : 'Камень'}

while True:

    us_choice = input('Выберите "Камень", "Ножницы", "Бумага" или "Выход": ')
    pc_choice = random.choice(['Камень', 'Ножницы', 'Бумага'])

    if us_choice == "Выход":
        print('Игра окончена')
        break
    elif us_choice == pc_choice:
        print('Ничья')

    elif us_choice != "Камень" and us_choice !=  "Ножницы" and us_choice !=  "Бумага":
        print("Ввод некорректных данных")

    elif winners[us_choice] == pc_choice:
        print(f'Ты выиграл. Компьютер выбрал {pc_choice}, а ты - {us_choice}')
    else:
        print(f'Ты проиграл. Компьютер выбрал {pc_choice}, а ты - {us_choice}')