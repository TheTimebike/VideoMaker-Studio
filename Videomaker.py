from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.AudioClip import AudioClip
from moviepy.video.VideoClip import VideoClip, TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.resize import resize
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.audio.fx import audio_loop
from tkinter import *
from tkinter.ttk import Progressbar
import praw, glob, urllib.request, threading

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.initWindow()

    def initWindow(self):
        # Main function that spirals off onto activating all of the windows objects.
        self.master.title("VideoMaker Studio")
        self.initEntryBoxes()
        self.initCheckboxes()
        self.initOptionmenu()
        self.initProgressbars()
        self.initListboxes()
        self.initButton()

    def initEntryBoxes(self):
        self.clientIDBox = Entry(self.master, width=70) # All objects are mastered to the main window
        self.clientIDBox.place(x=50, y=35) #All left-most objects are set to x=50, y increments by 35 for each object in a block
        self.clientIDBoxLabel = Label(self.master, text="Reddit Client ID Token") # Label that appears next to the entry box
        self.clientIDBoxLabel.place(x=475, y=34) # Placement of label varies on expected input size for entry box, are 1 lower on the y
        # to center with the entry box ( having 35 would result it in it being not centered).

        self.clientSecretBox = Entry(self.master, width=70)
        self.clientSecretBox.place(x=50, y=69 + 1) # Nice.
        self.clientSecretBoxLabel = Label(self.master, text="Reddit Client Secret Token")
        # Nothing is ever done with the reddit token other than try and access reddit to download posts.
        self.clientSecretBoxLabel.place(x=475, y=69) #Nice.

        self.subredditBox = Entry(self.master, width=50)
        self.subredditBox.place(x=50, y=105) # y variable incrementing by 35
        self.subredditBoxLabel = Label(self.master, text="Subreddit Name")
        self.subredditBoxLabel.place(x=350, y=104)

        self.musicNameBox = Entry(self.master, width=50)
        self.musicNameBox.place(x=50, y=170) # Given a gap of 30 extra on the y to form a new block
        self.musicNameBoxLabel = Label(self.master, text="Path To Music ( Optional )") # Check to see that the box is filled/unfilled, would
        # then enable and disable music depending on the value
        self.musicNameBoxLabel.place(x=350, y=169) # Nice.

        self.renderNameBox = Entry(self.master, width=50)
        self.renderNameBox.insert(0, "Rendered.mp4") # Sets default value to "Rendered.mp4"
        self.renderNameBox.place(x=50, y=205)
        self.renderNameBoxLabel = Label(self.master, text="Name of Outputted Render.")
        self.renderNameBoxLabel.place(x=350, y=204)

        self.renderFPSBox = Entry(self.master, width=15)
        self.renderFPSBox.insert(0, "30") # Defaults to 30 fps
        self.renderFPSBox.place(x=50, y=330) # Y variable appears to break off from the incrementing, but is actually placed under
        # two checkboxes that are initialized in another function
        # lowest checkbox's y is 265, so if we add in the 35 increment then another 30 for a new block.
        self.renderFPSBoxLabel = Label(self.master, text="FPS of Output Render")
        self.renderFPSBoxLabel.place(x=75, y=329)

        self.requiredSubredditFlair = Entry(self.master, width=25) # Most flairs are not long, so width halved to save space
        self.requiredSubredditFlair.place(x=50, y=365)
        self.requiredSubredditFlairLabel = Label(self.master, text="Required Subreddit Flair ( Optional )") # Follows the same logic as the 
        # music box, will automatically turn off if its left empty
        self.requiredSubredditFlairLabel.place(x=200, y=364)

        self.clipDownloadCountBox = Entry(self.master, width=15)
        self.clipDownloadCountBox.insert(0, "10") # Defaults to 10
        self.clipDownloadCountBox.place(x=50, y=425)
        self.clipDownloadCountBoxLabel = Label(self.master, text="Number of Videos to Download")
        self.clipDownloadCountBoxLabel.place(x=75, y=424)

    def initCheckboxes(self):
        self.deleteOldFilesBool = BooleanVar() # tkinter demands that all variables assigned to inputs have to be
        # *their* variety rather than pythons defaults. Doesnt matter much because I'm just gonna .get() all the variables
        # which converts them to pythons'.
        self.deleteOldFilesCheckbox = Checkbutton(self.master, variable=self.deleteOldFilesBool)
        self.deleteOldFilesCheckbox.place(x=50, y=240)
        self.deleteOldFilesLabel = Label(self.master, text="Delete Old Files? ( Downloaded Files and Previous Render )")
        self.deleteOldFilesLabel.place(x=75, y=242) # Text placed 2 lower due to the smaller size of the checkbuttons

        self.giveSubmitterCreditBool = BooleanVar()
        self.giveSubmitterCreditBool.set("true") # Sets default value to True ( checked ) BooleanVar doesnt take arguments during
        # init so you gotta do it in a seperate command, and you cant do BooleanVar().set() because .set() doesnt return the object
        # it also takes a uncapitalized string of "true" rather than a boolean??? whatever
        self.giveSubmitterCreditCheckbox = Checkbutton(self.master, variable=self.giveSubmitterCreditBool)
        # if you give the checkbutton a booleanvar variable it adopts its state
        self.giveSubmitterCreditCheckbox.place(x=50, y=265)
        self.giveSubmitterCreditLabel = Label(self.master, text="Give Clip Submitters Credit?")
        self.giveSubmitterCreditLabel.place(x=75, y=267)

    def initOptionmenu(self):
        self.subredditSearchMethodString = StringVar() # Once again, tkinter needs its own special variables
        self.subredditSearchMethodString.set("entirety of time") # Default
        self.subredditSearchMethod = OptionMenu(self.master, self.subredditSearchMethodString, 
        "entirety of time", # Different entries in the list
        "the the last year", # Each one determines the subreddit search type
        "the last month", # Might include support for hot, new and rising categories
        "the last week", # Would require a second option menu
        "the last day", 
        "the last hour") 

        self.subredditSearchMethod.place(x=240, y=390)
        # Optionmenu deviates from the x=50 rule, this is because its positioned after this text \/
        self.subredditSearchLabelBefore = Label(self.master, text="VM will search for posts within the")
        # You can see that the text is placed at x=50, and the optionbox is placed after the text ends.
        self.subredditSearchLabelBefore.place(x=50, y=395)

    def initProgressbars(self):
        self.downloadProgressBar = Progressbar(self.master, orient=HORIZONTAL, length=500, mode="determinate")
        # Length does not determine capacity, even if the length=500 the ["value"] is done by percentage
        # Progressbar is not from the regular tkinter package, instead the tkinter.ttk portion
        # this means that the way to interact with it can be odd sometimes, like the ["value"] thing
        self.downloadProgressBar.place(x=50, y=480)
        self.downloadProgressBarLabel = Label(self.master, text="Downloading") # regular label placed after progressbar
        self.downloadProgressBarLabel.place(x=550, y=480)

        #self.renderProgressBar = Progressbar(self.master, orient=HORIZONTAL, length=500, mode="determinate")
        #self.renderProgressBar.place(x=50, y=480)
        #self.renderProgressBarLabel = Label(self.master, text="Rendering")
        #self.renderProgressBarLabel.place(x=550, y=480)

        # Here we mourn the loss of a life of a dear loved one; Progress bar no.2
        # Having 2 progress bars was ambitious, but it was not meant to be
        # Because the only output moviepy gives for rendering is a print

    def initListboxes(self):
        self.logBoxScrollbar = Scrollbar(self.master, orient=VERTICAL)
        self.logBox = Listbox(self.master, width=50, height=22, yscrollcommand=self.logBoxScrollbar.set)  
        self.logBoxScrollbar.config(command=self.logBox.yview) # Scrollbar is not showing up due to a bug, will be fixed however!
        # if wraparound text is not possible, a horizontal oriented scrollbar might be added?
        self.logBox.place(x=750, y=35)

    def initButton(self):
        self.startButton = Button(self.master, text="Start!", width=42, height=5, command=self.packageData)
        # Cant make the text bigger or bolder without distorting the size of the button, even if the button is larger, the text is still
        # proportionate with the button
        self.startButton.place(x=750, y=400)

    def insertLog(self, logText):
        self.logBox.insert(END, logText)

    def packageData(self):
        self.downloadProgressBar["value"] = 0
        #self.renderProgressBar["value"] = 0
        self.dataPackage = {}
        self.dataPackage["redditClientID"] = self.clientIDBox.get()
        self.dataPackage["redditClientSecret"] = self.clientSecretBox.get()
        self.dataPackage["subredditName"] = self.subredditBox.get()
        if self.musicNameBox.get() != "":
            self.dataPackage["musicBool"] = True
            self.dataPackage["musicPath"] = self.musicNameBox.get() # Check to see if it exists
            #if not exists:
                #self.logBox.insert(0, "Could not find the music file specified")
                #return
        else:
            self.dataPackage["musicBool"] = False
            self.dataPackage["musicPath"] = None
        self.dataPackage["outputRenderName"] = self.renderNameBox.get()
        self.dataPackage["deleteOldBool"] = self.deleteOldFilesBool.get()
        self.dataPackage["giveCredit"] = self.giveSubmitterCreditBool.get()
        self.dataPackage["framesPerSecond"] = int(self.renderFPSBox.get())
        if self.requiredSubredditFlair.get() != "":
            self.dataPackage["flairBool"] = True
            self.dataPackage["flairName"] = self.requiredSubredditFlair.get()
        else:
            self.dataPackage["flairBool"] = False
            self.dataPackage["flairName"] = None
        self.dataPackage["timeframe"] = self.subredditSearchMethodString.get()
        self.dataPackage["downloadCount"] = int(self.clipDownloadCountBox.get())
        print(str(self.dataPackage))
        self.thread = threading.Thread(target=self.verifyData)
        self.thread.daemon = True
        self.thread.start()

    def verifyData(self):
        self.reddit = praw.Reddit(client_id=self.dataPackage["redditClientID"], client_secret=self.dataPackage["redditClientSecret"], user_agent='UserAgent')
        # 404 HTTP response == not found
        # 401 HTTP response == invalid keys
        try:
           self.subreddit = self.reddit.subreddit(self.dataPackage["subredditName"]).top(time_filter='all')
           for x in self.subreddit:
               break
        except Exception as ex:
            self.insertLog("Could not find r/" + self.dataPackage["subredditName"])
            return

        self.insertLog("r/{0} Found".format(self.dataPackage["subredditName"]))

        self.videoUrlDict = {}
        for subredditPost in self.subreddit:
            if len(self.videoUrlDict) > int(self.dataPackage["downloadCount"]) - 1:
                break
            if subredditPost.url.startswith('https://gfycat.com/'):
                if self.dataPackage["flairBool"]:
                    if subredditPost.link_flair_text.lower() != self.dataPackage["flairName"].lower():
                        continue
                self.videoUrlDict[subredditPost.url] = subredditPost.author.name

        # Check for the exitance of ./Downloaded Videos/, create if not found

        self.insertLog("Downloading Clips")
        self.clipCounter, self.clipNumberConversionTable =  = 1, {} # Initializing variables
        for videoUrl, videoCreator in self.videoUrlDict.items():
            self.parsedUrl = "https://giant.gfycat.com/" + str(videoUrl).split("/")[3] + ".mp4" # Converts regular gfycat links to
            # giant versions, which can be downloaded easier with urllib.request
            urllib.request.urlretrieve(self.parsedUrl, './Downloaded Videos/Clip{0}.mp4'.format(self.clipCounter))
            # Download clip to ./Downloaded Videos/
            self.downloadProgressBar["value"] += 100/int(self.dataPackage["downloadCount"])
            # Figure out the percentage of videos downloaded, then add it to the progressbar value
            # This is the weird-ness with the ttk objects I mentioned earler, acts as a dict rather than an object.
            self.clipNumberConversionTable[str(self.clipCounter)] = videoCreator
            # Uses a conversion table so the clip author can be found using the clip number
            self.clipCounter += 1

        self.insertLog("Downloaded Clips")
        self.insertLog("Loading Clips into Memory")

        self.clipList = [] # Creates a holder for the clips that can be stitched together with moviepy
        for videoNumber in range(1, self.dataPackage["downloadCount"] + 1): # Using a range() iter rather than a dict/list as I need the index
            self.insertLog("Loading Clip: {0}".format(videoNumber))
            self.videoClip = VideoFileClip("./Downloaded Videos/Clip{0}.mp4".format(videoNumber)).fx( resize,(1280, 720)) 
            # Loads file up as a VideoFileClip object, then resizes the clip to be 1280x720
            if self.dataPackage["giveCredit"]: # If the user wants to give credit to the clip creators
                self.clipAuthor = self.clipNumberConversionTable[str(videoNumber)] # Uses the clip number to find the creator
                self.textClip = TextClip('u/' + self.clipAuthor, fontsize=30, color='white').set_pos(('left', 'top')).set_duration(self.videoClip.duration)
                # Creates a TextClip object with "u/" appended before the clip authors name. font size and colour is set to white and 30.
                # The position of the text is set to the top left and is configured to last for the duration of the clip
                self.editedVideoClip = CompositeVideoClip([self.videoClip, self.textClip])
                # Overlays the textClip onto the videoClip
                self.clipList.append(self.editedVideoClip)
                # Puts the finished clip into a list for stitching
            else:
                self.clipList.append(CompositeVideoClip([self.videoClip]))
        self.insertLog("All Files Loaded Into Memory")
        self.insertLog("Starting Render Process")

        self.finalDuration = concatenate_videoclips(self.clipList, method='compose').duration
        if self.dataPackage["musicBool"]:
            concatenate_videoclips(self.clipList, method='compose').set_audio(afx.audio_loop(AudioFileClip(self.dataPackage["musicPath"]), duration=self.finalDuration)).write_videofile(self.dataPackage["outputRenderName"], fps=self.dataPackage["framesPerSecond"])      
        else:
            concatenate_videoclips(self.clipList, method='compose').write_videofile(self.dataPackage["outputRenderName"], fps=self.dataPackage["framesPerSecond"])    
        self.insertLog("Video Rendered")

root = Tk()
#root.state("zoomed")
#def on_closing():
#    quit()

#root.protocol("WM_DELETE_WINDOW", on_closing)
root.geometry("1100x530")
apps = Window(root)
#root.iconbitmap(filepath/to/icon)
root.mainloop() 