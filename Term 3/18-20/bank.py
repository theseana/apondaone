import tkinter as tk
from tkinter import Message, ttk
import json
import hashlib
import datetime
import random
from tkinter import messagebox


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


def new_card_number():
    names = read_json('names.json')
    if names:
        return names[-1]['card_number'] + random.randint(1000, 9999)
    else:
        return random.randint(6000000000000000, 7000000000000000)


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
    messagebox.showinfo(title='Success!',message='You registed successfully!')
    username_r.set('')
    password_r.set('')
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$ Login Button $$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
def log_in():
    global person
    names = read_json('names.json')
    for name in names:
        if name['username'] == username_l.get():
            if name['password'] == sha(password_l.get()):
                root.withdraw()
                menu.deiconify()
                person = name
                messagebox.showinfo(title='Success!',message='You Loged-in Successfully!')
                return None
    messagebox.showinfo(title='Failed!',message='Username or Password is invalid!') 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Withdraw $$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
def withdraw():
    def withdrawal():
        global person
        amount = withdraw_amount.get()
        persons = read_json('names.json')
        for p in persons:
            if p["username"] == person["username"]:
                if p["balance"] > amount:
    top = tk.Toplevel()
    withdraw_amount = tk.IntVar()
    tk.Entry(top, cnf=conf, textvariable=withdraw_amount).grid(row=0, column=0)
    tk.Button(top, text='Withdraw', cnf=conf, command=withdrawal).grid(row=1, column=0)
    tk.Button(top, text='Close', cnf=conf, command=top.destroy).grid(row=2, column=0)
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Transfer $$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
def transfer():
    pass
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Balance $$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
def balance():
    top = tk.Toplevel()
    now = datetime.datetime.now()
    msg = now.strftime('%Y-%m-%d\n') + now.strftime('%H:%M:%S')
    tk.Label(top, text=msg, cnf=conf).grid(row=0, column=0)
    msg1 = 'Your balance:\n' + str(person['balance'])
    tk.Label(top, text=msg1, cnf=conf).grid(row=1, column=0)
    tk.Button(top, text='Close', cnf=conf, command=top.destroy).grid(row=2, column=0)
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$ Change Pass $$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
def change_pass():
    pass

root = tk.Tk()
conf = {
    'font': ('times', 25)
}
person = None
menu = tk.Toplevel()
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
tk.Entry(register, textvariable=password_r, show="*").grid(row=1, column=1)

tk.Button(register, text='Register', command=confirm).grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E)
tk.Button(register, text='Cancel', command=root.destroy).grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E)
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Login $$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
tk.Label(login, text="Username").grid(row=0, column=0)
username_l = tk.StringVar()
tk.Entry(login, textvariable=username_l).grid(row=0, column=1)

tk.Label(login, text="Password").grid(row=1, column=0)
password_l = tk.StringVar()
tk.Entry(login, textvariable=password_l, show="*").grid(row=1, column=1)

tk.Button(login, text='Login', command=log_in).grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E)
tk.Button(login, text='Cancel', command=root.destroy).grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E)
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Menu $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
tk.Button(menu, text='Balance', cnf=conf, command=balance).grid(row=0, column=0)
tk.Button(menu, text='Withdraw', cnf=conf, command=withdraw).grid(row=0, column=1)
tk.Button(menu, text='Transfer', cnf=conf, command=transfer).grid(row=1, column=0)
tk.Button(menu, text='Change Password', cnf=conf, command=change_pass).grid(row=1, column=1)
menu.withdraw()
root.mainloop()
