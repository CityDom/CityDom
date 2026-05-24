default citydom_gallery_closing = False
default citydom_gallery_preview = None
default citydom_gallery_preview_closing = False
default citydom_gallery_scroll_target = 0.0
default citydom_gallery_scroll_active = False

init python:
    CITYDOM_GALLERY_SCROLL_STEP = 78.0
    CITYDOM_GALLERY_SCROLL_EASE = 0.13

    def citydom_gallery_adjustment_max(adj):
        return max(0.0, float(getattr(adj, "range", 0.0)))

    def citydom_gallery_change_adjustment(adj, value):
        try:
            adj.change(value)
        except Exception:
            adj.value = value

    def citydom_gallery_wheel(adj, delta):
        max_value = citydom_gallery_adjustment_max(adj)
        target = getattr(store, "citydom_gallery_scroll_target", float(getattr(adj, "value", 0.0)))
        store.citydom_gallery_scroll_target = max(0.0, min(max_value, target + delta))
        store.citydom_gallery_scroll_active = True
        renpy.restart_interaction()

    def citydom_gallery_smooth_scroll(adj):
        if not getattr(store, "citydom_gallery_scroll_active", False):
            store.citydom_gallery_scroll_target = float(getattr(adj, "value", 0.0))
            return

        max_value = citydom_gallery_adjustment_max(adj)
        target = max(0.0, min(max_value, float(getattr(store, "citydom_gallery_scroll_target", 0.0))))
        current = float(getattr(adj, "value", 0.0))
        diff = target - current

        if abs(diff) < 0.6:
            citydom_gallery_change_adjustment(adj, target)
            store.citydom_gallery_scroll_active = False
            return

        citydom_gallery_change_adjustment(adj, current + (diff * CITYDOM_GALLERY_SCROLL_EASE))
        renpy.restart_interaction()

    def citydom_gallery_back_to_phone():
        store.ShowPhone = True
        store.citydom_phone_opening = False
        store.citydom_phone_closing = False
        store.citydom_phone_close_target = None
        store.citydom_phone_home_returning = True
        store.citydom_gallery_closing = True
        store.citydom_gallery_preview_closing = False
        renpy.restart_interaction()

    def citydom_gallery_finish_close():
        store.showWallpaperScreen = False
        store.citydom_gallery_closing = False
        store.citydom_gallery_preview = None
        store.citydom_gallery_preview_closing = False
        renpy.restart_interaction()

    def citydom_gallery_set_preview(preview):
        store.citydom_gallery_preview = preview
        store.citydom_gallery_preview_closing = False
        store.previewImage = preview
        store.backFromBackgroundPreview = True
        store.saveAsBackgroundCheck = True
        renpy.restart_interaction()

    def citydom_gallery_close_preview():
        store.citydom_gallery_preview_closing = True
        renpy.restart_interaction()

    def citydom_gallery_finish_preview_close():
        store.citydom_gallery_preview = None
        store.citydom_gallery_preview_closing = False
        renpy.restart_interaction()

    def citydom_gallery_apply_preview():
        if store.citydom_gallery_preview:
            store.setBackgroundPhoto = store.citydom_gallery_preview
        citydom_gallery_close_preview()

transform citydom_gallery_screen_show:
    subpixel True
    alpha 0.0
    xoffset 340
    warp citydom_hud_curve 0.32 alpha 1.0 xoffset 0

transform citydom_gallery_screen_hide:
    subpixel True
    alpha 1.0
    xoffset 0
    warp citydom_hud_curve 0.30 alpha 0.0 xoffset 340

transform citydom_gallery_thumb_motion(index=0):
    subpixel True
    on show:
        alpha 0.0
        zoom 0.90
        pause 0.06 + (index * 0.045)
        warp citydom_hud_curve 0.25 alpha 1.0 zoom 1.0
    on hover:
        warp citydom_hud_curve 0.16 zoom 1.04 yoffset -2
    on idle:
        warp citydom_hud_curve 0.16 zoom 1.0 yoffset 0

transform citydom_gallery_preview_show:
    subpixel True
    alpha 0.0
    zoom 0.985
    yoffset 14
    warp citydom_hud_curve 0.30 alpha 1.0 zoom 1.0 yoffset 0

transform citydom_gallery_preview_hide:
    subpixel True
    alpha 1.0
    zoom 1.0
    yoffset 0
    warp citydom_hud_curve 0.24 alpha 0.0 zoom 0.985 yoffset 14

style citydom_gallery_title_text is citydom_inventory_title_text

style citydom_gallery_subtitle_text is citydom_inventory_count_text

style citydom_gallery_preview_label_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 10
    color "#f0dcffe6"
    outlines [ ]
    kerning 3

screen citydom_gallery_thumb(name, preview, index):
    $ _col = index % 2
    $ _row = index // 2
    $ _x = _col * 154
    $ _y = _row * 194
    button:
        xpos _x
        ypos _y
        xysize (134, 182)
        background None
        hover_background None
        at citydom_gallery_thumb_motion(index)
        action Function(citydom_gallery_set_preview, preview)

        fixed:
            xysize (134, 182)
            add AlphaMask(im.Scale(im.Crop("PhoneBackground/%s" % preview, (26, 0, 282, 384)), 134, 182), "gui/citydom_ui_v2/phone_gallery_thumb_mask.png")
            add "gui/citydom_ui_v2/phone_gallery_thumb_frame.png"

screen gallery_screen():
    default gallery_yadj = ui.adjustment()

    $ init_background_buttons()
    $ _wallpapers = [(name, preview) for name, preview in get_wallpaper_previews().items() if background_buttons.get(name + "Background", False)]

    if citydom_gallery_closing:
        timer 0.32 action Function(citydom_gallery_finish_close)

    if citydom_gallery_preview_closing:
        timer 0.24 action Function(citydom_gallery_finish_preview_close)

    if not citydom_gallery_preview:
        key "mousedown_4" action Function(citydom_gallery_wheel, gallery_yadj, -CITYDOM_GALLERY_SCROLL_STEP)
        key "mousedown_5" action Function(citydom_gallery_wheel, gallery_yadj, CITYDOM_GALLERY_SCROLL_STEP)
        timer 0.012 repeat True action Function(citydom_gallery_smooth_scroll, gallery_yadj)

    if not ShowPhone:
        fixed:
            at citydom_phone_overlay_static
            add "gui/citydom_ui_v2/phone_overlay_dim.png"

    fixed:
        xpos CITYDOM_PHONE_X + (CITYDOM_PHONE_W // 2)
        ypos CITYDOM_PHONE_Y + (CITYDOM_PHONE_H // 2)
        xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
        at citydom_phone_frame_static

        viewport:
            xpos 0
            ypos 0
            xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
            draggable False
            mousewheel False
            scrollbars None
            child_size (CITYDOM_PHONE_W, CITYDOM_PHONE_H)

            fixed:
                xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
                if citydom_gallery_closing:
                    at citydom_gallery_screen_hide
                else:
                    at citydom_gallery_screen_show

                if citydom_gallery_preview:
                    add AlphaMask("gui/citydom_ui_v2/phone_gallery_bg.png", "gui/citydom_ui_v2/phone_rounded_mask.png")

                    fixed:
                        xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
                        if citydom_gallery_preview_closing:
                            at citydom_gallery_preview_hide
                        else:
                            at citydom_gallery_preview_show

                        add AlphaMask(im.Scale(im.Crop("PhoneBackground/%s" % citydom_gallery_preview, (5, 26, 324, 648)), CITYDOM_PHONE_W, CITYDOM_PHONE_H), "gui/citydom_ui_v2/phone_rounded_mask.png")

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
                                action Function(citydom_gallery_close_preview)
                            imagebutton:
                                idle "gui/citydom_ui_v2/phone_gallery_check_idle.png"
                                hover "gui/citydom_ui_v2/phone_gallery_check_hover.png"
                                action Function(citydom_gallery_apply_preview)

                        fixed:
                            xpos 60
                            ypos 608
                            xysize (220, 34)
                            add "gui/citydom_ui_v2/phone_gallery_preview_label.png"
                            $ _preview_name = next((name for name, preview in _wallpapers if preview == citydom_gallery_preview), "")
                            text _preview_name.upper():
                                xalign 0.5
                                yalign 0.5
                                style "citydom_gallery_preview_label_text"

                else:
                    add AlphaMask("gui/citydom_ui_v2/phone_gallery_bg.png", "gui/citydom_ui_v2/phone_rounded_mask.png")

                    imagebutton:
                        idle "gui/citydom_ui_v2/phone_inventory_back_idle.png"
                        hover "gui/citydom_ui_v2/phone_inventory_back_hover.png"
                        xpos 20
                        ypos 54
                        action Function(citydom_gallery_back_to_phone)

                    text _("Gallery"):
                        xcenter 170
                        ypos 56
                        style "citydom_gallery_title_text"

                    text _("Backgrounds").upper():
                        xcenter 170
                        ypos 80
                        style "citydom_gallery_subtitle_text"

                    add "gui/citydom_ui_v2/chain_divider_phone.png":
                        xcenter 170
                        ypos 112

                    viewport:
                        xpos 18
                        ypos 142
                        xysize (304, 500)
                        mousewheel False
                        draggable True
                        scrollbars None
                        yadjustment gallery_yadj

                        fixed:
                            xysize (304, max(500, (((len(_wallpapers) + 1) // 2) * 194)))

                            for index, (name, preview) in enumerate(_wallpapers):
                                use citydom_gallery_thumb(name, preview, index)

        add "gui/citydom_ui_v2/phone_frame_overlay.png"

        add "gui/citydom_ui_v2/phone_dynamic_island.png":
            xpos 126
            ypos 14

        add "gui/citydom_ui_v2/phone_status_pill.png":
            xpos 20
            ypos 8

        text citydom_phone_time_text():
            xpos 31
            ypos 13
            style "citydom_phone_status_text"

        add "gui/citydom_ui_v2/phone_status_icons_pill.png":
            xpos 248
            ypos 8
