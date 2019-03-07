from videomaker.functions.packageData import packageData
import threading

def startThread(focus):
    # Start thread for the rest of the verifying and rendering so the main window doesnt freeze
    focus.thread = threading.Thread(target=packageData, args=(focus,))
    focus.thread.daemon = True # So the render stops if the user closes the program
    focus.thread.start()
