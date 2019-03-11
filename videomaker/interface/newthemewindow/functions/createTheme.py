from tkinter import *
import json, os

def createTheme(focus):
    dataPackage = {}
    dataPackage["Name"] = focus.selectThemeNameBox.get()
    dataPackage["backgroundColour"] = focus.selectThemeBackgroundColourBox.get()
    dataPackage["boxColour"] = focus.selectThemeBoxColourBox.get()
    dataPackage["textColour"] = focus.selectThemeTextColourBox.get()
    
    with open(os.getcwd() + "/interface/colourscheme/{0}.json".format(dataPackage["Name"].lower() + "theme"), "w+") as out:
        json.dump(dataPackage, out, indent=4)
