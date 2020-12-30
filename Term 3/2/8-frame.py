import tkinter as tk 


root = tk.Tk()
f1 = tk.Frame(root)
f2 = tk.Frame(root)
f2.pack()
f1.pack()
tk.Entry(f1, bg='red').pack()
tk.Button(f1, bg='red', text='Say my name!').pack()

tk.Entry(f2 ,bg='blue').pack()
tk.Button(f2 ,bg='blue', text='Say my name!').pack()

root.mainloop()
