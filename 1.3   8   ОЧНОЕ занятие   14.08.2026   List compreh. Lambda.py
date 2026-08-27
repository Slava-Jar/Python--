
"""
Задача 9. Функция для работы со списком.
Напишите функцию process_list(lst), которая:
1. Принимает список чисел.
2. Возвращает новый список, где все чётные числа заменены на их квадраты, а нечётные — на их кубы.
3. Обработайте случай, если на вход подан не список (выведите "Ошибка: аргумент не является списком").
4. Переписать через списковое включение.
5. Переписать через lambda функцию.

"""



# def process_list(lst):
#
#    try :
#     new_lst = []
#     for i in lst:
#         if i % 2 == 0:
#             new_lst.append(i**2)
#         else :
#             new_lst.append(i**3)
#     return new_lst
#
#    except Exception as e :
#        print(f'Ошибка {e}')
#
# print(process_list(['dfgerhb']))
# print(process_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

#   4. Переписать через списковое включение.
# def process_list(lst):
#     new_lst = [i**2 if i % 2 == 0 else i**3 for i in lst]
#     return new_lst
# print(process_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))



#   Списковое включение без функции
# lst = map(int, input("Введите числа: ").strip().split())
# new_lst = [i**2 if i % 2 == 0 else i**3 for i in lst ]
# print(new_lst)



#   5. Переписать через lambda функцию.
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# new_lst = list(map(lambda i: i ** 2 if i % 2 == 0 else i ** 3, lst))
# print(new_lst)



def process_list(lst):
    if isinstance(lst, list):
        new_lst = []
        for i in lst:
            if i % 2 == 0:
             new_lst.append(i**2)
            else:
                new_lst.append(i**3)
        return new_lst
    else:
        return("Ошибка! Аргумент не является списком")
print(process_list([1,2,3,4,5]))
print(process_list("ertgdhrndhjdtyh"))
