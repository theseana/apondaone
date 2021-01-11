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

def search_btn():
    content = search_content.get()
    if content:
        file = open('names.csv', 'r')
        for line in file:
            if content in line:
                line = line.strip('\n').split(',')
                find_first_name.set(line[0])
                find_last_name.set(line[1])
                find_birth.set(line[2])
                find_gender.set(line[3])
        file.close()


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
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& #
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&& Search &&&&&&&&&&&&&&&&&&&&&&&&&&&&&& #
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& #
search_content = tk.StringVar()
tk.Entry(search, textvariable=search_content).grid(row=0, column=1)
tk.Button(search, text='Search', command=search_btn).grid(row=0, column=0)

tk.Label(search, text='First Name').grid(row=1, column=0)
find_first_name = tk.StringVar()
tk.Label(search, textvariable=find_first_name).grid(row=1, column=1)

tk.Label(search, text='Last Name').grid(row=2, column=0)
find_last_name = tk.StringVar()
tk.Label(search, textvariable=find_last_name).grid(row=2, column=1)

tk.Label(search, text='Birth Date').grid(row=3, column=0)
find_birth = tk.StringVar()
tk.Label(search, textvariable=find_birth).grid(row=3, column=1)

tk.Label(search, text='Gender').grid(row=4, column=0)
find_gender = tk.StringVar()
tk.Label(search, textvariable=find_gender).grid(row=4, column=1)

root.mainloop()