from tkinter import *

root = Tk()

redbutton = Button(root, text="Red", fg="red")
redbutton.grid(row=0, column=0)

greenbutton = Button(root, text="green", fg="green")
greenbutton.grid(row=1, column=1)

bluebutton = Button(root, text="Blue", fg="blue")
bluebutton.grid(row=2, column=1)

root.mainloop()