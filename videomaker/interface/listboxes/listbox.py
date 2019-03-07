from tkinter import *

def initListboxes(focus):
    focus.logBoxScrollbar = Scrollbar(focus.master, orient=VERTICAL)
    focus.logBox = Listbox(focus.master, width=50, height=22, yscrollcommand=focus.logBoxScrollbar.set)  
    focus.logBoxScrollbar.config(command=focus.logBox.yview) # Scrollbar is not showing up due to a bug, will be fixed however!
    # if wraparound text is not possible, a horizontal oriented scrollbar might be added?
    focus.logBox.place(x=750, y=35)
