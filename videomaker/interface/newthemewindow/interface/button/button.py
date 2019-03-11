from tkinter import *
from videomaker.interface.newthemewindow.functions.selectBackgroundColour import askBackgroundColour
from videomaker.interface.newthemewindow.functions.selectTextColour import askTextColour
from videomaker.interface.newthemewindow.functions.selectBoxColour import askBoxColour
from videomaker.interface.newthemewindow.functions.createTheme import createTheme

def initButton(focus):
    focus.selectThemeBackgroundColourButton = Button(focus.master, text="Select", width=10, height=1, command=lambda: askBackgroundColour(focus))
    focus.selectThemeBackgroundColourButton.place(x=225, y=83)

    focus.selectThemeBoxColourButton = Button(focus.master, text="Select", width=10, height=1, command=lambda: askBoxColour(focus)
    focus.selectThemeBoxColourButton.place(x=225, y=133)

    focus.selectThemeTextColourButton = Button(focus.master, text="Select", width=10, height=1, command=lambda: askTextColour(focus)
    focus.selectThemeTextColourButton.place(x=225, y=183)
                                               
    focus.createThemeButton = Button(focus.master, text="Create", width=100, height=3, command=lambda: createTheme(focus))
    focus.createThemeButton.place(x=50, y=250)
