import tkinter as tk
from tkinter import Message, ttk
import json
import hashlib
import datetime
import random
from tkinter import messagebox
from tkinter.font import names


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

def get_destination(card):
    names = read_json('names.json')
    for name in names:
        if str(name["card_number"]) == card:
            return names.index(name)
    return None

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$ Register Button $$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
def confirm(a=None):
    if note.tab(note.select(), "text") == "Register":
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
def log_in(a=None):
    if note.tab(note.select(), "text") == "Log-in":
        global person, ind
        names = read_json('names.json')
        for name in names:
            
            if name['username'] == username_l.get():
                if name['password'] == sha(password_l.get()):
                    root.withdraw()
                    menu.deiconify()
                    person = name
                    messagebox.showinfo(title='Success!',message='You Loged-in Successfully!')
                    return None
            ind += 1
        messagebox.showinfo(title='Failed!',message='Username or Password is invalid!') 
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Withdraw $$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
def withdraw():
    def withdrawal():
        global person, ind
        amount = withdraw_amount.get()
        if person["balance"] > amount:
            names = read_json('names.json')
            names[ind]["balance"] -= amount
            write_json('names.json', names)
            messagebox.showinfo(title='Successfully Done',message='Withdraw successfull!')             
            top.withdraw()
        else:
            messagebox.showerror(title='Failed!',message='Not Enough MOney!') 
    top = tk.Toplevel()
    withdraw_amount = tk.IntVar()
    tk.Entry(top, cnf=conf, textvariable=withdraw_amount).grid(row=0, column=0)
    tk.Button(top, text='Withdraw', cnf=conf, command=withdrawal).grid(row=1, column=0)
    tk.Button(top, text='Close', cnf=conf, command=top.destroy).grid(row=2, column=0)
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Transfer $$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
def transfer():
    def transfer_money():
        global person, ind
        amount = transfer_amount.get()
        if person["balance"] > amount:
            if get_destination(des.get()):
                names = read_json('names.json')
                names[ind]["balance"] -= amount
                names[get_destination(des.get())]["balance"] += amount
                write_json('names.json', names)
                messagebox.showinfo(title='Successfully Done',message='Transfer successfull!')             
                top.destroy()
                menu.deiconify()
            else:

                messagebox.showerror(title='Failed!',message='Not Destination Found!') 
        else:            
            messagebox.showerror(title='Failed!',message='Not Enough MOney!') 
 

    def validation(var, indx, mode): 
        c1 = len(des.get()) == 16
        c2 = des.get().isdigit()
        if c1 and c2:
            e1.config(bg="green")
        else:
            e1.config(bg="red")

    top = tk.Toplevel()
    tk.Label(top, text="Amount").grid(row=0, column=0)
    transfer_amount = tk.IntVar()
    tk.Entry(top, cnf=conf, textvariable=transfer_amount).grid(row=0, column=1)
    
    tk.Label(top, text="Destination").grid(row=1, column=0)
    des = tk.StringVar()
    des.trace_add('write', validation)

    e1 = tk.Entry(top, cnf=conf, textvariable=des)
    e1.grid(row=1, column=1)
    
    tk.Button(top, text='Transfer', cnf=conf, command=transfer_money).grid(row=2, column=0)
    tk.Button(top, text='Close', cnf=conf, command=top.destroy).grid(row=3, column=0)
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
    def change():
        global person, ind
        if person["password"] == sha(old.get()):
            if sha(new.get()) == sha(new2.get()):
                names = read_json('names.json')
                names[ind]["password"] = sha(new.get())
                write_json('names.json', names)
                messagebox.showinfo(title='Successfully Done',message='Password Changed!')             
            else:
                messagebox.showerror(title='Failed!',message='Not Matched!') 
        else:            
            messagebox.showerror(title='Failed!',message='Wrong Password!') 
 
    top = tk.Toplevel()
    tk.Label(top, text="Old Password: ").grid(row=0, column=0)
    old = tk.StringVar()
    tk.Entry(top, cnf=conf, textvariable=old).grid(row=0, column=1)

    tk.Label(top, text="New Password: ").grid(row=1, column=0)
    new = tk.StringVar()
    tk.Entry(top, cnf=conf, textvariable=new).grid(row=1, column=1)

    tk.Label(top, text="New Password2: ").grid(row=2, column=0)
    new2 = tk.StringVar()
    tk.Entry(top, cnf=conf, textvariable=new2).grid(row=2, column=1)
    tk.Button(top, text='Change', cnf=conf, command=change).grid(row=3, column=0)


root = tk.Tk()
conf = {
    'font': ('times', 25),
    'bg': '#000000',
    'fg': '#ffffff'
}
person = None
ind = 0
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
tk.Label(register, text="Username", cnf=conf).grid(row=0, column=0)
username_r = tk.StringVar()
tk.Entry(register, textvariable=username_r, cnf=conf).grid(row=0, column=1)

tk.Label(register, text="Password", cnf=conf).grid(row=1, column=0)
password_r = tk.StringVar()
tk.Entry(register, textvariable=password_r, show="*", cnf=conf).grid(row=1, column=1)

button_register = tk.Button(register, text='Register', command=confirm, cnf=conf)
button_register.grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E)
button_register.bind("<Return>", confirm)

tk.Button(register, text='Cancel', command=root.destroy, cnf=conf).grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E)
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Login $$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
tk.Label(login, text="Username", cnf=conf).grid(row=0, column=0)
username_l = tk.StringVar()
tk.Entry(login, textvariable=username_l, cnf=conf).grid(row=0, column=1)

tk.Label(login, text="Password", cnf=conf).grid(row=1, column=0)
password_l = tk.StringVar()
tk.Entry(login, textvariable=password_l, show="*", cnf=conf).grid(row=1, column=1)

button_log = tk.Button(login, text='Login', command=log_in, cnf=conf)
button_log.grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E)
button_log.bind("<Return>", log_in)

tk.Button(login, text='Cancel', command=root.destroy, cnf=conf).grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E)
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Menu $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #
tk.Button(menu, text='Balance', cnf=conf, command=balance).grid(row=0, column=0)
tk.Button(menu, text='Withdraw', cnf=conf, command=withdraw).grid(row=0, column=1)
tk.Button(menu, text='Transfer', cnf=conf, command=transfer).grid(row=1, column=0)
tk.Button(menu, text='Change Password', cnf=conf, command=change_pass).grid(row=1, column=1)
menu.withdraw()
root.mainloop()
