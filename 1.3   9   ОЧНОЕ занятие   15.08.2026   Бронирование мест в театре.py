"""
Бронирование мест в кинотеатре.
Есть зал размером 10Х15 мест.
Для каждого ряда:
Проверить каждое место.
Если место свободно: спросить, хочет ли пользователь его купить.
Если пользователь согласен: забронировать место.
После завершения вывести количество свободных мест.
"""

hall = [[0 for place in range(3)] for row in range(2)]


for row in range(2):
    print(f'Ряд: {row + 1}')
    for place in range(3):
        print(f'Место {place + 1}')

        if hall[row][place] == 0:
            answer = input("Хотите забронировать? Введите \"да\" или \"нет\": ")
        if answer == "да":
            hall[row][place] = 1


# count = 0
# for row in range(2):
#     for place in range(3):
#         if hall[row][place] == 0:
#             count += 1
ebanaya_peremennaya = 0
for row in hall:
    ebanaya_peremennaya += row.count(0)

print(f'Количество свободных мест {ebanaya_peremennaya}')


for row in hall:
    print(row)