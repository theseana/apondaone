from tkinter import *

root = Tk()

redbutton = Button(root, text="Red", fg="red")
redbutton.pack()

greenbutton = Button(root, text="green", fg="green")
greenbutton.pack()

bluebutton = Button(root, text="Blue", fg="blue")
bluebutton.pack()

root.mainloop()