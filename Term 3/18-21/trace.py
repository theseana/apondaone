from tkinter import * 
  

def validation(var, indx, mode): 
    c1 = len(my_var.get()) == 16
    c2 = my_var.get().isdigit()
    if c1 and c2:
        e1.config(bg="green")
    else:
        e1.config(bg="red")



root = Tk() 


my_var = StringVar() 
my_var.trace_add('write', validation)

Label(root, textvariable = my_var).grid(row=0, column=0) 
e1 = Entry(root, textvariable = my_var)
e1.grid(row=1, column=0) 

root.mainloop() 