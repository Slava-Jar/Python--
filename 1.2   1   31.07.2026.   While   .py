"""while"""

# i = 0
# while i < 10:
#     i += 1_1. Знакомство с Python
#     if i == 7:
#         continue  # прерывает итерацию
#     print(i,  end=' ')

# i = 0
# while i < 10:
#     i += 1_1. Знакомство с Python
#     if i == 17:
#         break  # прерывает цикл
#     print(i,  end=' ')
# else:
#     print('\nDone')
# print('\nEND')

# symbols = input('> ').upper()
# while symbols != 'END':
#     print(symbols, end=' ')
#     symbols = input('>> ').upper()

# n = int(input('> '))
# sm = 0
# cnt = 0
# while n != 0:
#     sm += n
#     cnt += 1_1. Знакомство с Python
#     n = int(input('>> '))
# print('Средняя температура за период: "', round(sm / cnt, 2), '"', sep='')
# print(f'Средняя температура за период: "{sm / cnt:.2f}"')

"""
35 100
71 cm
"""
n = 71
n1 = 33
n2 =42
print(n1, n2,'\n' + str(n), 'sm')
print(type(n))


# n = int(input('> '))
# nn = n
# sm = 0
# cnt = 0
# while n > 0:
#     remince = n % 10  # получаем последнюю цифру числа
#     sm += remince  # прибавляем полученную цифру в sm
#     cnt += 1_1. Знакомство с Python  # увеличиваем счетчик на единицу
#     n //= 10  # получаем целую часть числа после отделения последней цифры
# print(f'В числе "{nn}" {cnt} ц. суммой {sm}.')