import webbrowser, sys

def redirectToSourceCode():
    webbrowser.open("https://github.com/TheTimebike/VideoMaker-Studio", 2, True)
def redirectToGithubIssue():
    webbrowser.open("https://github.com/TheTimebike/VideoMaker-Studio/issues", 2, True)
def redirectToRedditMessage():
    webbrowser.open("https://www.reddit.com/message/compose?to=TheTimebike&subject=Videomaker%20Studio", 2, True)
def redirectToRedditTokens():
    webbrowser.open("https://www.reddit.com/prefs/apps/", 2, True)
def quitProgram():
    sys.exit()