import tkinter as tk
from tkinter import ttk

def get_user_input():
    values = {}
    values["time"] = time_entry.get()
    values["order"] = order_entry.get()
    values["minLiqQ"] = minLiqQ_entry.get()
    values["maxLiqQ"] = maxLiqQ_entry.get()
    values["marketCap"] = marketCap_entry.get()
    values["minAge"] = minAge_entry.get()
    values["maxAge"] = maxAge_entry.get()
    values["volume"] = volume_entry.get()
    
    with open("output.txt", "w") as f:
        f.write(str([values]))

root = tk.Tk()
root.title("Input Values")

time_label = tk.Label(root, text="Временной отрезок:")
time_label.grid(row=0, column=0)

time_entry = ttk.Entry(root)
time_entry.insert(0, "5 минут (М5), час(Н1), 6 часов(Н6), 24 часа(Н24)")
time_entry.grid(row=0, column=1)

order_label = tk.Label(root, text="Порядок сортировки:")
order_label.grid(row=1, column=0)

order_entry = ttk.Entry(root)
order_entry.insert(0, "восходящий(asc), нисходящий(desc)")
order_entry.grid(row=1, column=1)

minLiqQ_label = tk.Label(root, text="Минимальная ликвидность:")
minLiqQ_label.grid(row=2, column=0)

minLiqQ_entry = ttk.Entry(root)
minLiqQ_entry.grid(row=2, column=1)

maxLiqQ_label = tk.Label(root, text="Максимальная ликвидность:")
maxLiqQ_label.grid(row=3, column=0)

maxLiqQ_entry = ttk.Entry(root)
maxLiqQ_entry.grid(row=3, column=1)

marketCap_label = tk.Label(root, text="Market Cap:")
marketCap_label.grid(row=4, column=0)

marketCap_entry = ttk.Entry(root)
marketCap_entry.grid(row=4, column=1)

minAge_label = tk.Label(root, text="Минимальный возраст в часах:")
minAge_label.grid(row=5, column=0)

minAge_entry = ttk.Entry(root)
minAge_entry.grid(row=5, column=1)

maxAge_label = tk.Label(root, text="Максимальный возраст в часах:")
maxAge_label.grid(row=6, column=0)

maxAge_entry = ttk.Entry(root)
maxAge_entry.grid(row=6, column=1)

volume_label = tk.Label(root, text="Капитализация токена за 24 часа:")
volume_label.grid(row=7, column=0)

volume_entry = ttk.Entry(root)
volume_entry.grid(row=7, column=1)

get_input_button = tk.Button(root, text="Получить значения", command=get_user_input)
get_input_button.grid(row=8, columnspan=2)

root.mainloop()