from tkinter import *
#from functions.packageData import packageData

def initButton(focus):
    focus.startButton = Button(focus.master, text="Start!", width=42, height=5)#, command= lambda: packageData(focus))
    # Cant make the text bigger or bolder without distorting the size of the button, even if the button is larger, the text is still
    # proportionate with the button
    focus.startButton.place(x=750, y=400)
