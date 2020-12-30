import tkinter as tk


root = tk.Tk()
root.config(bg='black')
root.geometry("610x328")
head = tk.Frame()
cent = tk.Frame()
left = tk.Frame()
right = tk.Frame()

head.place(x=10, y=10, width=590, height=27)
cent.place(x=210, y=47, width=190, height=266)
left.place(x=10, y=47, width=190, height=266)
right.place(x=410, y=47, width=190, height=266)

l_t = tk.Frame(bg='#556eaa')
l_m = tk.Frame(bg='#556eaa')
l_b = tk.Frame(bg='#556eaa')

l_t.place(x=20, y=57, width=170, height=76)
l_m.place(x=20, y=141, width=170, height=76)
l_b.place(x=20, y=226, width=170, height=76)

root.mainloop()