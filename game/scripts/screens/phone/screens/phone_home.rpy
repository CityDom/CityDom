default citydom_phone_opening = False
default citydom_phone_closing = False
default citydom_phone_close_target = None
default citydom_phone_inventory_launching = False
default citydom_phone_gallery_launching = False
default citydom_phone_messages_launching = False
default citydom_phone_calendar_launching = False
default citydom_phone_home_returning = False

init python:
    CITYDOM_PHONE_X = 790
    CITYDOM_PHONE_Y = 200
    CITYDOM_PHONE_W = 340
    CITYDOM_PHONE_H = 680

    def citydom_phone_wallpaper_displayable():
        wallpaper = getattr(store, "setBackgroundPhoto", "WallpaperPreview_Default.png")
        if wallpaper == "WallpaperPreview_Default.png":
            return AlphaMask(
                "gui/citydom_ui_v2/phone_home_bg.png",
                "gui/citydom_ui_v2/phone_rounded_mask.png",
            )

        source = "PhoneBackground/%s" % wallpaper
        return AlphaMask(
            im.Scale(im.Crop(source, (5, 26, 324, 648)), CITYDOM_PHONE_W, CITYDOM_PHONE_H),
            "gui/citydom_ui_v2/phone_rounded_mask.png",
        )

    def citydom_phone_time_text():
        real_hour = to_real_hour(calendar.Hours)
        hour_12_format = real_hour % 12
        hour_12_format = 12 if hour_12_format == 0 else hour_12_format
        am_pm = "AM" if real_hour < 12 or real_hour == 24 else "PM"
        return "%d:00 %s" % (hour_12_format, am_pm)

    def citydom_phone_start_open():
        store.citydom_phone_opening = True
        store.citydom_phone_closing = False
        store.citydom_phone_close_target = None
        store.set_hud_panels(ShowPhone=True)
        renpy.restart_interaction()

    def citydom_phone_finish_open():
        store.citydom_phone_opening = False
        renpy.restart_interaction()

    def citydom_phone_start_close(target=None):
        if not store.ShowPhone:
            return
        store.citydom_phone_opening = False
        store.citydom_phone_closing = True
        store.citydom_phone_close_target = target
        renpy.restart_interaction()

    def citydom_phone_finish_close():
        target = store.citydom_phone_close_target
        store.ShowPhone = False
        store.citydom_phone_closing = False
        store.citydom_phone_close_target = None

        if target == "gallery":
            store.showWallpaperScreen = True
        elif target == "inventory":
            store.ShowInventory = True
        elif target == "messages":
            store.Messanger = True
        elif target == "calendar":
            store.ShowCalendarScreen = True
        elif target == "stats":
            renpy.hide_screen("MainHud")
            renpy.show_screen("StatsScreen")
            renpy.show_screen("character_select_screen")
            store.CharacterSelectionIsShowing = True
            store.StatsScreenShown = True

        renpy.restart_interaction()

    def citydom_phone_finish_inventory_launch():
        store.citydom_phone_inventory_launching = False
        renpy.restart_interaction()

    def citydom_phone_finish_gallery_launch():
        store.citydom_phone_gallery_launching = False
        renpy.restart_interaction()

    def citydom_phone_finish_messages_launch():
        store.citydom_phone_messages_launching = False
        renpy.restart_interaction()

    def citydom_phone_finish_calendar_launch():
        store.citydom_phone_calendar_launching = False
        renpy.restart_interaction()

    def citydom_phone_finish_home_return():
        store.citydom_phone_home_returning = False
        renpy.restart_interaction()

    def citydom_phone_toggle():
        if store.citydom_phone_closing or getattr(store, "citydom_inventory_closing", False) or getattr(store, "citydom_calendar_closing", False):
            return
        if store.ShowConversationScreen:
            store.citydom_chat_closing = True
            store.citydom_messages_closing = True
            renpy.restart_interaction()
        elif store.Messanger:
            store.citydom_messages_closing = True
            renpy.restart_interaction()
        elif store.ShowInventory:
            store.citydom_inventory_closing = True
            renpy.restart_interaction()
        elif store.ShowCalendarScreen:
            store.citydom_calendar_closing = True
            renpy.restart_interaction()
        elif store.showWallpaperScreen:
            store.citydom_gallery_closing = True
            renpy.restart_interaction()
        elif store.ShowPhone:
            citydom_phone_start_close()
        else:
            citydom_phone_start_open()

    def citydom_phone_open_gallery_app():
        store.citydom_phone_opening = False
        store.citydom_phone_closing = False
        store.citydom_phone_close_target = None
        store.citydom_gallery_preview = None
        store.citydom_phone_gallery_launching = True
        store.showWallpaperScreen = True
        renpy.restart_interaction()

    def citydom_phone_open_inventory_app():
        store.citydom_phone_opening = False
        store.citydom_phone_closing = False
        store.citydom_phone_close_target = None
        store.citydom_phone_inventory_launching = True
        store.ShowInventory = True
        renpy.restart_interaction()

    def citydom_phone_open_messages_app():
        store.citydom_phone_opening = False
        store.citydom_phone_closing = False
        store.citydom_phone_close_target = None
        store.citydom_phone_messages_launching = True
        store.Messanger = True
        store.ShowConversationScreen = False
        renpy.restart_interaction()

    def citydom_phone_open_calendar_app():
        store.citydom_phone_opening = False
        store.citydom_phone_closing = False
        store.citydom_phone_close_target = None
        store.citydom_phone_calendar_launching = True
        store.citydom_schedule_selected_day = citydom_schedule_today_key()
        store.ShowCalendarScreen = True
        renpy.restart_interaction()

    CITYDOM_PHONE_APPS = (
        {
            "id": "gallery",
            "x": 54,
            "y": 540,
            "action": Function(citydom_phone_open_gallery_app),
        },
        {
            "id": "stats",
            "x": 142,
            "y": 540,
            "action": Function(citydom_phone_start_close, "stats"),
        },
        {
            "id": "inventory",
            "x": 230,
            "y": 540,
            "action": Function(citydom_phone_open_inventory_app),
        },
        {
            "id": "messages",
            "x": 98,
            "y": 616,
            "action": Function(citydom_phone_open_messages_app),
        },
        {
            "id": "calendar",
            "x": 186,
            "y": 616,
            "action": Function(citydom_phone_open_calendar_app),
        },
    )

transform citydom_phone_overlay_show:
    subpixel True
    alpha 0.0
    linear 0.24 alpha 1.0

transform citydom_phone_overlay_static:
    alpha 1.0

transform citydom_phone_overlay_hide:
    alpha 1.0
    linear 0.24 alpha 0.0

transform citydom_phone_frame_show:
    subpixel True
    anchor (0.5, 0.5)
    alpha 0.0
    zoom 0.88
    yoffset 34
    warp citydom_hud_curve 0.38 alpha 1.0 zoom 1.0 yoffset 0

transform citydom_phone_frame_static:
    subpixel True
    anchor (0.5, 0.5)
    alpha 1.0
    zoom 1.0
    yoffset 0

transform citydom_phone_frame_hide:
    subpixel True
    anchor (0.5, 0.5)
    alpha 1.0
    zoom 1.0
    yoffset 0
    warp citydom_hud_curve 0.30 alpha 0.0 zoom 0.90 yoffset 24

transform citydom_phone_app_motion(index=0):
    subpixel True
    on show:
        alpha 0.0
        yoffset 14
        zoom 0.82
        pause 0.08 + (index * 0.045)
        warp citydom_hud_curve 0.28 alpha 1.0 yoffset 0 zoom 1.0
    on hide:
        warp citydom_hud_curve 0.18 alpha 0.0 yoffset 10 zoom 0.92
    on hover:
        warp citydom_hud_curve 0.16 zoom 1.10 yoffset -3
    on idle:
        warp citydom_hud_curve 0.16 zoom 1.0 yoffset 0

transform citydom_phone_app_return_motion(index=0):
    subpixel True
    on show:
        alpha 0.0
        xoffset -10
        yoffset -10
        zoom 0.82
        pause 0.08 + (index * 0.045)
        warp citydom_hud_curve 0.28 alpha 1.0 xoffset 0 yoffset 0 zoom 1.0
    on hover:
        warp citydom_hud_curve 0.16 zoom 1.10 yoffset -3
    on idle:
        warp citydom_hud_curve 0.16 zoom 1.0 xoffset 0 yoffset 0

transform citydom_phone_home_content_static:
    alpha 1.0

transform citydom_phone_home_content_exit:
    alpha 1.0
    linear 0.22 alpha 0.0

style citydom_phone_status_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 10
    color "#f0dcffe6"
    outlines [ ]

screen citydom_phone_app_button(app, index):
    imagebutton:
        idle "gui/citydom_ui_v2/phone_app_%s_idle.png" % app["id"]
        hover "gui/citydom_ui_v2/phone_app_%s_hover.png" % app["id"]
        xpos app["x"]
        ypos app["y"]
        if citydom_phone_home_returning:
            at citydom_phone_app_return_motion(index)
        else:
            at citydom_phone_app_motion(index)
        action app["action"]

screen citydom_phone_outside_close_zone(x, y, w, h):
    button:
        xpos x
        ypos y
        xysize (w, h)
        background None
        hover_background None
        action If(citydom_phone_closing, NullAction(), Function(citydom_phone_toggle))

screen phone_screen():
    $ init_background_buttons()
    $ update_current_message()
    $ _phone_time = citydom_phone_time_text()

    if citydom_phone_opening:
        timer 0.52 action Function(citydom_phone_finish_open)

    if citydom_phone_closing:
        timer 0.36 action Function(citydom_phone_finish_close)

    if citydom_phone_inventory_launching:
        timer 0.38 action Function(citydom_phone_finish_inventory_launch)

    if citydom_phone_gallery_launching:
        timer 0.38 action Function(citydom_phone_finish_gallery_launch)

    if citydom_phone_messages_launching:
        timer 0.38 action Function(citydom_phone_finish_messages_launch)

    if citydom_phone_calendar_launching:
        timer 0.38 action Function(citydom_phone_finish_calendar_launch)

    if citydom_phone_home_returning:
        timer 0.52 action Function(citydom_phone_finish_home_return)

    fixed:
        if citydom_phone_opening:
            at citydom_phone_overlay_show
        elif citydom_phone_closing:
            at citydom_phone_overlay_hide
        else:
            at citydom_phone_overlay_static
        add "gui/citydom_ui_v2/phone_overlay_dim.png"

    use citydom_phone_outside_close_zone(0, 0, 1920, CITYDOM_PHONE_Y)
    use citydom_phone_outside_close_zone(0, CITYDOM_PHONE_Y + CITYDOM_PHONE_H, 1920, 1080 - CITYDOM_PHONE_Y - CITYDOM_PHONE_H)
    use citydom_phone_outside_close_zone(0, CITYDOM_PHONE_Y, CITYDOM_PHONE_X, CITYDOM_PHONE_H)
    use citydom_phone_outside_close_zone(CITYDOM_PHONE_X + CITYDOM_PHONE_W, CITYDOM_PHONE_Y, 1920 - CITYDOM_PHONE_X - CITYDOM_PHONE_W, CITYDOM_PHONE_H)

    fixed:
        xpos CITYDOM_PHONE_X + (CITYDOM_PHONE_W // 2)
        ypos CITYDOM_PHONE_Y + (CITYDOM_PHONE_H // 2)
        xysize (CITYDOM_PHONE_W, CITYDOM_PHONE_H)
        if citydom_phone_opening:
            at citydom_phone_frame_show
        elif citydom_phone_closing:
            at citydom_phone_frame_hide
        else:
            at citydom_phone_frame_static

        fixed:
            if citydom_phone_inventory_launching or citydom_phone_gallery_launching or citydom_phone_messages_launching or citydom_phone_calendar_launching:
                at citydom_phone_home_content_exit
            else:
                at citydom_phone_home_content_static

            add citydom_phone_wallpaper_displayable()
            add AlphaMask("gui/citydom_ui_v2/phone_home_vignette.png", "gui/citydom_ui_v2/phone_rounded_mask.png")
            add "gui/citydom_ui_v2/phone_frame_overlay.png"

        add "gui/citydom_ui_v2/phone_dynamic_island.png":
            xpos 126
            ypos 14

        add "gui/citydom_ui_v2/phone_status_pill.png":
            xpos 20
            ypos 8

        text _phone_time:
            xpos 31
            ypos 13
            style "citydom_phone_status_text"

        add "gui/citydom_ui_v2/phone_status_icons_pill.png":
            xpos 248
            ypos 8

        fixed:
            if citydom_phone_inventory_launching or citydom_phone_gallery_launching or citydom_phone_messages_launching or citydom_phone_calendar_launching:
                at citydom_phone_home_content_exit
            else:
                at citydom_phone_home_content_static

            for index, app in enumerate(CITYDOM_PHONE_APPS):
                use citydom_phone_app_button(app, index)
