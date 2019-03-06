import sys, os

def createFiles():
    dirList = ["Downloaded Videos", "Audio", "Renders"]
    for pathName in dirList:
        if not os.path.exists("./"+pathName+"/"):
            os.mkdir("./"+pathName+"/")