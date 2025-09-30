import keyboard
import pyautogui
import time
import threading

# Флаг для управления потоком кликов
clicking = False

def click_loop():
    global clicking
    while True:
        if clicking:
            # Клик левой кнопкой мыши
            pyautogui.click(button='left')
            time.sleep(0.1)  # небольшая задержка между кликами
            # Клик правой кнопкой мыши
            pyautogui.click(button='right')
            time.sleep(0.1)
        else:
            time.sleep(0.1)  # чтобы не нагружать процессор

def toggle_clicking(e):
    global clicking
    if e.event_type == keyboard.KEY_DOWN and e.name == 'h':
        clicking = not clicking
        print("Автокликер запущен!" if clicking else "Автокликер остановлен.")

# Запуск потока для кликов
thread = threading.Thread(target=click_loop)
thread.daemon = True
thread.start()

# Подписка на событие нажатия клавиши 'H'
keyboard.hook(toggle_clicking)

print("Нажмите 'H' для запуска/остановки автокликера. Нажмите Ctrl+C для выхода.")
try:
    # Бесконечный цикл, чтобы программа не завершалась
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Программа завершена.")