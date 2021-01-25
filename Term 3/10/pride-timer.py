import tkinter as tk
from threading import Thread
import datetime
import time


def format_time(number):
    return str(datetime.timedelta(seconds=number))


def reset():
    global seconds
    seconds = 0


def h():
    global seconds
    seconds += 3600
    if seconds > 86400:
        seconds -= 86400


def m():
    global seconds
    seconds += 60
    if seconds > 86400:
        seconds -= 86400


def counter():
    global seconds
    while True:
        seconds += 1
        form = format_time(seconds)
        if len(form) == 7:
            form = "0" + form
        timer.set(form)
        time.sleep(1)
        if seconds == 86400:
            seconds = 0

opt = {
    'bg': 'black',
    'fg': "white",
    'font': ("times", 10)
}

root = tk.Tk()
root.title('PRIDE TIMER')
root.config(bg="black")
seconds = 86350
timer = tk.StringVar()
tk.Label(root, cnf=opt, textvariable=timer, font=('times', 30)).grid(row=0, column=1, rowspan=3)
tk.Button(root, cnf=opt, text='H', command=h).grid(row=0, column=0, sticky=tk.W+tk.E)
tk.Button(root, cnf=opt, text='M', command=m).grid(row=1, column=0, sticky=tk.W+tk.E)
tk.Button(root, cnf=opt, text='RESET', command=reset).grid(row=2, column=0)

c = Thread(target=counter)
c.start()
root.mainloop()
