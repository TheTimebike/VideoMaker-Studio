from tkinter import *
from tkinter.ttk import Progressbar

def initProgressbars(focus):
    focus.downloadProgressBar = Progressbar(focus.master, orient=HORIZONTAL, length=500, mode="determinate")
    # Length does not determine capacity, even if the length=500 the ["value"] is done by percentage
    # Progressbar is not from the regular tkinter package, instead the tkinter.ttk portion
    # this means that the way to interact with it can be odd sometimes, like the ["value"] thing
    focus.downloadProgressBar.place(x=50, y=480)
    focus.downloadProgressBarLabel = Label(focus.master, text="Downloading") # regular label placed after progressbar
    focus.downloadProgressBarLabel.place(x=550, y=480)

    #focus.renderProgressBar = Progressbar(focus.master, orient=HORIZONTAL, length=500, mode="determinate")
    #focus.renderProgressBar.place(x=50, y=480)
    #focus.renderProgressBarLabel = Label(focus.master, text="Rendering")
    #focus.renderProgressBarLabel.place(x=550, y=480)

    # Here we mourn the loss of a life of a dear loved one; Progress bar no.2
    # Having 2 progress bars was ambitious, but it was not meant to be
    # Because the only output moviepy gives for rendering is a print