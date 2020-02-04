#!/usr/bin/python

import tkinter
from tkinter import *

window = tkinter.Tk()

box = Spinbox(window, from_ = 0, to = 10)
box.pack()

window.mainloop()
