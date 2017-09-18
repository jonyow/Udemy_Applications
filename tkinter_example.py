
from tkinter import *

def runConversion():
    #t1.insert(END, float(e1_value.get())*1.6)
    t1_value.set(float(e1_value.get())*1.6)

window = Tk()

b1 = Button(window, text = "Run", command=runConversion)

b1.grid(row=0, column = 0)

e1_value = StringVar()

e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column =1)

t1_value = StringVar()
t1 = Text(window, height=1, width=20, textvariable = t1_value)
t1.grid(row=0, column=2)

window.mainloop()

