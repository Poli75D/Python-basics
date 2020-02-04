#!/usr/bin/python

import tkinter
from tkinter import *

window = tkinter.Tk()

string = StringVar()
msg = Message(window, textvariable = string)
string.set("The most epic piece of sting ever!")
msg.pack()

window.mainloop()
