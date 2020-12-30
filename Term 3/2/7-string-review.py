import tkinter as tk 

def say():
    print(name.get())

root = tk.Tk()

name = tk.StringVar()
tk.Entry(root, textvariable=name)
b = tk.Button(root, text='Say my name!', command=say)
b.pack()
root.mainloop()