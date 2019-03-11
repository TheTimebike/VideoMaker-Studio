from tkinter import *
from tkinter.colorchoser import askcolor as askcolour

def askBoxColour(focus):
    focus.chosenBoxColour = askcolour()
