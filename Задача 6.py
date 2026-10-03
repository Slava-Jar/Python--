from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


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