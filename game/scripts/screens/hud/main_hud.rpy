default citydom_hud_sublocs_hiding = False
default citydom_hud_sublocs_showing = False

init python:
    HUD_PANEL_FLAGS = (
        "ShowPhone",
        "ShowInventory",
        "showWallpaperScreen",
        "ShowConversationScreen",
        "ShowCalendarScreen",
        "Messanger",
        "showWallpaperPreview",
        "ShowCallForSidebar",
    )

    def hideEventScreens():
        for screen_name in ALL_EVENT_SCREENS:
            renpy.hide_screen(screen_name)

    def callGameLoop():
        renpy.call("GameLoop")

    def set_hud_panels(**overrides):
        for flag_name in HUD_PANEL_FLAGS:
            setattr(store, flag_name, bool(overrides.get(flag_name, False)))

    def toggle_hud_panel(flag_name):
        next_state = not bool(getattr(store, flag_name))
        set_hud_panels(**{flag_name: next_state})

    def can_use_hud_hotspots():
        return not (
            store.ShowPhone
            or store.Messanger
            or store.ShowConversationScreen
            or store.ShowCalendarScreen
            or store.showWallpaperScreen
            or store.showWallpaperPreview
        )

    def hud_navigation_actions(target):
        return [Function(hideEventScreens), Function(set_hud_panels), Return(target)]

init python:
    def advance_time_or_sleep():
        if is_in_school(LocationID) and is_in_school_hours():
            if school_clock.is_last_period():
                renpy.call("GetOutOfSchoolItsLate")
                return
            calendar.advance_school_periods(1)
            if not is_in_school_hours():
                renpy.call("GetOutOfSchoolItsLate")
                return

        elif is_in_school(LocationID) and not is_in_school_hours():
            renpy.call("GetOutOfSchoolItsLate")

        elif calendar.Hours == 20:
            # It's 8 PM, trigger the sleep event
            renpy.call("SleepEvent")
        
        else:
            # Player is NOT in school
            calendar.AddTime(1)

        # Hide any active event screens
        for screen_name in ALL_EVENT_SCREENS:
            renpy.hide_screen(screen_name)

        # Force location background refresh after event scenes.
        store.calendar.update_period_index()
        store.LocationID = get_location_id(store.Location, store.LocationID)
        store.Location = get_location_name(store.Location)
        store.Location_img = get_location_image_key(store.Location, store.calendar.period_index)
        show_location_background(store.Location_img)

        # Continue the game loop
        renpy.call("GameLoop")


    def sleep_function():
            renpy.call("SleepEventButton")

    def is_in_school(location_id):
        return location_id == 1

    def is_in_school_hours():
        return calendar.is_school_hours()

    def is_in_school_hours_minusONE():
        return calendar.is_school_hours() and calendar.Hours < 11

    def show_map_screen():
        renpy.show_screen("MapScreen")
        renpy.hide_screen("MainHud")
        set_hud_panels()
        store.MapScreenShown = True

    def citydom_hud_start_hide_sublocations():
        store.citydom_hud_sublocs_hiding = True
        store.citydom_hud_sublocs_showing = False
        renpy.restart_interaction()

    def citydom_hud_finish_hide_sublocations():
        store.ShowSublocationIcons = False
        store.citydom_hud_sublocs_hiding = False
        renpy.restart_interaction()

    def citydom_hud_show_sublocations():
        store.ShowSublocationIcons = True
        store.citydom_hud_sublocs_showing = True
        store.citydom_hud_sublocs_hiding = False
        renpy.restart_interaction()

    def citydom_hud_finish_show_sublocations():
        store.citydom_hud_sublocs_showing = False
        renpy.restart_interaction()

    def citydom_hud_curve(t):
        return 1 - pow(1 - t, 3)

    def citydom_hud_time_text():
        real_hour = to_real_hour(calendar.Hours)
        hour_12_format = real_hour % 12
        hour_12_format = 12 if hour_12_format == 0 else hour_12_format
        am_pm = "AM" if real_hour < 12 or real_hour == 24 else "PM"

        if is_in_school(LocationID) and 12 <= school_clock.hour < 18:
            return "%s %s" % (school_clock.Output, am_pm)

        return "%s:00 %s" % (hour_12_format, am_pm)

    def citydom_hud_weekday_text():
        return calendar.WeekDays[int(calendar.Day)]

    def citydom_hud_period_text():
        for _icon, (_start, _end), _label in time_icons:
            if _start <= calendar.Hours < _end:
                return _label.upper()
        return ""

    def citydom_hud_dot_color():
        colors = ("#ff9a5aff", "#ffe36aff", "#66d2ffff", "#f078ffff", "#a56affff", "#c27affff")
        for index, (_icon, (_start, _end), _label) in enumerate(time_icons):
            if _start <= calendar.Hours < _end:
                return colors[min(index, len(colors) - 1)]
        return "#6f50cce6"

    HUD_ACTION_SIZE = 44
    HUD_ACTION_GAP = 8
    HUD_ACTION_TOP = 20
    HUD_ACTION_START_X = 1920 - 20 - (HUD_ACTION_SIZE * 5) - (HUD_ACTION_GAP * 4)
    HUD_TOP_ICON_POSITIONS = {
        "skip": (HUD_ACTION_START_X, HUD_ACTION_TOP),
        "sleep": (HUD_ACTION_START_X + (HUD_ACTION_SIZE + HUD_ACTION_GAP), HUD_ACTION_TOP),
        "call": (HUD_ACTION_START_X + (HUD_ACTION_SIZE + HUD_ACTION_GAP) * 2, HUD_ACTION_TOP),
        "phone": (HUD_ACTION_START_X + (HUD_ACTION_SIZE + HUD_ACTION_GAP) * 3, HUD_ACTION_TOP),
        "map": (HUD_ACTION_START_X + (HUD_ACTION_SIZE + HUD_ACTION_GAP) * 4, HUD_ACTION_TOP),
    }
    HUD_SUBLOC_SIZE = 76
    HUD_SUBLOC_GAP = 15
    HUD_SUBLOC_ARROW_SIZE = 36
    HUD_SUBLOC_YCENTER = 1022
    HUD_BACK_BUTTON_X = 1920 - 20 - HUD_SUBLOC_ARROW_SIZE
    HUD_BACK_BUTTON_Y = HUD_SUBLOC_YCENTER - (HUD_SUBLOC_ARROW_SIZE // 2)
    HUD_SUBLOC_HIDDEN_X = 20

screen hud_top_icon_button(icon, action, xpos, ypos, active=False, disabled=False):
    $ idle_state = "disabled" if disabled else ("active" if active else "idle")
    $ hover_state = "disabled" if disabled else ("active" if active else "hover")
    $ idle_image = "gui/citydom_ui_v2/hud_action_%s_%s.png" % (icon, idle_state)
    $ hover_image = "gui/citydom_ui_v2/hud_action_%s_%s.png" % (icon, hover_state)
    imagebutton:
        idle idle_image
        hover hover_image
        xpos xpos
        ypos ypos
        at citydom_hud_action_motion
        action action

transform citydom_hud_action_motion:
    subpixel True
    on show:
        alpha 0.0
        yoffset -8
        warp citydom_hud_curve 0.36 alpha 1.0 yoffset 0
    on hover:
        warp citydom_hud_curve 0.18 zoom 1.08
    on idle:
        warp citydom_hud_curve 0.18 zoom 1.0

transform citydom_hud_time_show:
    subpixel True
    alpha 0.0
    xoffset -12
    yoffset -6
    warp citydom_hud_curve 0.40 alpha 1.0 xoffset 0 yoffset 0

transform citydom_hud_subloc_static:
    subpixel True
    on hover:
        warp citydom_hud_curve 0.18 zoom 1.08 yoffset -4
    on idle:
        warp citydom_hud_curve 0.18 zoom 1.0 yoffset 0

transform citydom_hud_subloc_enter(index=0):
    subpixel True
    alpha 0.0
    yoffset 44
    zoom 1.0
    pause index * 0.035
    warp citydom_hud_curve 0.34 alpha 1.0 yoffset 0
    on hover:
        warp citydom_hud_curve 0.18 zoom 1.08 yoffset -4
    on idle:
        warp citydom_hud_curve 0.18 zoom 1.0 yoffset 0

transform citydom_hud_subloc_exit(index=0, count=1):
    subpixel True
    alpha 1.0
    yoffset 0
    zoom 1.0
    pause (count - index - 1) * 0.035
    warp citydom_hud_curve 0.30 alpha 0.0 yoffset 44

transform citydom_hud_arrow_motion:
    subpixel True
    on show:
        alpha 0.0
        xoffset -12
        warp citydom_hud_curve 0.28 alpha 1.0 xoffset 0
    on hide:
        warp citydom_hud_curve 0.20 alpha 0.0 xoffset -12
    on hover:
        warp citydom_hud_curve 0.18 zoom 1.06 xoffset -2
    on idle:
        warp citydom_hud_curve 0.18 zoom 1.0 xoffset 0

transform citydom_hud_hide_subloc_arrow_static:
    subpixel True
    anchor (0.5, 0.5)
    rotate 0
    on hover:
        warp citydom_hud_curve 0.18 zoom 1.06 xoffset -2
    on idle:
        warp citydom_hud_curve 0.18 zoom 1.0 xoffset 0

transform citydom_hud_hide_subloc_arrow_enter(end_x=0):
    subpixel True
    anchor (0.5, 0.5)
    alpha 0.0
    xpos HUD_SUBLOC_HIDDEN_X + (HUD_SUBLOC_ARROW_SIZE // 2)
    rotate 180
    warp citydom_hud_curve 0.38 alpha 1.0 xpos end_x rotate 0
    on hover:
        warp citydom_hud_curve 0.18 zoom 1.06 xoffset -2
    on idle:
        warp citydom_hud_curve 0.18 zoom 1.0 xoffset 0

transform citydom_hud_hide_subloc_arrow_exit:
    subpixel True
    anchor (0.5, 0.5)
    rotate 0
    pause 0.06
    warp citydom_hud_curve 0.38 xpos (HUD_SUBLOC_HIDDEN_X + (HUD_SUBLOC_ARROW_SIZE // 2)) xoffset 0 rotate 180

transform citydom_hud_show_subloc_arrow_motion(end_x=0):
    subpixel True
    anchor (0.5, 0.5)
    rotate 180
    on show:
        alpha 1.0
        xoffset 0
        rotate 180
    on hide:
        warp citydom_hud_curve 0.38 xpos end_x rotate 0 alpha 1.0
    on hover:
        warp citydom_hud_curve 0.18 zoom 1.06 xoffset 2
    on idle:
        warp citydom_hud_curve 0.18 zoom 1.0 xoffset 0

style citydom_hud_day_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 9
    color "#ff8df8"
    outlines [ (1, "#7d1bb380", 0, 0) ]
    kerning 4

style citydom_hud_time_text is default:
    font "fonts/citydom_ui/CinzelDecorative-Regular.ttf"
    size 13
    color "#ffe6fb"
    outlines [ (1, "#ff5bd680", 0, 0) ]
    kerning 1

style citydom_hud_period_text is default:
    font "fonts/citydom_ui/Raleway.ttf"
    size 8
    color "#ff9df8"
    outlines [ (1, "#7d1bb380", 0, 0) ]
    kerning 2

screen citydom_hud_time_widget():
    $ _hud_day = citydom_hud_weekday_text().upper()
    $ _hud_time = citydom_hud_time_text()
    $ _hud_period = citydom_hud_period_text()
    $ _hud_dot = citydom_hud_dot_color()
    fixed:
        xpos 20
        ypos 14
        xysize (360, 48)
        at citydom_hud_time_show

        add "gui/citydom_ui_v2/hud_time_pill.png"

        text "●":
            xpos 17
            ypos 14
            size 16
            color _hud_dot
            outlines [ ]

        text _hud_day:
            xpos 42
            ypos 18
            style "citydom_hud_day_text"

        add Solid("#ff82f0a6"):
            xpos 154
            ypos 17
            xysize (1, 14)

        text _hud_time:
            xpos 171
            ypos 15
            style "citydom_hud_time_text"

        text _hud_period:
            xpos 286
            ypos 19
            style "citydom_hud_period_text"

screen citydom_hud_sublocation_row(current_sublocs):
    $ _active_sublocs = [subloc for subloc in current_sublocs if subloc.active]
    $ _count = len(_active_sublocs)
    $ _total_width = HUD_SUBLOC_ARROW_SIZE + HUD_SUBLOC_GAP + (HUD_SUBLOC_SIZE * _count) + (HUD_SUBLOC_GAP * max(0, _count - 1))
    $ _start_x = int((1920 - 80 - _total_width) / 2)
    $ _row_y = HUD_SUBLOC_YCENTER - (HUD_SUBLOC_SIZE // 2)
    $ _arrow_y = HUD_SUBLOC_YCENTER - (HUD_SUBLOC_ARROW_SIZE // 2)
    $ _arrow_center_x = _start_x + (HUD_SUBLOC_ARROW_SIZE // 2)

    if citydom_hud_sublocs_hiding:
        timer 0.76 action Function(citydom_hud_finish_hide_sublocations)

    if citydom_hud_sublocs_showing:
        timer 0.76 action Function(citydom_hud_finish_show_sublocations)

    imagebutton:
        idle "gui/citydom_ui_v2/hud_arrow_left_idle.png"
        hover "gui/citydom_ui_v2/hud_arrow_left_hover.png"
        xpos _arrow_center_x
        ypos _arrow_y + (HUD_SUBLOC_ARROW_SIZE // 2)
        if citydom_hud_sublocs_hiding:
            at citydom_hud_hide_subloc_arrow_exit
        elif citydom_hud_sublocs_showing:
            at citydom_hud_hide_subloc_arrow_enter(_arrow_center_x)
        else:
            at citydom_hud_hide_subloc_arrow_static
        action If(citydom_hud_sublocs_hiding, NullAction(), Function(citydom_hud_start_hide_sublocations))

    for index, subloc in enumerate(_active_sublocs):
        $ img_idle, img_hover, icon_size = get_subloc_hud_icons(subloc, calendar.Hours)
        $ _item_x = _start_x + HUD_SUBLOC_ARROW_SIZE + HUD_SUBLOC_GAP + (index * (HUD_SUBLOC_SIZE + HUD_SUBLOC_GAP))
        imagebutton:
            idle Transform(img_idle, xysize=(HUD_SUBLOC_SIZE, HUD_SUBLOC_SIZE))
            hover Transform(img_hover, xysize=(HUD_SUBLOC_SIZE, HUD_SUBLOC_SIZE))
            xpos _item_x
            ypos _row_y
            if citydom_hud_sublocs_hiding:
                at citydom_hud_subloc_exit(index, _count)
            elif citydom_hud_sublocs_showing:
                at citydom_hud_subloc_enter(index)
            else:
                at citydom_hud_subloc_static
            focus_mask True
            action hud_navigation_actions(subloc.name)

screen citydom_hud_show_sublocations_button(current_sublocs):
    $ _active_sublocs = [subloc for subloc in current_sublocs if subloc.active]
    $ _count = len(_active_sublocs)
    $ _total_width = HUD_SUBLOC_ARROW_SIZE + HUD_SUBLOC_GAP + (HUD_SUBLOC_SIZE * _count) + (HUD_SUBLOC_GAP * max(0, _count - 1))
    $ _start_x = int((1920 - 80 - _total_width) / 2)
    $ _end_x = _start_x + (HUD_SUBLOC_ARROW_SIZE // 2)
    imagebutton:
        idle "gui/citydom_ui_v2/hud_arrow_left_idle.png"
        hover "gui/citydom_ui_v2/hud_arrow_left_hover.png"
        xpos HUD_SUBLOC_HIDDEN_X + (HUD_SUBLOC_ARROW_SIZE // 2)
        ypos HUD_BACK_BUTTON_Y + (HUD_SUBLOC_ARROW_SIZE // 2)
        at citydom_hud_show_subloc_arrow_motion(_end_x)
        action Function(citydom_hud_show_sublocations)

screen MainHud():

    

    # # Lightweight periodic refresh; does NOT advance game time
    # default _hud_tick = 0
    # timer 0.75 action SetScreenVariable("_hud_tick", _hud_tick + 1) repeat True
#  invisible door buttons
    if can_use_hud_hotspots() and Location_img in invisible_door_button_mappings:
        $ button_data = invisible_door_button_mappings[Location_img]
        for button in button_data:
            imagebutton:
                idle button["idle"]
                hover resolve_tinted_button_hover(button)
                xpos button["xpos"]
                ypos button["ypos"]
                action button["action"]
                focus_mask True
    $ current_sublocs = get_sublocations(LocationID)
    $ has_sublocs = bool(current_sublocs)

    if has_sublocs and not (is_in_school(LocationID) and not is_in_school_hours()):
        if ShowSublocationIcons:
            use citydom_hud_sublocation_row(current_sublocs)

        if not ShowSublocationIcons:
            use citydom_hud_show_sublocations_button(current_sublocs)

    #  map icon
    use hud_top_icon_button("map", Function(show_map_screen), HUD_TOP_ICON_POSITIONS["map"][0], HUD_TOP_ICON_POSITIONS["map"][1])

    #  phone icon
    use hud_top_icon_button("phone", Function(citydom_phone_toggle), HUD_TOP_ICON_POSITIONS["phone"][0], HUD_TOP_ICON_POSITIONS["phone"][1], active=(ShowPhone or ShowInventory or showWallpaperScreen or Messanger or ShowConversationScreen or ShowCalendarScreen))

    if ShowPhone:
        use phone_screen

    if ShowInventory:
        use inventory_screen

    if showWallpaperScreen:
        use gallery_screen
    
    if Messanger:
        use Messanger_screen
 
    if ShowConversationScreen:
        use Conversation_screen

    if ShowCalendarScreen:
        use TimeTableScreen

    if showWallpaperPreview:
        use WallPaperPreview_screen

    if ShowCallForSidebar:
        use sidebar_screen

    use citydom_hud_time_widget

    # go back 1 room button
    if StatScreenShown == False:
        if Location_img in room_mappings:
            imagebutton:
                idle "gui/citydom_ui_v2/hud_arrow_left_idle.png"
                hover "gui/citydom_ui_v2/hud_arrow_left_hover.png"
                xpos HUD_BACK_BUTTON_X
                ypos HUD_BACK_BUTTON_Y
                at citydom_hud_arrow_motion
                action [Function(set_hud_panels), Return(room_mappings[Location_img])]

    use hud_top_icon_button("skip", Function(advance_time_or_sleep), HUD_TOP_ICON_POSITIONS["skip"][0], HUD_TOP_ICON_POSITIONS["skip"][1])
    
    use hud_top_icon_button("sleep", If(can_use_hud_hotspots(), Function(sleep_function)), HUD_TOP_ICON_POSITIONS["sleep"][0], HUD_TOP_ICON_POSITIONS["sleep"][1])

    if LocationID == 0:
        use hud_top_icon_button("call", Function(citydom_call_panel_toggle), HUD_TOP_ICON_POSITIONS["call"][0], HUD_TOP_ICON_POSITIONS["call"][1], active=ShowCallForSidebar)
    else:
        use hud_top_icon_button("call", NullAction(), HUD_TOP_ICON_POSITIONS["call"][0], HUD_TOP_ICON_POSITIONS["call"][1], disabled=True)
