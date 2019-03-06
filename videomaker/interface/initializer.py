from videomaker.interface.button.button import initButton
from videomaker.interface.optionbox.optionbox import initOptionmenu
from videomaker.interface.spinbox.spinbox import initSpinbox
from videomaker.interface.window.window import initListboxes
from videomaker.interface.progressbar.progressbar import initProgressbars
from videomaker.interface.menu.menu import initMenubar
from videomaker.interface.checkbutton.checkbutton import initCheckboxes
from videomaker.interface.entry.entry import initEntryBoxes

def initWindow(focus):
    initEntryBoxes(focus)
    initButton(focus)
    initOptionmenu(focus)
    initSpinbox(focus)
    initListboxes(focus)
    initProgressbars(focus)
    initMenubar(focus)
    initCheckboxes(focus)