from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.AudioClip import AudioClip
from moviepy.video.VideoClip import VideoClip, TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.resize import resize
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.audio.fx.audio_loop import audio_loop
from tkinter import *
from tkinter.ttk import Progressbar
import praw, glob, urllib.request, threading, sys, os
from videomaker.interface.initializer import initWindow

# Ive tried to comment and make this as maintainable as possible because maybe someday someone is gonna find this and have no
# clue whats going on. That person will probably be me.

# Spacing Codex:
    # Objects should be spaced 50 x
    # Objects should be spaced by 35 y
    # Block seperator +30 y
    # Labels for checkboxes are +2 y
    # Labels for entry boxes are -1 y
    # Width of token entry boxes are 70
    # Width of path entry boxes are 50
    # Width of string entry boxes are 25
    # Width of number entry boxes are 15

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.initWindow()

    def initWindow(self):
        # Main function that spirals off onto activating all of the windows objects.
        self.master.title("VideoMaker Studio")
        initWindow(self)

    def turnOnDarkMode(self):
        self.textColour = "white"
        self.backgroundColour="#36393f"
        self.boxColour="#484b52"
        if self.darkThemeBool.get() == False:
            self.textColour = "black" # inverts the colours
            self.backgroundColour = "#f0f0f0"
            self.boxColour = "white"

        self.logBox.configure(background=self.boxColour)
        self.master.configure(background=self.backgroundColour) # Mass changing the colours of objects
        self.clientIDBoxLabel.configure(background=self.backgroundColour, foreground=self.textColour)
        self.clientIDBox.configure(background=self.boxColour, foreground=self.textColour)
        self.clientSecretBoxLabel.configure(background=self.backgroundColour, foreground=self.textColour)
        self.clientSecretBox.configure(background=self.boxColour, foreground=self.textColour)
        self.subredditBoxLabel.configure(background=self.backgroundColour, foreground=self.textColour)
        self.subredditBox.configure(background=self.boxColour, foreground=self.textColour)
        self.musicNameBoxLabel.configure(background=self.backgroundColour, foreground=self.textColour)
        self.musicNameBox.configure(background=self.boxColour, foreground=self.textColour)
        self.renderNameBoxLabel.configure(background=self.backgroundColour, foreground=self.textColour)
        self.renderNameBox.configure(background=self.boxColour, foreground=self.textColour)
        self.deleteOldFilesLabel.configure(background=self.backgroundColour, foreground=self.textColour)
        self.deleteOldFilesCheckbox.configure(background=self.backgroundColour, activebackground=self.backgroundColour, activeforeground=self.textColour)
        self.giveSubmitterCreditLabel.configure(background=self.backgroundColour, foreground=self.textColour)
        self.giveSubmitterCreditCheckbox.configure(background=self.backgroundColour, activebackground=self.backgroundColour, activeforeground=self.textColour)
        self.renderFPSBoxLabel.configure(background=self.backgroundColour, foreground=self.textColour)
        self.renderFPSBox.configure(background=self.boxColour, foreground=self.textColour)
        self.threadingSpinboxLabel.configure(background=self.backgroundColour, foreground=self.textColour)
        self.threadingSpinbox.configure(background=self.boxColour, foreground=self.textColour)
        self.requiredSubredditFlairLabel.configure(background=self.backgroundColour, foreground=self.textColour)
        self.requiredSubredditFlair.configure(background=self.boxColour, foreground=self.textColour)
        self.subredditSearchLabelBefore.configure(background=self.backgroundColour, foreground=self.textColour)
        self.subredditSearchMethod.configure(highlightthickness=0, background=self.backgroundColour, foreground=self.textColour, activebackground=self.backgroundColour, activeforeground=self.textColour)
        self.clipDownloadCountBoxLabel.configure(background=self.backgroundColour, foreground=self.textColour)
        self.clipDownloadCountBox.configure(background=self.boxColour, foreground=self.textColour)
        self.downloadProgressBarLabel.configure(background=self.backgroundColour, foreground=self.textColour)
        #self.downloadProgressBar.configure(background=self.boxColour, foreground=self.textColour)

    def insertLog(self, logText):
        self.logBox.insert(END, logText)

    def clearSelections(self, en=None):
        self.subredditBox.delete(0, 'end')
        self.requiredSubredditFlair.delete(0, 'end')
        self.musicNameBox.delete(0, 'end')
        self.renderNameBox.delete(0, 'end')
        self.deleteOldFilesBool.set("false")
        self.giveSubmitterCreditBool.set("true")
        self.renderFPSBox.delete(0, 'end')
        self.renderFPSBox.insert(0, "30")
        self.threadingSpinbox.delete(0, "end")
        self.threadingSpinbox.insert(0, "1")
        self.clipDownloadCountBox.delete(0, "end")
        self.clipDownloadCountBox.insert(0, "10")
        self.subredditSearchMethodString.set("entirety of time")

    def verifyData(self):
        self.reddit = praw.Reddit(client_id=self.dataPackage["redditClientID"], client_secret=self.dataPackage["redditClientSecret"], user_agent='UserAgent')
        # 404 HTTP response == not found
        # 401 HTTP response == invalid keys
        # 503 HTTP response == could not connect to reddit
        self.timeframeToRedditFormatConversionTable = {
            "entirety of time": "all", 
            "the last year": "year", 
            "the last month": "month", 
            "the last week": "week",
            "the last day": "day",
            "the last hour": "hour"
            } # Long name
        try:
           self.subreddit = self.reddit.subreddit(self.dataPackage["subredditName"]).top(time_filter=self.timeframeToRedditFormatConversionTable[self.dataPackage["timeframe"]])
           for x in self.subreddit: # Quick one iteration loop to see if the tokens/subreddit name is correct
               # A little sloppy and I'll probably revise this once i get the chance, low priority issue
               break
        except Exception as ex:
            self.insertLog("Could not find r/" + self.dataPackage["subredditName"])
            print(ex)
            return

        self.insertLog("r/{0} Found".format(self.dataPackage["subredditName"]))

        self.videoUrlDict = {} # Dictionary to store pairs of clips and authors.
        # post URL is the key and author name is the value
        for subredditPost in self.subreddit:
            if len(self.videoUrlDict) > int(self.dataPackage["downloadCount"]) - 1:
                break # If we have the right amount of videos, quit looping and continue on
            if subredditPost.url.startswith('https://gfycat.com/'): # Ensure that theyre gfycat clips, might expand to imgur soon
                # Imgur was planned, but scraping clips from there would need a lot of html parsing, so its put on the backburner
                # medium priority TODO
                if self.dataPackage["flairBool"]: # If they requested a specific flair
                    if subredditPost.link_flair_text.lower() != self.dataPackage["flairName"].lower(): # If the post doesnt have the flair
                        continue # skip this loop and try the next one
                self.videoUrlDict[subredditPost.url] = subredditPost.author.name # If you get to here, it either means it has the flair
                # or they didnt request any. either way, snag it

        # Check for the exitance of ./Downloaded Videos/, create if not found

        if self.deleteOldFilesBool:
            self.deleteOldClips()

        self.insertLog("Downloading Clips")
        self.clipCounter, self.clipNumberConversionTable = 1, {} # Initializing variables
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
                self.clipList.append(self.videoClip)
                # If it doesnt need any editing, just put it into the cliplist

        self.insertLog("All Files Loaded Into Memory")

        self.finalDuration = concatenate_videoclips(self.clipList, method='compose').duration # Work out the final duration of the output render
        if self.dataPackage["musicBool"]: # If the user requested music
            self.audioLoop = audio_loop(AudioFileClip(self.dataPackage["musicPath"]), duration=self.finalDuration)
            # Create an audio loop for the duration of the final video
            self.concatenatedVideo = concatenate_videoclips(self.clipList, method='compose').set_audio(self.audioLoop)
            # Stitch together all of the clips and add the music 
        else:
            self.concatenatedVideo = concatenate_videoclips(self.clipList, method='compose')
            # No need to add music, as they didnt want it. Sitch together all of the clips

        self.insertLog("Starting Render Process\n This could take a while...") # Let the user know somethings actually happening
        self.insertLog("Using {0} threads".format(self.dataPackage["threadCount"]))
        self.concatenatedVideo.write_videofile(self.dataPackage["outputRenderName"], fps=self.dataPackage["framesPerSecond"], logger=None, threads=self.dataPackage["threadCount"])
        # Render the video, name it what the user wanted and set the fps they reqested

        self.insertLog("Video Rendered")

    def deleteOldClips(self):
        self.clipList = glob.glob("./Downloaded Videos/Clip*.mp4")
        for clip in self.clipList:
            os.remove(clip)


root = Tk()
root.geometry("1100x530")
apps = Window(root)
#root.iconbitmap(filepath/to/icon)
# For adding icon when its finished
root.mainloop()