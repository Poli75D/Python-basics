#!/usr/bin/python

import tkinter
from tkinter import *

window = tkinter.Tk()

labelFrame = LabelFrame(window, text = "This is awesome")
labelFrame.pack(fill = "both", expand = "yes")

left = Label(labelFrame, text = "Inside the LabelFrame")
left.pack()

window.mainloop()
