from tkinter import *
from videomaker.interface.initializer import initWindow
from videomaker.functions.createFiles import createDirectories
import sys

isFrozen = False
if getattr(sys, 'frozen', True):
    isFrozen = True

# Ive tried to comment and make this as maintainable as possible because maybe someday someone is gonna find this and have no
# clue whats going on. That person will probably be me.

# Spacing Codex:
    # Objects should be spaced 50 x
    # Objects should be spaced by 35 y
    # Block seperator +30 y
    # Labels for checkboxes are +2 y
    # Labels for entry boxes are -1 y
    # Width of token entry boxes are 70
    # Width of path entry boxes are 50
    # Width of string entry boxes are 25
    # Width of number entry boxes are 15

class Window(Frame):
    def __init__(self, master=None, frozen=False):
        Frame.__init__(self, master)
        self.isFrozen = frozen
        self.master = master
        self.master.title("VideoMaker Studio")
        createDirectories()
        initWindow(self)
       
if __name__ == "__main__":
    root = Tk()
    root.geometry("1100x530")
    apps = Window(root, isFrozen)
    #root.iconbitmap("./vms.ico")
    root.mainloop()
