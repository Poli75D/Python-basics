#!/usr/bin/python

import tkinter
from tkinter import *

window = tkinter.Tk()

frame = Frame(window)
frame.pack()

btn = Button(frame, text = "Hello")
btn.pack(side = LEFT)

cv = IntVar()
cb = Checkbutton(frame, text = "Text", variable = cv, onvalue = 1, offvalue = 0, height = 6, width = 18)
cb.pack()

window.mainloop()
