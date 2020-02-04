#!/usr/bin/python

import tkinter
from tkinter import *

window = tkinter.Tk()

cv = IntVar()
cb = Checkbutton(window, text = "Text", variable = cv, onvalue = 1, offvalue = 0, height = 40, width = 30)
cb.pack()

window.mainloop()
