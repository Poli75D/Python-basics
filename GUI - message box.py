#!/usr/bin/python

import tkinter
from tkinter import *

from tkinter import messagebox

window = tkinter.Tk()

def func():
    messagebox.showinfo("Title", "Pysiu jest super :>")

btn = Button(window, text = "Click Me Now", command = func)
btn.place(x = 0, y = 0)

window.mainloop()
