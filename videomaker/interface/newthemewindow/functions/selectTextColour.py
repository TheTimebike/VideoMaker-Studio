from tkinter import *
from tkinter.colorchoser import askcolor as askcolour

def askTextColour(focus):
    focus.chosenTextColour = askcolour()
