# print((n := int(input('Введите n '))) + n % 10)  #  в выражении нельзя присваивать значения поэтому используется := моржовая операция


# x = 10
# y = 10
#
# if x < y :
#     print('x < y')
# elif x > y :
#     print('x > y')
# else :
#     print ('x = y')

h = float(input('Введите время суток: '))
if h >= 4 and h <= 12 :
    print("Утро")
elif 12 <= h <= 17 :
    print('День')
elif h >= 17 and h < 24 :
    print('Вечер')
elif h >= 0 and h < 4 or h == 24 :
    print("Ночь")
else :
    print("Время указано неверно")

