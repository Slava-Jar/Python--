"""
import random
n = random.randint(1, 6)   #   число 6 входит в диапазон
a = 0
while a != n:
    a = int(input("Введите число: "))
print(f'Вы угадали. Это число {n}')
"""



"""
i = 1
while i <= 10:
   print(i)
   i += 1
"""



"""
n = 0
while n < 10 :
    n = int(input("Введите число: "))
    print(n)
"""



"""   
p = ""
while p != "Пароль" :
    p = input("Введите пароль: ")
print("Начинаем выполнение программы")
"""



"""
a = 9
b = 0
while b != a :
    b = int(input("Введите число: "))
print(f'Угадал. Это число {b}')
"""



"""   


text =  input("Введите текст. Пять символов: ")
while len(text) != 5 :
    text = input("Неверно. Пять символов: ")
print("Верно")
"""



"""   
text = input("Введите более пяти символов: ")

while len(text) < 5 :
    print(len(text))
    text = input("Неверно. Введите заново: ")
print(f'Right. Text length {len(text)}')
"""



"""   
text = input("Введите более пяти символов: ")

while len(text) < 5 :
    print(len(text))
    text = input("Неверно. Введите заново: ")
print(f'Right. You entered "{text}". Text length {len(text)}')
"""



"""   
i = 0
while True :
    print(i)
    i += 1
    if i >= 10 :
        print(i)
        break
"""



"""   """
st = "Это тестовая строка."
print(st.find("я"))   #   выводится индекс символа "я"

print(st.find("о", 3))   #   выводит индекс первого элемента "о" начиная с индекса 4

print(st.find("***"))   #   если искать несуществующий элемент, выводится -1

print(st.index("я"))   #   выводится индекс элемента

print(f'Индекс точки: {st.index(".")}')   #   выводится индекс элемента

# print(f'Индекс точки: {st.index("8")}')   #   если через .index пытаться вывести индекс несуществующего элемента будет ошибка

print(st.replace("Это", "Та"))   #   замена элементов "Это" на "Та"

print(st.replace("о", "" ))   #   удалены все буквы "о"

print(st.count("о"))   #   подсчет количества вхождений символа "о" в строку

# s = "Мои питомцы: кошка Сима, кошка Рита, кот Кекс"
# print(f'У меня {s.count("кошка")} кошки')

s = "Имена сотрудников: Артём Иванов, Егор Нестеров, Артём Филатов, Артём Синицын"
print(s)
print(f"Индекс двоеточия: {s.index(":")}")
print(f'В нашем отделе {s.count("Артём")} Артёма')

print(s.split())   #   список из строки
print(s.strip())

t = "  Это тестовая строка текста.  "
print(t)
print(t.strip())   #   удаление пробелов

a = "ЗАГЛАВНЫЕ БУКВЫ"
print(a.lstrip())
print(a.lower())   #   все буквы маленькие

print(a.upper())   #   все буквы заглавные

print(a.capitalize())   #   заглавная только первая буква

t = "LADA Granta"
print(t.startswith("LADA"))
if t.startswith("LADA"):   #   проверка первых символов
    print("Это автомобиль марки LADA")

print(t.endswith("a"))   #   проверка последних символов

n = "65 см"
if n.endswith("мм") :
    print("Размер в мм")
elif n.endswith("см") :
    print("Размер в см")
else :
    print("ХЗ в чем этот размер")

print("С новым\nгодом")   #   перенос текста на новую строку

# fio = input("Введите ФИО: ")
# print(fio.replace(" ","\n"))   #   замена пробелов между словами переносами на новую строку#



# fio = input('Введи ФИО: ')
# f, i, o = fio.split()
# print(f'Фамилия: {f}\nИмя: {i}\nОтчество: {o}')
#
# fio = input("Введите ФИО: ")
# f, i, o = fio.split()
# s = f"| {f} | {i} | {o} |"
# print(s)


# fio = input("Введите ФИО: ")
# f, i, o = fio.split()
# s = f"| {f} | {i} | {o} |"
# print(s)
# print(f'| {f} | {i} | {o} |')


fio = input("Введите ФИО: ")
f, i, o = fio.split()
s = f"| {f} | {i} | {o} |"
print("-" * 5)   #   печатается 5 дефисов
print(s)
print("-" * len(s))   #   печатается количество дефисов равное длине строки



