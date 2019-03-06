from tkinter import *
import threading
from videomaker.functions.insertLog import insertLog
from videomaker.functions.verifyData import verifyData

def packageData(focus):
    # This function directly spins off from the button press, so whenever the button is pressed it will collect all of the information
    # provided by the user and will backage it into a dictionary, not nessesary seeing as this is class based and any function/thread
    # can access all of the information, but if I wanted to enable debugging, using JSON would be a quick and easy way to dump all of 
    # the configuration. Hooray for future proofing!

    focus.downloadProgressBar["value"] = 0
    #focus.renderProgressBar["value"] = 0
    # Set the value of both progress bars to 0, meaning they reset to empty. This fixes an issue where, when doing a second render in the
    # same session, it would not display progress properly, whenever they click start it'll clear the bars and let them refill

    focus.dataPackage = {}
    # Validation checks on each box, get ready to read a bunch of the same stuff

    if focus.clientIDBox.get() == "":
        insertLog(focus, "Please Enter a Client ID Token")
        return
    focus.dataPackage["redditClientID"] = focus.clientIDBox.get()

    if focus.clientSecretBox.get() == "":
        insertLog(focus, "Please Enter a Client Secret Token")
        return
    focus.dataPackage["redditClientSecret"] = focus.clientSecretBox.get()

    if focus.subredditBox.get() == "":
        insertLog(focus, "Please Enter a Subreddit Name")
        return
    focus.dataPackage["subredditName"] = focus.subredditBox.get()

    if focus.musicNameBox.get() != "": # Checks to see if the user entered anything
        focus.dataPackage["musicBool"] = True # Simple bool so its easy for other parts to see if they requested music.
        focus.dataPackage["musicPath"] = focus.musicNameBox.get()
        if not os.path.isfile(focus.dataPackage["musicPath"]):
            focus.logBox.insert(0, "Could not find the music file specified")
            return
    else:
        focus.dataPackage["musicBool"] = False
        focus.dataPackage["musicPath"] = None # Technichally dont need to even set this in this case, but makes it easier for debugging
        # and reading

    if focus.renderNameBox.get() == "":
        insertLog(focus, "Please Enter a Name for the Outputted File")
        return
    focus.dataPackage["outputRenderName"] = focus.renderNameBox.get() # If they didnt type anything, default to rendered.mp4 or time/date?

    focus.dataPackage["deleteOldBool"] = focus.deleteOldFilesBool.get() #No need to check for validity, theyre true or false
    focus.dataPackage["giveCredit"] = focus.giveSubmitterCreditBool.get()

    if focus.renderFPSBox.get() == "":
        insertLog(focus, "Please Enter a Valid FPS")
        return
    focus.dataPackage["framesPerSecond"] = int(focus.renderFPSBox.get())

    if focus.requiredSubredditFlair.get() != "": # Same logic as audio block
        focus.dataPackage["flairBool"] = True
        focus.dataPackage["flairName"] = focus.requiredSubredditFlair.get()
    else:
        focus.dataPackage["flairBool"] = False
        focus.dataPackage["flairName"] = None

    focus.dataPackage["timeframe"] = focus.subredditSearchMethodString.get()

    if focus.clipDownloadCountBox.get() == "":
        insertLog(focus, "Please Enter a ")
        return
    focus.dataPackage["downloadCount"] = int(focus.clipDownloadCountBox.get())

    focus.dataPackage["threadCount"] = int(focus.threadingSpinbox.get())

    print(str(focus.dataPackage)) # for debugging

    # Start thread for the rest of the verifying and rendering so the main window doesnt freeze
    focus.thread = threading.Thread(target=verifyData, args=(focus,))
    focus.thread.daemon = True # So the render stops if the user closes the program
    focus.thread.start()