default citydom_wallpaper_preview_closing = False

init python:
    def citydom_wallpaper_preview_close():
        store.citydom_wallpaper_preview_closing = True
        renpy.restart_interaction()

    def citydom_wallpaper_preview_finish_close():
        store.showWallpaperPreview = False
        store.citydom_wallpaper_preview_closing = False
        store.canDownload = False
        store.backFromBackgroundPreview = False
        store.backFromBackgroundSave = False
        renpy.restart_interaction()

    def citydom_wallpaper_preview_apply():
        store.setBackgroundPhoto = store.previewImage
        store.showWallpaperPreview = False
        store.citydom_wallpaper_preview_closing = False
        store.showWallpaperScreen = False
        store.ShowPhone = True
        renpy.restart_interaction()

transform citydom_wallpaper_preview_show:
    subpixel True
    alpha 0.0
    zoom 0.985
    yoffset 14
    warp citydom_hud_curve 0.30 alpha 1.0 zoom 1.0 yoffset 0

transform citydom_wallpaper_preview_hide:
    subpixel True
    alpha 1.0
    zoom 1.0
    yoffset 0
    warp citydom_hud_curve 0.24 alpha 0.0 zoom 0.985 yoffset 14

screen WallPaperPreview_screen():
    $ _preview = previewImage if previewImage else "WallpaperPreview_Default.png"

    if citydom_wallpaper_preview_closing:
        timer 0.24 action Function(citydom_wallpaper_preview_finish_close)

    fixed:
        xpos CITYDOM_PHONE_X + (CITYDOM_PHONE_W // 2)
        ypos CITYDOM_PHONE_Y + (CITYDOM_PHONE_H // 2)
        xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
        at citydom_phone_frame_static

        fixed:
            xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
            if citydom_wallpaper_preview_closing:
                at citydom_wallpaper_preview_hide
            else:
                at citydom_wallpaper_preview_show

            add AlphaMask(im.Scale(im.Crop("PhoneBackground/%s" % _preview, (5, 26, 324, 648)), CITYDOM_PHONE_W, CITYDOM_PHONE_H), "gui/citydom_ui_v2/phone_rounded_mask.png")

            button:
                xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
                background None
                hover_background None
                action NullAction()

            vbox:
                xpos 288
                ypos 56
                spacing 8
                imagebutton:
                    idle "gui/citydom_ui_v2/phone_gallery_close_idle.png"
                    hover "gui/citydom_ui_v2/phone_gallery_close_hover.png"
                    action Function(citydom_wallpaper_preview_close)

                if saveAsBackgroundCheck:
                    imagebutton:
                        idle "gui/citydom_ui_v2/phone_gallery_check_idle.png"
                        hover "gui/citydom_ui_v2/phone_gallery_check_hover.png"
                        action Function(citydom_wallpaper_preview_apply)
                elif canDownload:
                    imagebutton:
                        idle "gui/citydom_ui_v2/phone_gallery_check_idle.png"
                        hover "gui/citydom_ui_v2/phone_gallery_check_hover.png"
                        action [Function(unlockBackground), SetVariable("backFromBackgroundSave", False), SetVariable("canDownload", False)]

        use citydom_phone_status_layer
