
from datetime import datetime


"""
Создайте файл log.txt сос следующим содержимым (каждая строка - запись лога).

Напишите программу которая:
1. Считывает файл.
2. Выводит количество записей каждого типа (EROR, INFO, WARNING).
3. Находит самую раннюю и самую позднюю дату в логе.
4. Сколько дней между самой ранней и самой поздней датой.
"""
from itertools import count

# with open(r'C:\Users\Administrator\Desktop\log.txt', encoding="utf-8") as file:
#     for line in file :
#         print(line.split()[1])


#   задаем счетчики
count_info = 0
count_error = 0
count_warning = 0

#   открываем файл, проходим по первому индексу каждой строки
with open(r'C:\Users\Administrator\Desktop\log.txt', encoding="utf-8") as file:
    for line in file :
        parts = line.split()
        print(parts[1])
        if line.split()[1] == "INFO" :
            count_info += 1
        elif line.split()[1] == "ERROR" :
            count_error += 1
        elif line.split()[1] == "WARNING" :
            count_warning += 1

print(f'Количество ошибок ИНФО: {count_info},  ')
print(f'Количество ошибок ERROR: {count_error}')
print(f'Количество ошибок WARNING: {count_warning}')

early_date = 0
late_date = 0
date_list = []

with open(r'C:\Users\Administrator\Desktop\log.txt', encoding="utf-8") as file:
    for line in file :
        date_list.append(datetime.strptime(line.split()[0], "%Y-%m-%d"))
    late_date = max(date_list).day
    early_date = min(date_list).day
    print(f"""Самая ранняя дата: {early_date}
Самая поздняя дата {late_date}
Разница между самой ранней и самой поздней датой: {late_date - early_date} дней""")

