"""
Задача.
Учёт товаров на складе
warehouse = { "laptop": {"price": 80000, "quantity": 5}, "mouse": {"price": 1500, "quantity": 20}, "keyboard": {"price": 4000, "quantity": 10} }

Программа должна уметь:
1 — Показать товары
2 — Добавить товар
3 — Продать товар
4 — Пополнить остаток
5 — Изменить цену
6 — Общая стоимость склада
7 — Самый дорогой товар
8 — Товары с остатком меньше 3
0 — Выход
"""



warehouse = { "laptop": {"price": 80000, "quantity": 2}, "mouse": {"price": 150000000000, "quantity": 20}, "keyboard": {"price": 4000, "quantity": 10} }

while True:
    print(f'\n')
    print(f'1 - Показать товары.')
    print(f'2 - Добавить товар.')
    print(f'3 - Продать товар.')
    print(f'4 - Пополнить остаток.')
    print(f'5 - Изменить цену.')
    print(f'6 - Общая стоимость склада.')
    print(f'7 - Самый дорогой товар.')
    print(f'8 - Товары с остатком менее 3.')
    print(f'0 - Выход.')


    choice = input("Выберите действие: ")
    if choice == "1":                                                                                   #   1. Показать товары.
        for name, produkt in warehouse.items():
            print(f'Товар: {name}, цена: {produkt['price']} р., остаток: {produkt['quantity']} шт.')


    elif choice == "2":                                                                                 #   2. Добавить товар
        while True:
            name_ = input("Введите наименование товара или \"Стоп\" для выхода: ")
            if name_ == "Стоп":
                break
            elif name_ in warehouse:
                print("Товар уже есть в списке")
                break
            price_ = int(input("Введите цену: "))
            quantity_ = int(input("Введите количество единиц: "))
            new_item = {'price': price_, 'quantity': quantity_}
            warehouse[name_] = new_item
            print(f'Товар "{name_}" добавлен. Цена: {price_} р., количество: {quantity_} шт.')


    elif choice == "3":                                                                                 #   3. Продать товар
        name = input(f'Введите наименование товара: ')
        if name not in warehouse:
            print("Товара нет в списке")
        else:
            quantity_ = int(input("Введите количество: "))
            if warehouse[name]['quantity'] >= quantity_:
                warehouse[name]["quantity"] -= quantity_
                print("Товар продан.")
                print(f'Остаток товара: {warehouse[name]['quantity']}')
            else:
                print("Недостаточное количество товара.")
                print(f'В наличии: {warehouse[name]['quantity']} шт.')


    elif choice == "4":                                                                                  #   4. Пополнить остаток
        while True:
            name = input("Введите наименование товара или \"Стоп\" для выхода: ")
            if name == "Стоп":
                break
            elif name not in warehouse:
                print(f'Товар "{name}" отсутствует')
            else:
                quantity = int(input("Введите добавляемое количество: "))
                warehouse[name]["quantity"] += quantity
                print(f'Остаток товара обновлен. В наличии {warehouse[name]['quantity']} шт.')


    elif choice == "5":                                                                                  #   5. Изменить цену
        while True:
            name = input("Введите наименование товара или \"Стоп\" для выхода: ")
            if name == "Стоп":
                break
            elif name not in warehouse:
                print(f'Товар "{name}" отсутствует')
            else:
                new_price = int(input("Введите новую цену: "))
                warehouse[name]["price"] = new_price
                print(f'Цена позиции "{name}" изменена. Новая цена {warehouse[name]['price']} р.')


    elif choice == "6":                                                                                  #   6. Общая стоимость склада
        total_coast = 0
        for name, price in warehouse.items():
            item_total_cost = int(warehouse[name]["price"] * warehouse[name]["quantity"])
            total_coast += item_total_cost
            print(f'Общая стоимость позиции {name}: {item_total_cost} р.')
        print(f'Общая стоимость склада: {total_coast} р.')


    elif choice == "7":                                                                                  #   7. Самый дорогой товар
        max_cost_item = 0
        for name, price in warehouse.items():
            if warehouse[name]["price"] > max_cost_item:
                max_cost_item = warehouse[name]["price"]
                print(f'Самый дорогой товар "{name}", цена: {max_cost_item} р.')


    elif choice == "8":                                                                                  #   6. Товары с остатком меньше 3
        flag = False
        for name, price in warehouse.items():
            if warehouse[name]["quantity"] < 3:
                print(f'Остаток товара "{name}" меньше 3 единиц.')
                flag = True
        if flag == False:
            print("На складе достаточное количество товара.")


    elif choice == "0":
        print("Выход.")
        break