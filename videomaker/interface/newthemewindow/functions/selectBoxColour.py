from tkinter import *
from tkinter.colorchoser import askcolor as askcolour

def askBoxColour(focus):
    focus.chosenBoxColour = askcolour()
    stringVar = StringVar(focus.chosenBoxColour[1])
    focus.selectThemeBoxColourBox.set(stringVar)
