init python:
    def get_wallpaper_previews():
        return {
            "Default": "WallpaperPreview_Default.png",
            "Jennifer": "WallpaperPreview_Jennifer.png",
            "Isabella": "WallpaperPreview_Isabella.png",
            "Claire": "WallpaperPreview_Claire.png",
            "Mhyrorin": "WallpaperPreview_Mhyrorin.png",
            "Maria": "WallpaperPreview_Maria.png",
            "Scarlet": "WallpaperPreview_Scarlet.png",
            "ScarletLingerie": "WallpaperPreview_Lingerie_Scarlet.png",
        }

    def init_background_buttons():
        for name in get_wallpaper_previews().keys():
            key = name + "Background"
            if key not in renpy.store.background_buttons:
                renpy.store.background_buttons[key] = (name == "Default")
        renpy.store.background_buttons["DefaultBackground"] = True

    def handleBackgroundPreview(chat_name):
        previews = get_wallpaper_previews()
        preview_image = previews.get(chat_name, "")

        renpy.store.previewImage = preview_image if preview_image else "WallpaperPreview_Default.png"

        renpy.store.showWallpaperPreview = True
        renpy.store.canDownload = True
        renpy.store.saveAsBackgroundCheck = False
        renpy.store.backFromBackgroundSave = True

    def unlockBackground():
        global previewImage

        previewImageFilename = previewImage.split("/")[-1]

        matchedKey = None
        for key, value in get_wallpaper_previews().items():
            if value == previewImageFilename:
                matchedKey = key + "Background"
                break

        if matchedKey:
            background_buttons[matchedKey] = True
            renpy.store.showWallpaperPreview = False
            renpy.store.showWallpaperScreen = True
            renpy.store.canDownload = False
            renpy.redraw(None, 0)
        else:
            renpy.error("Preview image does not match any known backgrounds: " + previewImageFilename)

    def toggle_schedule():
        global is_weekend_schedule
        is_weekend_schedule = not is_weekend_schedule

    def get_field(character, field):
        return renpy.store.__dict__.get("Show{}{}".format(character, field), False)

    def calculate_progress(character):
        love = renpy.store.__dict__.get(character + "_love", 0)
        obedience = renpy.store.__dict__.get(character + "_Obedience", 0)
        corruption = renpy.store.__dict__.get(character + "_Corruption", 0)

        total_progress = love + obedience + corruption
        max_progress = 60
        progress_percentage = (total_progress / max_progress) * 100
        return progress_percentage

    def toggle_char_tab():
        global current_char_tab
        if current_char_tab == 1:
            current_char_tab = 2
        else:
            current_char_tab = 1

    def check_and_update_character_stats(character):
        love = renpy.store.__dict__.get(character + "_love", 0)
        obedience = renpy.store.__dict__.get(character + "_Obedience", 0)
        corruption = renpy.store.__dict__.get(character + "_Corruption", 0)

        if love > 20:
            renpy.store.__dict__[character + "_love"] = 20
        if obedience > 20:
            renpy.store.__dict__[character + "_Obedience"] = 20
        if corruption > 20:
            renpy.store.__dict__[character + "_Corruption"] = 20

        if love < 0:
            renpy.store.__dict__[character + "_love"] = 0
        if obedience < 0:
            renpy.store.__dict__[character + "_Obedience"] = 0
        if corruption < 0:
            renpy.store.__dict__[character + "_Corruption"] = 0
