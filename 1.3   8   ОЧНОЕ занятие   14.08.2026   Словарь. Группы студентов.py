"""
Задача . Разделить студентов по группам

students = [ ("Anna", "A"), ("Ivan", "B"), ("Maria", "A"), ("Petr", "B"), ("Olga", "C") ]

"""


# Создаём список кортежей: каждый кортеж - это пара (имя студента, его группа/оценка)
students = [ ("Anna", "A"), ("Ivan", "B"), ("Maria", "A"), ("Petr", "B"), ("Olga", "C") ]

# A = []
# B = []
# C = []
#
# for i in students:
#     if "A" in i :
#         A.append(i)
#     elif "B" in i :
#         B.append(i)
#     elif "C" in i :
#         C.append(i)
# print(*A, sep="\n")
# print(*B, sep="\n")
# print(*C, sep="\n")

print()

# Создаём пустой словарь, куда будем собирать списки студентов по группам
groups = {}
for name, group in students:     #   Проходим по каждому кортежу в списке students; name - имя, group — группа
    if group not in groups:      #   Если такой группы (ключа) ещё нет в словаре groups, нужно сначала создать для неё пустой список
        groups[group] = []       #   Создаём ключ group и присваиваем ему пустой список [], чтобы потом можно было добавлять имена
    groups[group].append(name)   #   Добавляем имя студента в список, соответствующий его группе
print(groups)
