from tkinter import *

def initSpinbox(focus):
    focus.threadingSpinbox = Spinbox(focus.master, values=(1,2,3,4,5,6,7,8,9), width=2)
    focus.threadingSpinbox.place(x=240, y=330) # Aligned vertically with the fps box and is aligned hoziontally with the 
    focus.threadingSpinboxLabel = Label(focus.master, text="Thread Count")
    focus.threadingSpinboxLabel.place(x=270, y=330)
