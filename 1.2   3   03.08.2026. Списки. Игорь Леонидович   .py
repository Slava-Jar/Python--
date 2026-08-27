"""СПИСКИ (list)
тип данных - списки, структура данных - массив."""
from copy import deepcopy
# import copy

# print(__doc__)
"""Список - упорядоченный набор объектов"""
"""      0   1   2   3   4   """
nums = [22, 33, 44, 55, 99]
"""     -5  -4  -3  -2  -1   """
# print(nums[-3])
# print(nums[2])
# print(nums[-3:0:-1])
# print(nums[2:-5:-1])
# print(nums[2::-1])
#
# print(nums[2:])
# print(nums[::-1])  # реверсивный вывод информации
# nums = [20, 30, [40, 50]]
# s = nums
# s = nums.copy()
# s = nums[:]
# s = deepcopy(nums)
# s = copy.deepcopy(nums)
# nums[0] = 200
# nums[-1][0] = 400
# print(nums)
# print(id(nums))
# print(id(s))
# print(s)
# nums[:3] = 10, 20, 30
# print(nums)

ls = [10, 'Dasha', 5.45, True, [67,'Andre']]
lst = [['Masha', 18], ['Dasha', 22]]
name = ['Masha', 'Dasha']
age = [18, 22]
print(name[1], age[1])

nums = [55, 33, 44, 99, 77]
print(id(nums))
nums.append(100)  # временная сложность O(1) - константная
nums.insert(3, 200)  # временная сложность O(n) - линейная
nums.extend([1, 2])
# nums += [1, 2]
# nums = nums + [1, 2]

nums.pop()  # удаляет последний элемент списка временная сложность O(1) - константная
n = nums.pop()
# del n
nn = nums.pop(3)
# while 55 in nums:
#     nums.remove(55)
nums.remove(100)
print(nums.index(55))
print(nums.count(55))
print(sum(nums))
print(max(nums))
print(min(nums))
nums.reverse()
nums.sort(reverse=True)

print(id(nums))
print(nums)
# print('n ==', n, 'nn ==', nn)
print(len(nums))

nums = []
n = 0
while  n != -273:
    n = float(input('> '))
    nums.append(n)
nums.pop()

print(f'min = {min(nums)}\nmax = {max(nums)}\nmean = {sum(nums)/len(nums):.2f}')
print(nums)
