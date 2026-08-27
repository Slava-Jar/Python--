"""
Дана строка. Создать словарь подсчета слов.
 text = "Осень в Москве, Зима в Москве, Весна в Москве, Лето в Москве. Времена года!"
Создать словарь подсчета слов: counts = {}

"""
text = "Осень в Москве, Зима в Москве, Весна в Москве, Лето в Москве. Времена года!"
text_1 =text.replace(",","").replace(".", "").replace("!", "").lower().split()
print(text_1)

counts = {}

for i in text_1:
    item = text_1.count("i")
    if i in counts:
        counts[i] += 1
        # print(counts)
    else:
        counts[i] = 1
        # print(counts)
print(counts)

counts_1 = {}
for i in text_1:
    key = i
    value = text_1.count(i)
    counts_1.update({key:value})
print(counts_1)