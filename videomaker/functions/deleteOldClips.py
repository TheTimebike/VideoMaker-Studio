import os, glob

def deleteOldClips():
    clipList = glob.glob("./Downloaded Videos/Clip*.mp4")
    for clip in clipList:
        os.remove(clip)