
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на ноль"
    return x / y

def log(result):                                                          #   encoding="utf-8"
    with open("calculations.txt", "a") as file:
        file.write(result + "\n")                                                   #   добавлен перевод строки для читаемости


def show_history():
    try:
        with open("calculations.txt", "r") as file:                                 #   encoding="utf-8"
            lines = file.readlines()                                                #   Считываем все строки в список

        if lines:                                                                   # Если список не пустой
            print("\n=== ИСТОРИЯ ВЫЧИСЛЕНИЙ ===")
            for line in lines:
                print(line.strip())                                                 #   strip() убирает лишние пробелы и \n
            print("=== Конец истории ===")
        else:
            print("История пуста. Начните вычисления!")

    except FileNotFoundError:
        print("Файл с историей ещё не создан. Начните вычисления!")


print("Выберите операцию: ")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Показать историю вычислений")

choice = input("Введите номер операции (1/2/3/4/5): ")


if choice == '1':
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    r = f"Результат: {num1} + {num2} = {add(num1, num2)}"
    print(r)
    log(r)
elif choice == '2':
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    r = f"Результат: {num1} - {num2} = {subtract(num1, num2)}"
    print(r)
    log(r)
elif choice == '3':
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    r = f"Результат: {num1} * {num2} = {multiply(num1, num2)}"
    print(r)
    log(r)
elif choice == '4':
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    r = f"Результат: {num1} / {num2} = {divide(num1, num2)}"
    print(r)
    log(r)
elif choice == '5':
    show_history()
else:
    print("Неверный ввод")
