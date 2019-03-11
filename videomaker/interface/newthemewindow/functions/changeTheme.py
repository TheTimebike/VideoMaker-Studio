def changeTheme(focus):
    focus.backgroundColour = focus.main.backgroundColour
    focus.boxColour = focus.main.boxColour
    focus.textColour = focus.main.textColour
    
    focus.master.configure(background=focus.backgroundColour)
    
    focus.selectThemeNameBox.configure(background=focus.boxColour)
    focus.selectThemeBackgroundColourBox.configure(background=focus.boxColour)
    focus.selectThemeTextColourBox.configure(background=focus.boxColour)
    focus.selectThemeBoxColourBox.configure(background=focus.boxColour)
    
    focus.selectThemeNameBoxLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
    focus.selectThemeBackgroundColourBoxLabel.configure(background=focus.backgroundColour, foreground=focus.textColour))
    focus.selectThemeTextColourBoxLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
    focus.selectThemeBoxColourBoxLabel.configure(background=focus.backgroundColour, foreground=focus.textColour)
