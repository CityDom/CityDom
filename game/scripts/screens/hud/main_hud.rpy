init python:
    HUD_PANEL_FLAGS = (
        "ShowPhone",
        "ShowInventory",
        "showWallpaperScreen",
        "ShowConversationScreen",
        "Messanger",
        "showWallpaperPreview",
        "ShowCamera",
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
            or store.showWallpaperScreen
            or store.showWallpaperPreview
            or store.ShowCamera
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
        renpy.store.Location_img = ""

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
                hover button["hover"]
                xpos button["xpos"]
                ypos button["ypos"]
                action button["action"]
                focus_mask True
    $ current_sublocs = get_sublocations(LocationID)
    $ has_sublocs = bool(current_sublocs)

    if ShowSublocationIcons and has_sublocs and not (is_in_school(LocationID) and not is_in_school_hours()):
        $ min_x, min_y = get_sublocation_layout(LocationID)
        for subloc in current_sublocs:
            if subloc.active:
                # Scale distances to shrink the gaps uniformly (X and Y both preserved).
                $ nx = int(min_x + (subloc.x - min_x) * SUBLOC_POS_SCALE_X) + SUBLOC_RIGHT_SHIFT
                $ ny = int(min_y + (subloc.y - min_y) * SUBLOC_POS_SCALE_Y) + SUBLOC_BOTTOM_SHIFT
                if LocationID == 1:
                    $ ny += SUBLOC_SCHOOL_Y_SHIFT

                # Resolve concrete filenames for size/idle/hover.
                $ img_idle, img_hover = subloc.resolve_icons()

                # Get image size (fallback to a sane default if not loadable)
                $ iw, ih = subloc.get_icon_size()

                # Convert top-left layout (nx, ny) to center coords so we can anchor/zoom from middle
                $ cx = nx + (iw // 2)
                $ cy = ny + SUBLOC_ICON_Y_OFFSET + (ih // 2)

                # Shadow (center-anchored so it matches the icon)
                add "SubIconsShadow.png":
                    xcenter cx + SUBLOC_SHADOW_OFFSET
                    ycenter cy + SUBLOC_SHADOW_OFFSET
                    anchor (0.5, 0.5)

                # Icon (zooms from its center)
                imagebutton:
                    at subloc_hover_zoom
                    idle img_idle
                    hover img_hover
                    xcenter cx
                    ycenter cy
                    focus_mask True
                    action hud_navigation_actions(subloc.name)

    #  map icon
    imagebutton:
        idle "gui/new_ui/icons/map.png"
        hover "gui/new_ui/icons/map_hover.png"
        xpos 1740
        ypos 12
        action Function(show_map_screen)

    #  open/close sublocations
    if not (is_in_school(LocationID) and not is_in_school_hours()):
        imagebutton:
            auto "Arrow_%s.png" xpos -15 ypos 955
            action ToggleVariable("ShowSublocationIcons", True, False)

    #  phone icon
    imagebutton:
        idle "gui/new_ui/icons/phone.png"
        hover "gui/new_ui/icons/phone_hover.png"
        xpos 1660
        ypos 12
        action Function(toggle_hud_panel, "ShowPhone")

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

    if showWallpaperPreview:
        use WallPaperPreview_screen

    if ShowCallForSidebar:
        use sidebar_screen

    # if ShowCamera:
    #     use Camera_screen

    # daytime icons 
    for icon, (start, end), label in time_icons:
        if start <= calendar.Hours < end:
            # Creating a frame to hold the icon and text together
            $ scaled_icon = scale_image(icon, scale_factor)
            frame:
                xpos 20
                ypos 10
                xsize scaled_icon.width
                ysize scaled_icon.height
                background None  # Ensures the frame itself has no visible border

                # Add the scaled icon as the background of the frame
                add scaled_icon

                # Calculate the real hour format
                $ real_hour = to_real_hour(calendar.Hours)
                $ hour_12_format = real_hour % 12
                $ hour_12_format = 12 if hour_12_format == 0 else hour_12_format
                $ am_pm = "AM" if real_hour < 12 or real_hour == 24 else "PM"

                if not is_in_school(LocationID):
                    # Position the time text within the frame
                    text f"{hour_12_format}:00 {am_pm}" xalign 0.7 yalign 0.25 style "digital_text" color "#ffffff" outlines [(1, "#000000", 0, 0)] size 30
                    
                    # Display the current weekday within the frame
                    $ current_weekday = calendar.WeekDays[int(calendar.Day)]
                    text "[current_weekday]" xalign 0.5 yalign 0.1 color "#ffffff" style "digital_text" outlines [(1, "#000000", 0, 0)] size 30

                if is_in_school(LocationID) and 12 <= school_clock.hour < 18:
                    # Position the school clock time within the frame
                    text f"{school_clock.Output} {am_pm}" xalign 0.7 yalign 0.25 style "digital_text" color "#ffffff" outlines [(1, "#000000", 0, 0)] size 30
                    
                    # Display the current weekday within the frame
                    $ current_weekday = calendar.WeekDays[int(calendar.Day)]
                    text "[current_weekday]" xalign 0.5 yalign 0.1 color "#ffffff" style "digital_text" outlines [(1, "#000000", 0, 0)] size 30



    # go back 1 room button
    if StatScreenShown == False:
        if Location_img in room_mappings:
            $ button_image = "GoBackRoomButton_%s.png"
            imagebutton:
                auto button_image
                idle "GoBackRoomButton_idle.png"
                xpos 1850
                ypos 1000
                action [Function(set_hud_panels), Return(room_mappings[Location_img])]

    imagebutton:
        idle "gui/new_ui/icons/skip.png"
        hover "gui/new_ui/icons/skip_hover.png"
        xpos 1430
        ypos 12
        action Function(advance_time_or_sleep)
    
    imagebutton:
        idle "gui/new_ui/icons/sleep.png"
        hover "gui/new_ui/icons/sleep_hover.png"
        xpos 1510
        ypos 12
        action If(can_use_hud_hotspots(), Function(sleep_function))

    if LocationID == 0:
        imagebutton:
            idle "gui/new_ui/icons/call.png"
            hover "gui/new_ui/icons/call_hover.png"
            xpos 1590
            ypos 22
            action Function(toggle_hud_panel, "ShowCallForSidebar")
    else:
        imagebutton:
            idle "gui/new_ui/icons/call.png"
            hover "gui/new_ui/icons/call_hover.png"
            xpos 1590
            ypos 22
            action NullAction()
        add "forbidden.png" xpos 1590 ypos 22
