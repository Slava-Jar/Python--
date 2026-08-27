
"""   Проверка возраста

# age = int(input("Введите возраст: "))
# if age >= 18 :
#     print('Доступ разрешён')
# else :
#     print("Доступ запрещен")

"""



"""   Банкомат   

my_count = 1500

query = int(input("Введите сумму: "))

if query <= my_count :
    res = my_count - query
    print("Остаток на счете ", res)
else :
    print("Недостаточно средств")

"""



"""   Сложение или вычитание   

a, b = map(int, input("Введите два числа через пробел: ").split())
c = input("Выберите операцию \"+\", \"-\", \"*\" или \"/\": ")

if c == "+" :
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/" :
    if b == 0 :
        print("На ноль делить нельзя")
    else :
        print(a/b)

"""



"""   Логин / Пароль   

log = 111
pas = 222

while True :
    a = int(input("Введите логин: "))
    b = int(input("Введите пароль: "))
    if a == log and b == pas :
        print("Вход в аккаунт")
        break
    else:
        print("Неверный логин или пароль")

"""



"""   Логин / пароль для 10 пользователей   

log = [00, 11, 22, 33, 44, 55, 66, 77, 88, 99]
pas = [00, 11, 22, 33, 44, 55, 66, 77, 88, 99]

user_cnt = 0
try_cnt = 0

# while user_cnt < 10 and try_cnt < 3 ???

while try_cnt < 3 :
    try_cnt += 1
    a = int(input("Введи логин: "))
    b = int(input("Введите пароль: "))
    if a in log and b in pas :
        print("Вход в аккаунт")
        break
    else :
        print("Повторите ввод")
else :
    print("Вы исчерпали попытки ввода")

"""



"""   Логин / пароль для 10 пользователей. Версия преподавателя   

password = 11
login = "22"

for i in range(1, 11) :
    print(f'User {i}')

    your_login = input("Введите логин: ").capitalize()
    if your_login == login :

        attempt=0
        while attempt < 3 :

            your_password = int(input("Введите пароль: "))
            if your_password == password and your_login == login :
                print("Доступ в систему открыт")
                break

            else :
                print("Ошибка. Повторите ввод пароля")
                attempt += 1

            if attempt == 3 :
                print("Аккаунт заблокирован")
    else :
        print("Такого пользователя нет")
        
"""



"""   Логин / пароль для нескольких пользователей. Проверка наличия заглавных букв, цифр и длины"""
login = [11, 22, 33]

for iteration in range(3) :
    log = int(input("Введите логин: "))

    if log in login :


        has_digit = False
        has_upper = False

        for attempt in range(3) :

            pas = input("Введите пароль: ")
            attempt += 1
            if attempt >= 3 :
                print("Аккаунт заблокирован")
                break

            for i in pas :
                if i.isdigit() :
                    has_digit = True

                if i.isupper() :
                    has_upper = True

            if has_digit and has_upper and len(pas) >= 8 :
                print("Пароль принят")
                break
            else :
                print("Длина пароля должна быть не менее 8 символов. Пароль должен содержать цифру и заглавную букву")

    else:
        print("Такого пользователя нет")



