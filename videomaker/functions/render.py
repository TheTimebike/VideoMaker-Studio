from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.AudioClip import AudioClip
from moviepy.video.VideoClip import VideoClip, TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.resize import resize
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.audio.fx.audio_loop import audio_loop
from videomaker.functions.insertLog import insertLog
import os


def render(focus):
    insertLog(focus, "Loading Clips into Memory")
    print(os.getcwd())

    focus.clipList = [] # Creates a holder for the clips that can be stitched together with moviepy
    for videoNumber in range(1, focus.dataPackage["downloadCount"] + 1): # Using a range() iter rather than a dict/list as I need the index
        insertLog(focus, "Loading Clip: {0}".format(videoNumber))
        focus.videoClip = VideoFileClip("./Downloaded Videos/Clip{0}.mp4".format(videoNumber)).fx( resize,(1280, 720)) 
        # Loads file up as a VideoFileClip object, then resizes the clip to be 1280x720
        if focus.dataPackage["giveCredit"]: # If the user wants to give credit to the clip creators
            focus.clipAuthor = focus.clipNumberConversionTable[str(videoNumber)] # Uses the clip number to find the creator
            focus.textClip = TextClip('u/' + focus.clipAuthor, fontsize=30, color='white').set_pos(('left', 'top')).set_duration(focus.videoClip.duration)
            # Creates a TextClip object with "u/" appended before the clip authors name. font size and colour is set to white and 30.
            # The position of the text is set to the top left and is configured to last for the duration of the clip
            focus.editedVideoClip = CompositeVideoClip([focus.videoClip, focus.textClip])
            # Overlays the textClip onto the videoClip
            focus.clipList.append(focus.editedVideoClip)
            # Puts the finished clip into a list for stitching
        else:
            focus.clipList.append(focus.videoClip)
            # If it doesnt need any editing, just put it into the cliplist

    insertLog(focus, "All Files Loaded Into Memory")

    focus.finalDuration = concatenate_videoclips(focus.clipList, method='compose').duration # Work out the final duration of the output render
    if focus.dataPackage["musicBool"]: # If the user requested music
        focus.audioLoop = audio_loop(AudioFileClip("./Audio/"+focus.dataPackage["musicPath"]), duration=focus.finalDuration)
        # Create an audio loop for the duration of the final video
        focus.concatenatedVideo = concatenate_videoclips(focus.clipList, method='compose').set_audio(focus.audioLoop)
        # Stitch together all of the clips and add the music 
    else:
        focus.concatenatedVideo = concatenate_videoclips(focus.clipList, method='compose')
        # No need to add music, as they didnt want it. Sitch together all of the clips

    insertLog(focus, "Starting Render Process\n This could take a while...") # Let the user know somethings actually happening
    insertLog(focus, "Using {0} threads".format(focus.dataPackage["threadCount"]))
    focus.concatenatedVideo.write_videofile("./Renders/"+focus.dataPackage["outputRenderName"], fps=focus.dataPackage["framesPerSecond"], logger=None, threads=focus.dataPackage["threadCount"])
    # Render the video, name it what the user wanted and set the fps they reqested

    insertLog(focus, "Video Rendered")