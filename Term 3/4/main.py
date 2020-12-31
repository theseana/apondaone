from re import template
import tkinter as tk
from tkinter import ttk

from tkcalendar import DateEntry


def register_btn():
    f = first_name.get()
    l = last_name.get()
    b = birth_date.get()
    g = gender.get()
    template = f'{f},{l},{b},{g}\n'
    file = open('names.csv', 'a')
    file.write(template)
    file.close()
    first_name.set('')
    last_name.set('')

root = tk.Tk()
root.geometry("244x188")
root.resizable(0, 0)
note = ttk.Notebook()
note.place(x=0, y=0)

register = tk.Frame(note)
search = tk.Frame(note)

note.add(register, text='Registration Form')
note.add(search, text='Search Form')
# ################################################################## #
# ############################ Register ############################ #
# ################################################################## #
tk.Label(register, text='Frist Name').grid(row=0, column=0)
first_name = tk.StringVar()
tk.Entry(register, textvariable=first_name).grid(row=0, column=1)

tk.Label(register, text='Last Name').grid(row=1, column=0)
last_name = tk.StringVar()
tk.Entry(register, textvariable=last_name).grid(row=1, column=1)

tk.Label(register, text='Birth Date').grid(row=2, column=0)
birth_date = tk.StringVar()
DateEntry(
    register,
    textvariable=birth_date,
    background='darkgreen',
    foreground='white',
    width=10
    ).grid(row=2, column=1, sticky=tk.W+tk.E)

tk.Label(register, text='Gender').grid(row=3, column=0)
gender = tk.StringVar()
gender.set('-select-')
choices = ['F', 'M', 'Others', 'Not to Say']
tk.OptionMenu(register, gender, *choices).grid(row=3, column=1, sticky=tk.W+tk.E)

tk.Button(
    register,
    text='Register',
    command=register_btn
    ).grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E)
tk.Button(
    register,
    text='Cancel',
    command=root.destroy
    ).grid(row=5, column=0, columnspan=2, sticky=tk.W+tk.E)

root.mainloop()