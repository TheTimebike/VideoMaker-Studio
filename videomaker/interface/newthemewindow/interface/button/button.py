from tkinter import *

def initButton(focus):
    focus.selectThemeBackgroundColourButton = Button(focus.master, text="Select", width=10, height=1)
    focus.selectThemeBackgroundColourButton.place(x=225, y=83)

    focus.selectThemeBoxColourButton = Button(focus.master, text="Select", width=10, height=1)
    focus.selectThemeBoxColourButton.place(x=225, y=133)

    focus.selectThemeTextColourButton = Button(focus.master, text="Select", width=10, height=1)
    focus.selectThemeTextColourButton.place(x=225, y=183)