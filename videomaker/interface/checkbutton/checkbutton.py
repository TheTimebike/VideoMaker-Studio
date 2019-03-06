from tkinter import *

def initCheckboxes(focus):
    focus.deleteOldFilesBool = BooleanVar() # tkinter demands that all variables assigned to inputs have to be
    # *their* variety rather than pythons defaults. Doesnt matter much because I'm just gonna .get() all the variables
    # which converts them to pythons'.
    focus.deleteOldFilesCheckbox = Checkbutton(focus.master, variable=focus.deleteOldFilesBool)
    focus.deleteOldFilesCheckbox.place(x=50, y=240)
    focus.deleteOldFilesLabel = Label(focus.master, text="Delete Old Clips?")
    focus.deleteOldFilesLabel.place(x=75, y=242) # Text placed 2 lower due to the smaller size of the checkbuttons

    focus.giveSubmitterCreditBool = BooleanVar()
    focus.giveSubmitterCreditBool.set("true") # Sets default value to True ( checked ) BooleanVar doesnt take arguments during
    # init so you gotta do it in a seperate command, and you cant do BooleanVar().set() because .set() doesnt return the object
    # it also takes a uncapitalized string of "true" rather than a boolean??? whatever
    focus.giveSubmitterCreditCheckbox = Checkbutton(focus.master, variable=focus.giveSubmitterCreditBool)
    # if you give the checkbutton a booleanvar variable it adopts its state
    focus.giveSubmitterCreditCheckbox.place(x=50, y=265)
    focus.giveSubmitterCreditLabel = Label(focus.master, text="Include Clip Uploaders Username?")
    focus.giveSubmitterCreditLabel.place(x=75, y=267)