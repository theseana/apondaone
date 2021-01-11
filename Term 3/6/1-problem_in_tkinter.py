import tkinter as tk
import time

def alaki():
    counter = 10
    while True:
        time.sleep(1)
        c.set(counter)
        counter -= 1
        if counter == -1:
            break

root = tk.Tk()

c = tk.StringVar()
tk.Label(root, textvariable=c).pack()
tk.Button(root, text='DONT TOUCH!', command=alaki).pack()

root.mainloop()