import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)


def update_base_2_label(event):
    code = base_2_combobox.get()
    name = currencies[code]
    base_2_label.config(text=name)


def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    currency_label.config(text=name)


def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()
    base_2_code = base_2_combobox.get()
    if target_code and base_code and base_2_code:
        try:

            result = requests.get(f"https://open.er-api.com/v6/latest/{base_code}")
            result.raise_for_status()
            data = result.json()

            result_2 = requests.get(f"https://open.er-api.com/v6/latest/{base_2_code}")
            result_2.raise_for_status()
            data_2 = result_2.json()

            if target_code in data['rates'] and target_code in data_2['rates']:
                exchange_rate = data['rates'][target_code]
                exchange_rate_2 = data_2['rates'][target_code]
                base = currencies[base_code]
                base_2 = currencies[base_2_code]
                target = currencies[target_code]

                mb.showinfo('Курс обмена',
                            f'Курс\n'
                            f'{exchange_rate:.1f} {target} за 1 {base},\n'
                            f'{exchange_rate_2:.1f} {target} за 1 {base_2}')
            else:
                mb.showerror('Ошибка', f'Валюта {target_code} не найдена')

        except Exception as e:
            mb.showerror('Ошибка', f'error 400 {e}')

currencies = {
    "USD": "Доллар США",
    "EUR": "Евро",
    "CNY": "Юань",
    "RUB": "Российский рубль",
}

pop_curr = ['EUR', 'USD', 'RUB', 'CNY']

root = Tk()
root.title("Курс валют ")
root.geometry("300x500")

Label(text='Базовая валюта').pack(pady=10, padx=10)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack()

base_label = ttk.Label()
base_label.pack(pady=10, padx=10)
base_combobox.bind("<<ComboboxSelected>>", update_base_label)

Label(text='Вторая базовая валюта').pack(pady=10, padx=10)
base_2_combobox = ttk.Combobox(values=list(currencies.keys()))
base_2_combobox.pack()

base_2_label = ttk.Label()
base_2_label.pack(pady=10, padx=10)
base_2_combobox.bind("<<ComboboxSelected>>", update_base_2_label)

Label(text='Целевая валюта').pack(pady=10, padx=10)
target_combobox = ttk.Combobox(values=list(currencies))
target_combobox.pack()

currency_label = ttk.Label()
currency_label.pack(pady=10, padx=10)
target_combobox.bind("<<ComboboxSelected>>", update_currency_label)

button = Button(text='Получить курс', command=exchange)
button.pack()

root.mainloop()