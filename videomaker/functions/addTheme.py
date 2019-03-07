from videomaker.functions.changeTheme import changeTheme
import sys, os, glob, json

def inbetweenFunction(focus, theme):
    focus.menuDropdownView.add_command(label="Enable {0} Theme".format(theme["themeName"]), command= lambda: changeTheme(focus, theme))

def addNewTheme(focus):
    fileList = glob.glob(os.getcwd() + "/interface/colourscheme/*.json")
    for themeFile in fileList:
        with open(themeFile, "r") as out:
            theme = json.load(out)
        inbetweenFunction(focus, theme)
 
