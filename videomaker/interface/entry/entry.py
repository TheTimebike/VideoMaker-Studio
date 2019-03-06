from tkinter import *

def initEntryBoxes(focus):
    focus.clientIDBox = Entry(focus.master, width=70) # All objects are mastered to the main window
    focus.clientIDBox.place(x=50, y=35) #All left-most objects are set to x=50, y increments by 35 for each object in a block
    focus.clientIDBoxLabel = Label(focus.master, text="Reddit Client ID Token") # Label that appears next to the entry box
    focus.clientIDBoxLabel.place(x=475, y=34) # Placement of label varies on expected input size for entry box, are 1 lower on the y
    # to center with the entry box ( having 35 would result it in it being not centered).

    focus.clientSecretBox = Entry(focus.master, width=70)
    focus.clientSecretBox.place(x=50, y=69 + 1) # Nice.
    focus.clientSecretBoxLabel = Label(focus.master, text="Reddit Client Secret Token")
    # Nothing is ever done with the reddit token other than try and access reddit to download posts.
    focus.clientSecretBoxLabel.place(x=475, y=69) #Nice.

    focus.subredditBox = Entry(focus.master, width=50)
    focus.subredditBox.place(x=50, y=105) # y variable incrementing by 35
    focus.subredditBoxLabel = Label(focus.master, text="Subreddit Name")
    focus.subredditBoxLabel.place(x=350, y=104)

    focus.musicNameBox = Entry(focus.master, width=50)
    focus.musicNameBox.place(x=50, y=170) # Given a gap of 30 extra on the y to form a new block
    focus.musicNameBoxLabel = Label(focus.master, text="Path To Music ( Optional )") # Check to see that the box is filled/unfilled, would
    # then enable and disable music depending on the value
    focus.musicNameBoxLabel.place(x=350, y=169) # Nice.

    focus.renderNameBox = Entry(focus.master, width=50)
    focus.renderNameBox.insert(0, "Rendered.mp4") # Sets default value
    focus.renderNameBox.place(x=50, y=205)
    focus.renderNameBoxLabel = Label(focus.master, text="Name of Outputted Render.")
    focus.renderNameBoxLabel.place(x=350, y=204)

    focus.renderFPSBox = Entry(focus.master, width=15)
    focus.renderFPSBox.insert(0, "30") # Defaults to 30 fps
    focus.renderFPSBox.place(x=50, y=330) # Y variable appears to break off from the incrementing, but is actually placed under
    # two checkboxes that are initialized in another function
    # lowest checkbox's y is 265, so if we add in the 35 increment then another 30 for a new block.
    focus.renderFPSBoxLabel = Label(focus.master, text="Frames Per Second")
    focus.renderFPSBoxLabel.place(x=75, y=329)

    focus.requiredSubredditFlair = Entry(focus.master, width=25) # Most flairs are not long, so width halved to save space
    focus.requiredSubredditFlair.place(x=50, y=365)
    focus.requiredSubredditFlairLabel = Label(focus.master, text="Required Subreddit Flair ( Optional )") # Follows the same logic as the 
    # music box, will automatically turn off if its left empty
    focus.requiredSubredditFlairLabel.place(x=200, y=364)

    focus.clipDownloadCountBox = Entry(focus.master, width=15)
    focus.clipDownloadCountBox.insert(0, "10") # Defaults to 10
    focus.clipDownloadCountBox.place(x=50, y=425)
    focus.clipDownloadCountBoxLabel = Label(focus.master, text="Number of Videos to Download")
    focus.clipDownloadCountBoxLabel.place(x=75, y=424)
