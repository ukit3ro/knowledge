import tkinter as tk
from tkinter import ttk, filedialog
import os

def save_data():
    time = time_var.get()
    order = order_var.get()
    min_liq = int(min_liq_entry.get())
    max_liq = int(max_liq_entry.get())
    market_cap = int(market_cap_entry.get())
    min_age = int(min_age_entry.get())
    max_age = int(max_age_entry.get())
    volume = int(volume_entry.get())
    circle = int(circle_cap_entry.get())

    data = time +'.'+order + '.'+str(min_liq) + '.'+str(max_liq) + '.'+str(market_cap)\
        +'.'+str(min_age) + '.'+str(max_age) +  '.'+str(volume) + '.'+str(circle)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(script_dir, 'data.txt')

    with open(data_file, "w") as file:
        file.write(str(data))

app = tk.Tk()
app.title("Data Collector")

time_var = tk.StringVar()
order_var = tk.StringVar()

ttk.Label(app, text="Временной отрезок:").grid(row=0, column=0, sticky="w")
ttk.Combobox(app, textvariable=time_var, values=["M5", "H1", "H6", "H24"]).grid(row=0, column=1)

ttk.Label(app, text="Порядок сортировки:").grid(row=1, column=0, sticky="w")
ttk.Combobox(app, textvariable=order_var, values=["desc", "asc"]).grid(row=1, column=1)

ttk.Label(app, text="Минимальная ликвидность:").grid(row=2, column=0, sticky="w")
min_liq_entry = ttk.Entry(app)
min_liq_entry.grid(row=2, column=1)

ttk.Label(app, text="Максимальная ликвидность:").grid(row=3, column=0, sticky="w")
max_liq_entry = ttk.Entry(app)
max_liq_entry.grid(row=3, column=1)

ttk.Label(app, text="Market Cap:").grid(row=4, column=0, sticky="w")
market_cap_entry = ttk.Entry(app)
market_cap_entry.grid(row=4, column=1)

ttk.Label(app, text="Минимальный возраст в часах:").grid(row=5, column=0, sticky="w")
min_age_entry = ttk.Entry(app)
min_age_entry.grid(row=5, column=1)

ttk.Label(app, text="Максимальный возраст в часах:").grid(row=6, column=0, sticky="w")
max_age_entry = ttk.Entry(app)
max_age_entry.grid(row=6, column=1)

ttk.Label(app, text="Капитализация токена за 24 часа:").grid(row=7, column=0, sticky="w")
volume_entry = ttk.Entry(app)
volume_entry.grid(row=7, column=1)

ttk.Label(app, text="%Оборота").grid(row=8, column=0, sticky="w")
circle_cap_entry = ttk.Entry(app)
circle_cap_entry.grid(row=8, column=1)


ttk.Button(app, text="Сохранить введённые", command=save_data).grid(row=9, column=0, columnspan=2)
ttk.Button(app, text="Поиск токенов", command=lambda:app.quit()).grid(row=10, column=0, columnspan=2)

app.mainloop()