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
        self.clientIDBox = Entry(self.master, width=70) # 
        self.clientIDBox.place(x=50, y=35) #
        self.clientIDBoxLabel = Label(self.master, text="Reddit Client ID Token")
        self.clientIDBoxLabel.place(x=475, y=34)

        self.clientSecretBox = Entry(self.master, width=70)
        self.clientSecretBox.place(x=50, y=69 + 1) # Nice.
        self.clientSecretBoxLabel = Label(self.master, text="Reddit Client Secret Token")
        self.clientSecretBoxLabel.place(x=475, y=69) #Nice.

        self.subredditBox = Entry(self.master, width=50)
        self.subredditBox.place(x=50, y=105)
        self.subredditBoxLabel = Label(self.master, text="Subreddit Name")
        self.subredditBoxLabel.place(x=350, y=104)

        self.musicNameBox = Entry(self.master, width=50)
        self.musicNameBox.place(x=50, y=170)
        self.musicNameBoxLabel = Label(self.master, text="Path To Music ( Optional )")
        self.musicNameBoxLabel.place(x=350, y=169) # Nice.

        self.renderNameBox = Entry(self.master, width=50)
        self.renderNameBox.place(x=50, y=205)
        self.renderNameBoxLabel = Label(self.master, text="Name of Outputted Render.")
        self.renderNameBoxLabel.place(x=350, y=204)

        self.renderFPSBox = Entry(self.master, width=15)
        self.renderFPSBox.insert(0, "30")
        self.renderFPSBox.place(x=50, y=330)
        self.renderFPSBoxLabel = Label(self.master, text="FPS of Output Render")
        self.renderFPSBoxLabel.place(x=75, y=329)

        self.requiredSubredditFlair = Entry(self.master, width=25)
        self.requiredSubredditFlair.place(x=50, y=365)
        self.requiredSubredditFlairLabel = Label(self.master, text="Required Subreddit Flair ( Optional )")
        self.requiredSubredditFlairLabel.place(x=200, y=364)

        self.clipDownloadCountBox = Entry(self.master, width=15)
        self.clipDownloadCountBox.insert(0, "10")
        self.clipDownloadCountBox.place(x=50, y=425)
        self.clipDownloadCountBoxLabel = Label(self.master, text="Number of Videos to Download")
        self.clipDownloadCountBoxLabel.place(x=75, y=424)

    def initCheckboxes(self):
        self.deleteOldFilesBool = BooleanVar()
        self.deleteOldFilesCheckbox = Checkbutton(self.master, variable=self.deleteOldFilesBool)
        self.deleteOldFilesCheckbox.place(x=50, y=240)
        self.deleteOldFilesLabel = Label(self.master, text="Delete Old Files? ( Downloaded Files and Previous Render )")
        self.deleteOldFilesLabel.place(x=75, y=242)

        self.giveSubmitterCreditBool = BooleanVar()
        self.giveSubmitterCreditBool.set("true")
        self.giveSubmitterCreditCheckbox = Checkbutton(self.master, variable=self.giveSubmitterCreditBool)
        self.giveSubmitterCreditCheckbox.place(x=50, y=265)
        self.giveSubmitterCreditLabel = Label(self.master, text="Give Clip Submitters Credit?")
        self.giveSubmitterCreditLabel.place(x=75, y=267)

    def initOptionmenu(self):
        self.subredditSearchMethodString = StringVar()
        self.subredditSearchMethodString.set("entirety of time")
        self.subredditSearchMethod = OptionMenu(self.master, self.subredditSearchMethodString, "entirety of time", "the the last year", "the last month", "the last week", "the last day", "the last hour")
        self.subredditSearchMethod.place(x=240, y=390)

        self.subredditSearchLabelBefore = Label(self.master, text="VM will search for posts within the")
        self.subredditSearchLabelBefore.place(x=50, y=395)

    def initProgressbars(self):
        self.downloadProgressBar = Progressbar(self.master, orient=HORIZONTAL, length=500, mode="determinate")
        self.downloadProgressBar.place(x=50, y=480)
        self.downloadProgressBarLabel = Label(self.master, text="Downloading")
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
        self.logBoxScrollbar.config(command=self.logBox.yview)
        self.logBox.place(x=750, y=35)

    def initButton(self):
        self.startButton = Button(self.master, text="Start!", width=42, height=5, command=self.packageData)
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
            if "404" in str(ex):
                self.insertLog("Could not find r/" + self.dataPackage["subredditName"])
                return
            elif "401" in str(ex):
                self.insertLog("Invalid Client Tokens")
                return

        self.insertLog("Client Tokens Verified")
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

        print(self.videoUrlDict)
        self.insertLog("Downloading Clips")
        self.clipCounter = 1
        self.clipNumberConversionTable = {}
        for videoUrl, videoCreator in self.videoUrlDict.items():
            self.parsedUrl = "https://giant.gfycat.com/" + str(videoUrl).split("/")[3] + ".mp4"
            print(self.parsedUrl)
            urllib.request.urlretrieve(self.parsedUrl, './Downloaded Videos/Clip{0}.mp4'.format(self.clipCounter))
            self.downloadProgressBar["value"] += 100/int(self.dataPackage["downloadCount"])
            self.clipNumberConversionTable[str(self.clipCounter)] = videoCreator
            self.clipCounter += 1

        self.insertLog("Downloaded Clips")
        self.insertLog("Loading Clips into Memory")

        self.clipList = []
        for videoNumber in range(1, self.dataPackage["downloadCount"] + 1):
            self.insertLog("Loading Clip: {0}".format(videoNumber))
            self.videoClip = VideoFileClip("./Downloaded Videos/Clip{0}.mp4".format(videoNumber)).fx( resize,(1280, 720)) 
            if self.dataPackage["giveCredit"]:
                self.clipAuthor = self.clipNumberConversionTable[str(videoNumber)]
                self.clipList.append(CompositeVideoClip([self.videoClip, TextClip('u/' + self.clipAuthor, fontsize=30, color='white').set_pos(('left', 'top')).set_duration(self.videoClip.duration)]))
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