#!/usr/bin/python

import tkinter
from tkinter import *

window = tkinter.Tk()

mButton = Menubutton(window, text = "Click Me!")
mButton.grid()
mButton.menu = Menu(mButton)
mButton["menu"] = mButton.menu

mButton.menu.add_checkbutton(label = "Item1")
mButton.menu.add_checkbutton(label = "Item2")
mButton.menu.add_checkbutton(label = "Item3")
mButton.menu.add_checkbutton(label = "Item4")
mButton.menu.add_checkbutton(label = "Item5")
mButton.menu.add_checkbutton(label = "Item6")
mButton.menu.add_checkbutton(label = "Item7")
mButton.menu.add_checkbutton(label = "Item8")
mButton.pack

window.mainloop()
