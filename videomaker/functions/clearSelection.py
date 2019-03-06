from tkinter import *

def clearSelections(focus, en=None):
    focus.subredditBox.delete(0, 'end')
    focus.requiredSubredditFlair.delete(0, 'end')
    focus.musicNameBox.delete(0, 'end')
    focus.renderNameBox.delete(0, 'end')
    focus.deleteOldFilesBool.set("false")
    focus.giveSubmitterCreditBool.set("true")
    focus.renderFPSBox.delete(0, 'end')
    focus.renderFPSBox.insert(0, "30")
    focus.threadingSpinbox.delete(0, "end")
    focus.threadingSpinbox.insert(0, "1")
    focus.clipDownloadCountBox.delete(0, "end")
    focus.clipDownloadCountBox.insert(0, "10")
    focus.subredditSearchMethodString.set("entirety of time")