import tkinter as tk
from tkinter.constants import LEFT, RIGHT, X 


def register():
    n = name.get()
    l = last.get()
    p = phone.get()
    template = f"""
First Name: {n}
Last Name:  {l}
Phone:      {p}
---------------
"""
    file = open('athlete.txt', 'a')
    file.write(template)
    file.close()
    
root = tk.Tk()
f1 = tk.Frame(root)
tk.Label(f1, text='Name').pack(side=LEFT)
name = tk.StringVar()
tk.Entry(f1, textvariable=name).pack()

f2 = tk.Frame(root)
tk.Label(f2, text='Last').pack(side=LEFT)
last = tk.StringVar()
tk.Entry(f2, textvariable=last).pack()

f3 = tk.Frame(root)
tk.Label(f3, text='Phone').pack(side=LEFT)
phone = tk.StringVar()
tk.Entry(f3, textvariable=phone).pack()

f1.pack()
f2.pack()
f3.pack()

tk.Button(root, text='Register', command=register).pack()

root.mainloop()