from tkinter import *
from videomaker.interface.newthemewindow.interface.initializer import initWindow as initWindowModules
from videomaker.interface.newthemewindow.functions.changeTheme import changeTheme

class Window(Frame):
    def __init__(self, master=None, main=None):
        Frame.__init__(self, master)
        self.master.title("Create A Theme")
        self.main = main
        self.chosenBackgroundColour = ""
        self.chosenBoxColour = ""
        self.chosenTextColour = ""
        initWindowModules(self)
        changeTheme(self)
        

def initWindow(mainWindow):
    root = Tk()
    root.geometry("400x400")
    apps = Window(root, main=mainWindow)
    root.mainloop()
