#!/usr/bin/python

import tkinter
from tkinter import *

window = tkinter.Tk()

lbox = Listbox(window)
lbox.insert(1, "Item1")
lbox.insert(2, "Item2")
lbox.insert(3, "Item3")
lbox.insert(4, "Item4")
lbox.insert(5, "Item5")
lbox.pack()

window.mainloop()
