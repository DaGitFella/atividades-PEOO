import tkinter as tk
from tkinter import messagebox
import time 

def callback():
    msg = messagebox.showinfo("Hello python", "Hello World")

def error():
    msg = messagebox.showerror("error", "You're in danger!")

def warning():
    seconds = 10
    while seconds > 0:
        msg = messagebox.showwarning(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
