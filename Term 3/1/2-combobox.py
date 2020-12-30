import tkinter as tk
from tkinter import messagebox

root = tk.Tk()


choices = ['-select-', 'US', 'IR', 'UK']
o1 = tk.OptionMenu(root, *choices)
o1.pack()

root.mainloop()