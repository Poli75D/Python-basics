#!/usr/bin/python

import tkinter
from tkinter import *

window = tkinter.Tk()

text = Text(window)
text.insert(INSERT, "Hello...")
text.insert(END, "Bye Bye...")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background = "yellow", foreground = "red")
text.tag_config("start", background = "black", foreground = "green")

window.mainloop()
