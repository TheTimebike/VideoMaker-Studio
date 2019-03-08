from videomaker.functions.changeTheme import changeTheme
import sys, os, glob, json

def addOption(focus, theme):
    focus.menuDropdownView.add_command(label="Enable {0} Theme".format(theme["themeName"]), command= lambda: changeTheme(focus, theme))

# Because of the way that the command system works in tkinter, the arguments passed to the function 
# are not given during the command to add the button, and are rather referenced to the actual variable. 
# This means that, despite having passed one version of "theme", it would check to see what "theme" 
# held at the time of button press. This would mess everything up. I fixed this by passing it through
# a seperate function before the command. This fixes the bug as the function does not reference the original
# variable, and rather just holds a static version of what was passed to it. This allows me to change "theme"
# in the loop without overwriting its data.

def addNewTheme(focus):
    fileList = glob.glob(os.getcwd() + "/interface/colourscheme/*.json") # Iterates through json files in the directory
    for themeFile in fileList:
        try:
            with open(themeFile, "r") as out:
                theme = json.load(out) # Saves the data in the file to a variable
            addOption(focus, theme) # Adds the option to the view tab
        except Exception as ex:
            pass
