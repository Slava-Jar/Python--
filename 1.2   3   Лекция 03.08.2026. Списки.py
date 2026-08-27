"""СПИСКИ (list)
тип данных - списки, структура данных - массив."""
from copy import deepcopy
# import copy

# print(__doc__)
"""Список - упорядоченный набор объектов"""
"""      0   1   2   3   4   """
nums = [22, 33, 44, 55, 99]
"""     -5  -4  -3  -2  -1   """
# # print(nums[-3])
# # print(nums[2])
# # print(nums[-3:0:-1])
# # print(nums[2:-5:-1])
# # print(nums[2::-1])
# #
# # print(nums[2:])
# # print(nums[::-1])  # реверсивный вывод информации
# nums = [20, 30, [40, 50]]
# # s = nums
# # s = nums.copy()
# # s = nums[:]
# s = deepcopy(nums)
# # s = copy.deepcopy(nums)
# nums[0] = 200
# nums[-1][0] = 400
# print(nums)
# print(id(nums))
# print(id(s))
# print(s)

# nums[:3] = 10, 20, 30
# print(nums)

# ls = [10, "Dasha", 5.45, True, [67, "Andre"]]
# lst = [["Masha", 18], ["Daasha", 22]]


nums[:3] = 10, 20, 30
print(id(nums))
nums.append(100)   #   временная сложность 0(1) - константная
print(nums)
print(id(nums))

nums.insert(0, 200)   #   временная сложность 0(1) - линейная
print(nums)
# nums.extend([1, 2])
print(nums)

nums += [1, 2]
print(nums)