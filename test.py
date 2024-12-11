import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Функция синуса
def sinus(x):
    return np.sin(x * np.pi / 180)

# Пример данных
angles = np.linspace(-90, 90, 181)
y_values = sinus(angles)

# Создание основного окна
root = tk.Tk()
root.title("Синусоидальный график")

# Создание графика
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
ax.plot(angles, y_values, color='blue', linewidth=2)
ax.set_xlim(-90, 90)
ax.set_ylim(-1.1, 1.1)
ax.set_xlabel('Угол (°)')
ax.set_ylabel('Значение синуса')

# Создание canvas для отображения графика
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Отображение окна
root.mainloop()