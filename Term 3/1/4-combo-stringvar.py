import tkinter as tk

root = tk.Tk()


choices = ['US', 'IR', 'UK']
option = tk.StringVar()
option.set('UK')
tk.OptionMenu(root, option, *choices).pack()

root.mainloop()