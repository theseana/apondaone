import tkinter as tk
from tkinter import messagebox

def login():
    u = e1.get()
    p = e2.get()
    if u == username :
        if p == password:
            messagebox.showinfo(title='Successful Login',
                                   message='Welcome Back!')
        elif p == '':
            messagebox.showerror(title='Enter Password',
                                    message="You must entered a Password")
        else:
            messagebox.showerror(title='Wrong Password',
                                    message="You entered invalid Password")
    else:
        messagebox.showerror(title='Wrong Username',
                                    message="You entered invalid Username")

root = tk.Tk()

username = 'poulstar'
password = 'poulstar'

tk.Label(root, text='Username:').pack()
e1 = tk.StringVar()
tk.Entry(root, textvariable=e1).pack()

tk.Label(root, text='Password:').pack()
e2 = tk.StringVar()
tk.Entry(root, textvariable=e2).pack()

tk.Button(root, text='Login', command=login).pack()

root.mainloop()