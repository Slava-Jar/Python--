"""
Работа со словарем.
user = { "name": "Anna", "age": 20, "city": "Moscow" }
получить имя и возраст;
изменить город;
добавить профессию;
удалить возраст;
проверить наличие ключа "email";
вывести все ключи и значения.

"""

user = { "name": "Anna", "age": 20, "city": "Moscow" }
print(f'Имя: {user.get("name")}, возраст: {user["age"]}')
user.update({"city" : "Астана"})                              #   user["city"] = "Астана"
user.update({"profession" : "инженер"})
print(f'Город: {user.get("city")}')
print(f'Профессия: {user.get("profession")}')
print(f'Email: {user.get("email")}')
if "email" in user:
    print(f'Email имеется')
else:
    print(f'Email отсутствует')
print(user.items())
for key, value in user.items():
    print(f'{key} : {value}')

