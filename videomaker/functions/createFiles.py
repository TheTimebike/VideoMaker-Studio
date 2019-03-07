import sys, os

def createDirectories():
    dirList = ["Downloaded Videos", "Audio", "Renders"]
    for pathName in dirList:
        if not os.path.exists("./"+pathName+"/"):
            os.mkdir("./"+pathName+"/")
            
def createFiles():
    if not os.path.isfile("./praw.ini"):
        fileString = """
[DEFAULT]
# A boolean to indicate whether or not to check for package updates.
check_for_updates=True

# Object to kind mappings
comment_kind=t1
message_kind=t4
redditor_kind=t2
submission_kind=t3
subreddit_kind=t5

# The URL prefix for OAuth-related requests.
oauth_url=https://oauth.reddit.com

# The URL prefix for regular requests.
reddit_url=https://www.reddit.com

# The URL prefix for short URLs.
short_url=https://redd.it"""
        with open("praw.ini", "w+") as out:
            out.write(fileString)
