from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def update_b_label(event):
    code = base_combobox.get()
    b_label.config(text=cryptos[code])


def update_t_label(event):
    code = target_combobox.get()
    t_label.config(text=cryptos[code])


def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()

    if target_code and base_code:
        try:
            # 1. Формируем запрос: получаем цены обеих монет к USD
            # ids: перечисляем через запятую
            # vs_currencies: жестко ставим 'usd', так как API не дает прямой кросс-курс
            url = 'https://api.coingecko.com/api/v3/simple/price'
            params = {
                'ids': f'{base_code},{target_code}',
                'vs_currencies': 'usd'
            }

            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            # 2. Проверяем, пришли ли данные для обеих монет
            if base_code not in data or target_code not in data:
                mb.showerror("Ошибка", "Не удалось получить данные от API")
                return

            # 3. Получаем курсы к доллару
            base_rate_usd = data[base_code]['usd']
            target_rate_usd = data[target_code]['usd']

            # 4. Рассчитываем кросс-курс: (Цена Базы в USD) / (Цена Цели в USD)
            # Пример: BTC стоит 27000 USD, USDT стоит 1 USD. Курс = 27000 / 1 = 27000
            exchange_rate = base_rate_usd / target_rate_usd

            base_name = cryptos[base_code]
            target_name = cryptos[target_code]

            mb.showinfo("Курс обмена",
                        f"Курс: {exchange_rate:.6f} {target_name} за 1 {base_name}")

        except requests.exceptions.HTTPError as e:
            mb.showerror("Ошибка HTTP", f"Ошибка API: {e}")
        except requests.exceptions.RequestException as e:
            mb.showerror("Ошибка сети", f"Нет соединения: {e}")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла непредвиденная ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите криптовалюты из списка")


# Словарь: ключ = ID для CoinGecko API (lowercase), значение = отображаемое название
cryptos = {
    "bitcoin": "Биткоин (BTC)",
    "ethereum": "Эфириум (ETH)",
    "tether": "Tether (USDT)",
    "bnb": "BNB (BNB)",
    "ripple": "Ripple (XRP)",
    "cardano": "Cardano (ADA)",
    "solana": "Solana (SOL)",
    "dogecoin": "Dogecoin (DOGE)",
    "polkadot": "Polkadot (DOT)",
    "polygon": "Polygon (MATIC)"
}

# Создание интерфейса
window = Tk()
window.title("Курс обмена криптовалют")
window.geometry("360x300")

Label(text="Базовая криптовалюта:").pack(padx=10, pady=5)

base_combobox = ttk.Combobox(values=list(cryptos.keys()), state="readonly")
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Целевая криптовалюта:").pack(padx=10, pady=5)

target_combobox = ttk.Combobox(values=list(cryptos.keys()), state="readonly")
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()