import tkinter as tk

root = tk.Tk()


tk.Spinbox(root, from_=0, to=10, wrap=True).pack()
tk.Label(root, text='Label', bg='red').pack()
tk.Entry(root, bg='red', state=tk.DISABLED).pack()
tk.Button(root, text='Label', fg='blue').pack()

tk.Label(root, text = "FLAT", relief = tk.FLAT ).pack()
tk.Label(root, text = "RAISED", relief = tk.RAISED ).pack()
tk.Label(root, text = "SUNKEN", relief = tk.SUNKEN ).pack()
tk.Label(root, text = "GROOVE", relief = tk.GROOVE ).pack()
tk.Label(root, text = "RIDGE", relief = tk.RIDGE ).pack()

root.mainloop()