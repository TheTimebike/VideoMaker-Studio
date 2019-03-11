from tkinter import *
from tkinter.colorchoser import askcolor as askcolour

def askBackgroundColour(focus):
    focus.chosenBackgroundColour = askcolour()
    stringVar = StringVar(focus.chosenBackgroundColour[1])
    focus.selectThemeBackgroundColourBox.set(stringVar)
