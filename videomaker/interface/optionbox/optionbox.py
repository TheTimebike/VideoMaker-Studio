from tkinter import *

def initOptionmenu(focus):
    focus.subredditSearchMethodString = StringVar() # Once again, tkinter needs its own special variables
    focus.subredditSearchMethodString.set("entirety of time") # Default
    focus.subredditSearchMethod = OptionMenu(focus.master, focus.subredditSearchMethodString, 
    "entirety of time", # Different entries in the list
    "the last year", # Each one determines the subreddit search type
    "the last month", # Might include support for hot, new and rising categories
    "the last week", # Would require a second option menu
    "the last day", 
    "the last hour") 

    focus.subredditSearchMethod.place(x=240, y=390)
    # Optionmenu deviates from the x=50 rule, this is because its positioned after this text \/
    focus.subredditSearchLabelBefore = Label(focus.master, text="VM will search for posts within the")
    # You can see that the text is placed at x=50, and the optionbox is placed after the text ends.
    focus.subredditSearchLabelBefore.place(x=50, y=395)
