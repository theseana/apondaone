import tkinter as tk
from tkinter import ttk

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$ Register Button $$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
def confirm():
    info = {}
    info['username'] = username_r.get()
    info['password'] = username_r.get()
    info['created_at'] = username_r.get()
    info['card_number'] = username_r.get()
    info['balance'] = 10000




root = tk.Tk()
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$ Notebook $$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
note = ttk.Notebook()
note.grid(row=0, column=0)

register = tk.Frame(note)
login = tk.Frame(note)

note.add(register, text='Register')
note.add(login, text='Log-in')
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$ Register $$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
tk.Label(register, text="Username").grid(row=0, column=0)
username_r = tk.StringVar()
tk.Entry(register, textvariable=username_r).grid(row=0, column=1)

tk.Label(register, text="Password").grid(row=1, column=0)
password_r = tk.StringVar()
tk.Entry(register, textvariable=password_r).grid(row=1, column=1)

tk.Button(register, text='Register', command=confirm).grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E)
tk.Button(register, text='Cancel', command=root.destroy).grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E)

root.mainloop()
# {
#     "username": '',
#     "password": 'password hashed',
#     "created_at": 'now',
#     "card_number": 124578878787,
#     "balance": 1000
# }
