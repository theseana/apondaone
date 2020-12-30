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

l1 = tk.Label(root, text='Username:')
l1.pack()

e1 = tk.Entry(root)
e1.pack()

l2 = tk.Label(root, text='Password:')
l2.pack()

e2 = tk.Entry(root)
e2.pack()

b1 = tk.Button(root, text='Login', command=login)
b1.pack()

root.mainloop()