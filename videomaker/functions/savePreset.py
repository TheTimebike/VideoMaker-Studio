import json
from videomaker.functions.packageData import packageData

def savePreset(focus):
    preset = packageData(focus, verify=False)
    with open(preset["subredditName"], "w+") as out:
        json.dump(preset, out, indent=4)
