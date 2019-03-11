import json, threading
from videomaker.functions.verifyData import verifyData

def startFromFile(focus, path):
    with open(path, "r") as out:
        fileData = json.load(out)
    focus.dataPackage = fileData
    startFromFileThread = threading.Thread(target=verifyData)
    startFromFileThread.start()
