from tkinter import *

def initEntry(focus):
    focus.selectThemeNameBox  = Entry(focus.master, width=25)
    focus.selectThemeNameBox.place(x=50, y=35)
    focus.selectThemeNameBoxLabel = Label(focus.master, text="Select a Theme Name")
    focus.selectThemeNameBoxLabel.place(x=50, y=10)

    focus.selectThemeBackgroundColourBox = Entry(focus.master, width=25, variable=focus.chosenBackgroundColour)
    focus.selectThemeBackgroundColourBox.place(x=50, y=85)
    focus.selectThemeBackgroundColourBoxLabel = Label(focus.master, text="Select a Theme Background Colour")
    focus.selectThemeBackgroundColourBoxLabel.place(x=50, y=60)

    focus.selectThemeTextColourBox = Entry(focus.master, width=25, variable=focus.chosenTextColour)
    focus.selectThemeTextColourBox.place(x=50, y=135)
    focus.selectThemeTextColourBoxLabel = Label(focus.master, text="Select A Theme Text Colour")
    focus.selectThemeTextColourBoxLabel.place(x=50, y=110)

    focus.selectThemeBoxColourBox = Entry(focus.master, width=25, variable=focus.chosenBoxColour)
    focus.selectThemeBoxColourBox.place(x=50, y=185)
    focus.selectThemeBoxColourBoxLabel = Label(focus.master, text="Select a Theme Box Colour")
    focus.selectThemeBoxColourBoxLabel.place(x=50, y=160)
