from tkinter import *
from videomaker.functions.insertLog import insertLog
from videomaker.functions.downloader import download
from videomaker.functions.createFiles import createFiles
import praw

def verifyData(focus):
    createFiles()
    focus.reddit = praw.Reddit(client_id=focus.dataPackage["redditClientID"], client_secret=focus.dataPackage["redditClientSecret"], user_agent='UserAgent')
    # 404 HTTP response == not found
    # 401 HTTP response == invalid keys
    # 503 HTTP response == could not connect to reddit
    focus.timeframeToRedditFormatConversionTable = {
        "entirety of time": "all", 
        "the last year": "year", 
        "the last month": "month", 
        "the last week": "week",
        "the last day": "day",
        "the last hour": "hour"
        } # Long name
    try:
        focus.subreddit = focus.reddit.subreddit(focus.dataPackage["subredditName"]).top(time_filter=focus.timeframeToRedditFormatConversionTable[focus.dataPackage["timeframe"]])
        for x in focus.subreddit: # Quick one iteration loop to see if the tokens/subreddit name is correct
            # A little sloppy and I'll probably revise this once i get the chance, low priority issue
            break
    except Exception as ex:
        insertLog(focus, "Could not find r/" + focus.dataPackage["subredditName"])
        print(ex)
        return

    insertLog(focus, "r/{0} Found".format(focus.dataPackage["subredditName"]))
    download(focus)

