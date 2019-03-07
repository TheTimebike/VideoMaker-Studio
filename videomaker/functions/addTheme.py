from tkinter import *
from videomaker.functions.changeTheme import changeTheme
import sys, os, glob

def addNewTheme(focus):
    fileList = glob.glob("./videomaker/interface/colourshemes/*.json")
    for themeFile in fileList:
        with open(themeFile, "r") as out:
            theme = json.load(out)
        focus.menuDropdownView.add_command(label="Enable {0} Theme".format(theme["themeName"]), command= lambda: changeTheme(focus, theme))
 
