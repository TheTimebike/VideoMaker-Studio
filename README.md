# VideoMaker-Studio

VideoMaker Studio is the GUI version of the VideoMaker project I had made a while ago. The rendering time for this version has been improved drastically and has added various new functions and options.

The Interface for VideoMaker Studio was created in tkinter, a python module for GUI's and window creation.

If you attempt to compile a version of VMS using Pyinstaller, make sure to bundle the praw.ini file in the .spec file.

## Dependancies

VideoMaker Studio, much like the original VideoMaker, relies on a program called Imagemagick to render its videos. When installing ImageMagick, ensure that you enable the "legacy files" option, as VideoMaker Studio relies on these files.

## Interface

VideoMaker Studio comes with both light and dark mode themes, with the current theme able to be switched under the "View" menu.

### Light Mode
![Light Mode](https://raw.githubusercontent.com/TheTimebike/VideoMaker-Studio/master/images/lightmode.PNG)

### Dark Mode
![Dark Mode](https://raw.githubusercontent.com/TheTimebike/VideoMaker-Studio/master/images/darkmode.PNG)
