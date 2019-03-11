from tkinter import *
from tkinter.colorchoser import askcolor as askcolour

def askBackgroundColour(focus):
    focus.chosenBackgroundColour = askcolour()
