from tkinter import *
import time
def digital():
    d=time.strftime("%h:%m:%s")
    clock.config(text=d)
    clock.after(40,digital)
root=Tk()
root.title("digital clock-nithesh python")
clock=Label(root,font=('times',30,"bold"),bg="white")
clock.grid(row=2,column=1)
digital()
root.mainloop()
