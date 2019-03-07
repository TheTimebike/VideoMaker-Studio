from tkinter import *

def toggleDarkMode(focus):
    focus.textColour = "white"
    focus.backgroundColour="#36393f"
    focus.boxColour="#484b52"
    if focus.darkThemeBool.get() == False:
        focus.textColour = "black" # inverts the colours
        focus.backgroundColour = "#f0f0f0"
        focus.boxColour = "white"

    focus.logBox.configure(background=focus.boxColour)
    focus.master.configure(background=focus.backgroundColour) # Mass changing the colours of objects
    focus.clientIDBoxLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
    focus.clientIDBox.configure(background=focus.boxColour, foreground=focus.textColour)
    focus.clientSecretBoxLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
    focus.clientSecretBox.configure(background=focus.boxColour, foreground=focus.textColour)
    focus.subredditBoxLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
    focus.subredditBox.configure(background=focus.boxColour, foreground=focus.textColour)
    focus.musicNameBoxLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
    focus.musicNameBox.configure(background=focus.boxColour, foreground=focus.textColour)
    focus.renderNameBoxLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
    focus.renderNameBox.configure(background=focus.boxColour, foreground=focus.textColour)
    focus.deleteOldFilesLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
    focus.deleteOldFilesCheckbox.configure(background=focus.backgroundColour, activebackground=focus.backgroundColour, activeforeground=focus.textColour)
    focus.giveSubmitterCreditLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
    focus.giveSubmitterCreditCheckbox.configure(background=focus.backgroundColour, activebackground=focus.backgroundColour, activeforeground=focus.textColour)
    focus.renderFPSBoxLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
    focus.renderFPSBox.configure(background=focus.boxColour, foreground=focus.textColour)
    focus.threadingSpinboxLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
    focus.threadingSpinbox.configure(background=focus.boxColour, foreground=focus.textColour)
    focus.requiredSubredditFlairLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
    focus.requiredSubredditFlair.configure(background=focus.boxColour, foreground=focus.textColour)
    focus.subredditSearchLabelBefore.configure(background=focus.backgroundColour, foreground=focus.textColour)
    focus.subredditSearchMethod.configure(highlightthickness=0, background=focus.backgroundColour, foreground=focus.textColour, activebackground=focus.backgroundColour, activeforeground=focus.textColour)
    focus.clipDownloadCountBoxLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
    focus.clipDownloadCountBox.configure(background=focus.boxColour, foreground=focus.textColour)
    focus.downloadProgressBarLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
    #focus.downloadProgressBar.configure(background=focus.boxColour, foreground=focus.textColour)
