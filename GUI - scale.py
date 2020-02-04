#!/usr/bin/python

import tkinter
from tkinter import *

def getValue():
    selection = "Value: " + str(var.get())
    label.config(text = selection)

window = tkinter.Tk()

var = DoubleVar()
scale = Scale(window, variable = var)
scale.pack()

button = Button(window, text = "Retrieve value", command = getValue)
button.pack()

label = Label(window)
label.pack()

window.mainloop()
