from tkinter import *
from videomaker.interface.newthemewindow.interface.initializer import initWindow as oInitWindow

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Create A Theme")
        oInitWindow(self)

def initWindow():
    root = Tk()
    root.geometry("400x400")
    apps = Window(root)
    root.mainloop()