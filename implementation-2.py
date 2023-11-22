import tkinter as tk
from functions import *

window = tk.Tk()
window.title("league of legends")
window.geometry("500x900")
window.resizable(False, False)

widgets = {
    "count": tk.Label(text=r"Let´s count", font=("Verdana", "32", "italic", "bold")),
    "msg": tk.Button(text=r"hello", command=callback, width=32),
    "error": tk.Button(text=r"error", command=error, width=32),
    "warning": tk.Button(text=r"WARNING!", command=warning, width=32),
    "exit": tk.Button(text=r"exit", command=exit, width=32),
    }

for widget in widgets:
    widgets[widget].pack()

window.mainloop()
