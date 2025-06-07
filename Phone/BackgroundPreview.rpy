init python:
    # Function to unlock the background based on the preview image
    def unlockBackground():
        global previewImage  # Ensure previewImage is accessible globally

        previewImageFilename = previewImage.split("/")[-1]  # Extract filename

        matchedKey = None
        for key, value in get_wallpaper_previews().items():
            if value == previewImageFilename:
                matchedKey = key + "Background"  # Construct the key for background_buttons
                break

        if matchedKey:
            background_buttons[matchedKey] = True
            renpy.store.showWallpaperPreview = False
            renpy.store.showWallpaperScreen = True
            renpy.store.canDownload = False
            renpy.redraw(None, 0)
        else:
            renpy.error("Preview image does not match any known backgrounds: " + previewImageFilename)

screen WallPaperPreview_screen():
    frame:
        xpos 1550
        ypos 100
        if previewImage:
            background "PhoneBackground/{}".format(previewImage)
        else:
            background "PhoneBackground/{}".format(default_wallpaper_preview)

        if backFromBackgroundPreview:
            imagebutton:
                idle "back_idle.png"
                xpos 280 
                ypos 30 
                action [SetVariable("showWallpaperPreview", False),
                        SetVariable("showWallpaperScreen", True),
                        SetVariable("canDownload", False),
                        SetVariable("backFromBackgroundPreview", False)]

        if backFromBackgroundSave:
            imagebutton:
                idle "back_idle.png"
                xpos 280 
                ypos 30 
                action [SetVariable("showWallpaperPreview", False),
                        SetVariable("canDownload", False),
                        SetVariable("backFromBackgroundSave", False)]
                    
        if saveAsBackgroundCheck:
            imagebutton:
                idle "Check_idle.png"
                xpos 240 
                ypos 30 
                action [SetVariable("setBackgroundPhoto", previewImage), 
                        SetVariable("showWallpaperPreview", False),
                        SetVariable("showWallpaperScreen", False),
                        SetVariable("ShowPhone", True)]
                
        if canDownload:
            imagebutton:
                idle "Download_idle.png"
                xpos 240
                ypos 30
                action [Function(unlockBackground),
                        SetVariable("backFromBackgroundSave", False),
                        SetVariable("canDownload", False),
                        SetVariable("showWallpaperPreview", False),
                        SetVariable("showWallpaperScreen", False)]
