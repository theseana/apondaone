import tkinter as tk
import time
import datetime
from threading import Thread


def time_format(seconds):
    return str(datetime.timedelta(seconds=seconds))

def timer(button):
    global state
    if button:
        state = True
    else:
        state = False

def updater():
    while True:
        if state:
            t['right'] -= 1
            right_timer.set(time_format(t['right']))
        else:
            t['left'] -= 1
            left_timer.set(time_format(t['left']))
        time.sleep(1)



root = tk.Tk()

t = {
    'left': 1200,
    'right': 1200,
}
state = True

left_timer = tk.StringVar()
left_timer.set('0:20:00')
tk.Label(root, textvariable=left_timer, font=('times', 20)).grid(row=0, column=0)
tk.Button(root, text='press', command=lambda: timer(1)).grid(row=1, column=0)

right_timer = tk.StringVar()
right_timer.set('0:20:00')
tk.Label(root, textvariable=right_timer, font=('times', 20)).grid(row=0, column=1)
tk.Button(root, text='press', command=lambda: timer(0)).grid(row=1, column=1)

update = Thread(target=updater)
update.start()

root.mainloop()