import tkinter as tk
import ctypes
import pyautogui

center_res = ctypes.windll.user32.GetSystemMetrics(0)/2, ctypes.windll.user32.GetSystemMetrics(1)/2

window = tk.Tk()
window.attributes('-fullscreen', True)

label = tk.Label(window, text="Введи ключ и нажми ctrl+c", font=("Arial", 24))
label.place(relx=.5, rely=.45, anchor="c")


entry = tk.Entry(window, font=("Arial", 18))
entry.place(relx=.5, rely=.5, anchor="c")

while True:
  pyautogui.moveTo(center_res)
  window.update_idletasks()
  window.update()
  window.after(100)

