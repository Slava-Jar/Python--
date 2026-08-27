lst = input("Введи элементы: ").split()
result = []

for x in lst:
    result.append(x)
    result.append(x)

print(result)

result_2 = [x for x in lst for _ in range(3)]
print(result_2)

print(result_3 := [x * 2 for x in lst])