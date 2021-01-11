import tkinter as tk
from tkinter import ttk
import time
import datetime


def to_time(seconds):
    return str(datetime.timedelta(seconds=seconds))


def start(a, b, c):
    seconds = spin1.get()
    string = to_time(seconds)
    timer1.set(string)


def start2(a, b, c):
    seconds = spin2.get()
    string = to_time(seconds)
    timer2.set(string)

root = tk.Tk()


timer1 = tk.StringVar()
tk.Label(root, textvariable=timer1).grid(row=0, column=0)
spin1 = tk.IntVar()
spin1.trace('w', start)
tk.Spinbox(root, textvariable=spin1, from_=0, to=36000, width=10).grid(row=1, column=0)

tk.Button(root, text='Start').grid(row=2, column=0)

timer2 = tk.StringVar()
tk.Label(root, textvariable=timer2).grid(row=0, column=1)
spin2 = tk.IntVar()
spin2.trace('w', start2)
tk.Spinbox(root, textvariable=spin2, from_=0, to=36000, width=10).grid(row=1, column=1)

tk.Button(root, text='Start').grid(row=2, column=1)

root.mainloop()