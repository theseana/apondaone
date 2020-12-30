from tkinter import *

window = Tk()

b1 = Button(window,text = "h : 20 , w : 10")
b1.place(x =0 ,y = 0,height = 100,width = 110)


b2 = Button(window,text = "h : 10 , w : 10")
b2.place(x =0,y = 100,height = 50,width = 100)

window.mainloop()