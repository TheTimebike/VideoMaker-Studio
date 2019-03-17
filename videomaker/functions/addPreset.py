from videomaker.functions.startFromFile import startFromFile
import glob, os, threading, json

def addOption(focus, path, name="Undefined"):
    focus.menuDropdownStartFromFile.add_command(label="Start {0} Preset".format(name), command= lambda: startFromFile(focus, path))
 
def addPreset(focus):
    fileList = glob.glob(os.getcwd() + "/presets/*.json") # Iterates through json files in the directory
    for presetFile in fileList:
        print(presetFile)
        try:
            with open(presetFile, "r") as out:
                data = json.load(out)
            addOption(focus, presetFile, data["subredditName"]) # Adds the option to the view tab
        except Exception as ex:
            print(ex)
            pass
