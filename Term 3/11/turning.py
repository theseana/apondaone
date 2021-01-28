import tkinter as tk
import datetime

def pressed():
    msg = """WELCOME
YOUR TURN: {}
{}
{}
{} people in line
""" 
    number.set(number.get() + 1)
    today = datetime.datetime.now()
    date = today.strftime("%a, %b-%d-%Y")
    time = today.strftime("%H:%M:%S")
    print(msg.format(number.get(),date, time, 1))
root = tk.Tk()
number = tk.IntVar()
text_box = tk.Text(root, bg='khaki', width=21, height=8)
text_box.grid(row=0, column=0) 
text_box.insert(tk.END, 'You will be FIRST ONE!!!')
tk.Button(root, text='PRESS!', command=pressed).grid(row=1, column=0)
root.mainloop()