from tkinter import *
from tkinter.colorchooser import askcolor as askcolour

def askTextColour(focus):
    focus.chosenTextColour = askcolour()
    stringVar = StringVar(focus.chosenTextColour[1])
    focus.selectThemeTextColourBox.set(stringVar)
