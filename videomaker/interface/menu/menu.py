from tkinter import *
from videomaker.functions.packageData import packageData
from videomaker.interface.menu.functions.modules import *

def initMenubar(focus):
    focus.menuBar = Menu(focus.master)
    focus.master.config(menu=focus.menuBar)
    focus.menuDropdownStudio = Menu(focus.menuBar)
    focus.menuDropdownView = Menu(focus.menuBar)
    focus.menuDropdownDebug = Menu(focus.menuBar)
    focus.menuDropdownHelp = Menu(focus.menuBar)

    focus.menuDropdownStudio.add_command(label="Start", command= lambda: packageData(focus))
    focus.menuDropdownStudio.add_command(label="Clear Boxes", command=focus.clearSelections)
    focus.menuDropdownStudio.add_command(label="Remove Old Clips", command=focus.deleteOldClips)
    focus.menuDropdownStudio.add_command(label="Quit", command=quitProgram)

    focus.darkThemeBool = BooleanVar()
    focus.darkThemeBool.set("false")
    focus.menuDropdownView.add_checkbutton(label="Toggle Dark Mode", onvalue=True, offvalue=False, command=focus.turnOnDarkMode, variable=focus.darkThemeBool)

    focus.loggingModeBool = BooleanVar()
    focus.loggingModeBool.set("false")
    focus.menuDropdownDebug.add_checkbutton(label="Logging Mode", onvalue=True, offvalue=False, variable=focus.loggingModeBool)

    focus.menuDropdownHelp.add_command(label="Source Code", command=redirectToSourceCode)
    focus.menuDropdownHelp.add_command(label="File Issue", command=redirectToGithubIssue)
    focus.menuDropdownHelp.add_command(label="Contact The Creator", command=redirectToRedditMessage)
    focus.menuDropdownHelp.add_command(label="How To Find Reddit Tokens?", command=redirectToRedditTokens)

    focus.menuBar.add_cascade(label="VideoMaker Studio", menu=focus.menuDropdownStudio)
    focus.menuBar.add_cascade(label="View", menu=focus.menuDropdownView)
    focus.menuBar.add_cascade(label="Debug", menu=focus.menuDropdownDebug)
    focus.menuBar.add_cascade(label="Help", menu=focus.menuDropdownHelp)
