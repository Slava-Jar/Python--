words = ["море", "солнце", "майка", "отпуск"]

a_words = [i for i in words if i.startswith('м')]

print(a_words)

b = [i for i in words if i.endswith('е')]

print(b)