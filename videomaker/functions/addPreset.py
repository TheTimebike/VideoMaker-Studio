from videomaker.functions.verifyData import verifyData
import glob, os, threading

def addOption(focus, preset, name):
    focus.menuDropdownStartFromFile.add_command(label="Start {0} Preset".format(name), command= lambda: startThread(focus, preset))
    
def startThread(focus, preset):
    threading.Thread(target=verifyData, args=(focus,preset)).start()
 
def addPreset(focus):
    fileList = glob.glob(os.getcwd() + "/presets/*.json") # Iterates through json files in the directory
    for presetFile in fileList:
        try:
            with open(presetFile, "r") as out:
                preset = json.load(out) # Saves the data in the file to a variable
            addOption(focus, preset, preset["subredditName"]) # Adds the option to the view tab
        except Exception as ex:
          pass
