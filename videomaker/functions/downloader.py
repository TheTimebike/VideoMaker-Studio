from tkinter import *
import urllib.request
from videomaker.functions.deleteOldClips import deleteOldClips
from videomaker.functions.insertLog import insertLog

def download(focus)
    focus.videoUrlDict = {} # Dictionary to store pairs of clips and authors.
    # post URL is the key and author name is the value
    for subredditPost in focus.subreddit:
        if len(focus.videoUrlDict) > int(focus.dataPackage["downloadCount"]) - 1:
            break # If we have the right amount of videos, quit looping and continue on
        if subredditPost.url.startswith('https://gfycat.com/'): # Ensure that theyre gfycat clips, might expand to imgur soon
            # Imgur was planned, but scraping clips from there would need a lot of html parsing, so its put on the backburner
            # medium priority TODO
            if focus.dataPackage["flairBool"]: # If they requested a specific flair
                if subredditPost.link_flair_text.lower() != focus.dataPackage["flairName"].lower(): # If the post doesnt have the flair
                    continue # skip this loop and try the next one
            focus.videoUrlDict[subredditPost.url] = subredditPost.author.name # If you get to here, it either means it has the flair
            # or they didnt request any. either way, snag it

    # Check for the exitance of ./Downloaded Videos/, create if not found

    if focus.deleteOldFilesBool:
        deleteOldClips()

    insertLog(focus, "Downloading Clips")
    focus.clipCounter, focus.clipNumberConversionTable = 1, {} # Initializing variables
    for videoUrl, videoCreator in focus.videoUrlDict.items():
        focus.parsedUrl = "https://giant.gfycat.com/" + str(videoUrl).split("/")[3] + ".mp4" # Converts regular gfycat links to
        # giant versions, which can be downloaded easier with urllib.request
        urllib.request.urlretrieve(focus.parsedUrl, './Downloaded Videos/Clip{0}.mp4'.format(focus.clipCounter))
        # Download clip to ./Downloaded Videos/
        focus.downloadProgressBar["value"] += 100/int(focus.dataPackage["downloadCount"])
        # Figure out the percentage of videos downloaded, then add it to the progressbar value
        # This is the weird-ness with the ttk objects I mentioned earler, acts as a dict rather than an object.
        focus.clipNumberConversionTable[str(focus.clipCounter)] = videoCreator
        # Uses a conversion table so the clip author can be found using the clip number
        focus.clipCounter += 1

    insertLog(focus, "Downloaded Clips")