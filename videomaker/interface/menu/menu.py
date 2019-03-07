from tkinter import *
from videomaker.functions.startThread import startThread
from videomaker.functions.clearSelection import clearSelections
from videomaker.functions.deleteOldClips import deleteOldClips
from videomaker.functions.darkMode import turnOnDarkMode
from videomaker.functions.redirect import *

def initMenubar(focus):
    focus.menuBar = Menu(focus.master)
    focus.master.config(menu=focus.menuBar)
    focus.menuDropdownStudio = Menu(focus.menuBar)
    focus.menuDropdownView = Menu(focus.menuBar)
    focus.menuDropdownDebug = Menu(focus.menuBar)
    focus.menuDropdownHelp = Menu(focus.menuBar)

    focus.menuDropdownStudio.add_command(label="Start", command= lambda: startThread(focus))
    focus.menuDropdownStudio.add_command(label="Clear Boxes", command=lambda: clearSelections(focus))
    focus.menuDropdownStudio.add_command(label="Remove Old Clips", command=deleteOldClips)
    focus.menuDropdownStudio.add_command(label="Quit", command=quitProgram)

    focus.darkThemeBool = BooleanVar()
    focus.darkThemeBool.set("false")
    focus.menuDropdownView.add_checkbutton(label="Toggle Dark Mode", onvalue=True, offvalue=False, command= lambda: turnOnDarkMode(focus), variable=focus.darkThemeBool)

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
