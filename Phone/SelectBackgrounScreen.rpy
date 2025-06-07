screen gallery_screen():
    frame:
        xpos 1550
        ypos 100
        background "BackgroundsScreen.png"
        text "Backgrounds":
            xpos 15
            ypos 25
        viewport:
            xpos 9
            ypos 70
            draggable True
            mousewheel True
            area (9, 70, 330, 600)
            vbox:
                spacing 10
                
                $ unlocked_backgrounds = {name: preview for name, preview in get_wallpaper_previews().items() if background_buttons.get(name + "Background", False)}
                $ num_items = len(unlocked_backgrounds)
                $ items_per_row = 3
                $ rows_needed = (num_items + items_per_row - 1) // items_per_row
                for row in range(rows_needed):
                    hbox:
                        spacing 5
                        for col in range(items_per_row):
                            $ index = row * items_per_row + col
                            if index >= num_items:
                                break
                            $ name = list(unlocked_backgrounds.keys())[index]
                            $ preview = unlocked_backgrounds[name]
                            $ button_image_path = "BackgroundButtons/BackgroundButton_{}_idle.png".format(name)
                            frame:
                                background None
                                padding (1, 1)
                                fixed:
                                    area (0, 0, 95, 95)
                                    imagebutton:
                                        idle Transform(button_image_path, size=(95, 95), zoom=1.0)
                                        hover Transform(button_image_path, size=(95, 95), zoom=1.05)
                                        action [
                                            SetVariable("previewImage", preview), 
                                            SetVariable("showWallpaperPreview", True), 
                                            SetVariable("backFromBackgroundPreview", True), 
                                            SetVariable("saveAsBackgroundCheck", True), 
                                        ]
        imagebutton:
            idle "back_idle.png"
            xpos 280
            ypos 30
            action [SetVariable("ShowPhone", True),
                    SetVariable("showWallpaperScreen", False)]
