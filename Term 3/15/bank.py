import tkinter as tk
from tkinter import ttk
import json
import hashlib
import datetime


def now():
    dt = datetime.datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def sha(password):
    hash = hashlib.sha1(password.encode('utf-8'))
    return hash.hexdigest()


def write_json(file_path, data):
    with open(file_path, 'w') as names:
        json.dump(data, names, indent=4)


def read_json(file_path):
    with open(file_path, 'r') as names:
        return json.load(names)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$ Register Button $$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
def confirm():
    info = {}
    info['username'] = username_r.get()
    info['password'] = sha(password_r.get())
    info['created_at'] = now()
    info['card_number'] = new_card_number()
    info['balance'] = 10000
    names_json = read_json('names.json')
    names_json.append(info)
    write_json('names.json', names_json)
        

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
