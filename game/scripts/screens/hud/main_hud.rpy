init python:
    def hideEventScreens():
        for screen_name in ALL_EVENT_SCREENS:
            renpy.hide_screen(screen_name)

    def callGameLoop():
        renpy.call("GameLoop")

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
        ShowPhone = False
        MapScreenShown = True
        ShowInventory = False
        showWallpaperScreen = False
        Messanger = False
        showWallpaperPreview = False
        ShowCallForSidebar = False

screen MainHud():

    

    # # Lightweight periodic refresh; does NOT advance game time
    # default _hud_tick = 0
    # timer 0.75 action SetScreenVariable("_hud_tick", _hud_tick + 1) repeat True
#  invisible door buttons
    if ShowPhone == False:
        if Messanger == False:
            if ShowConversationScreen == False:
                if showWallpaperScreen == False:
                    if showWallpaperPreview == False:
                        if ShowCamera == False:
                            if Location_img in invisible_door_button_mappings:
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
                    action [Function(hideEventScreens),
                            Return(subloc.name),
                            SetVariable("ShowPhone", False),
                            SetVariable("ShowInventory", False), 
                            SetVariable("showWallpaperScreen", False), 
                            SetVariable("Messanger", False),
                            SetVariable("showWallpaperPreview", False),
                            SetVariable("ShowCallForSidebar", False)]

    #  map icon
    imagebutton:
        auto "SubLocationIcons/MapIcon_%s.png" xpos 1830 ypos 10
        action [Function(show_map_screen),
                SetVariable("ShowCallForSidebar", False)]

    #  open/close sublocations
    if not (is_in_school(LocationID) and not is_in_school_hours()):
        imagebutton:
            auto "Arrow_%s.png" xpos -15 ypos 955
            action ToggleVariable("ShowSublocationIcons", True, False)

    #  phone icon
    imagebutton:
        auto "PhoneIcon_%s.png" xpos 1750 ypos 10
        action [ToggleVariable("ShowPhone", True, False), 
                SetVariable("ShowInventory", False), 
                SetVariable("showWallpaperScreen", False), 
                SetVariable("ShowConversationScreen", False), 
                SetVariable("Messanger", False),
                SetVariable("showWallpaperPreview", False),
                SetVariable("ShowCamera", False),
                SetVariable("ShowCallForSidebar", False)]

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
                $ real_hour = (calendar.Hours + 6) % 24
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
                action [Return(room_mappings[Location_img]), 
                        SetVariable("ShowPhone", False), 
                        SetVariable("ShowInventory", False), 
                        SetVariable("showWallpaperScreen", False), 
                        SetVariable("Messanger", False),
                        SetVariable("showWallpaperPreview", False),
                        SetVariable("ShowCamera", False),
                        SetVariable("ShowCallForSidebar", False)]

    imagebutton:
        auto "skip_time_%s.png" xpos 1510 ypos 10
        action Function(advance_time_or_sleep)
    
    imagebutton:
        auto "sleep_%s.png" xpos 1590 ypos 10
        action If(ShowPhone == False and Messanger == False and ShowConversationScreen == False and showWallpaperScreen == False and showWallpaperPreview == False and ShowCamera == False, Function(sleep_function))

    if LocationID == 0:
        imagebutton:
            auto "Announce_%s.png" xpos 1670 ypos 10
            action [ToggleVariable("ShowCallForSidebar", True, False),
                    SetVariable("ShowInventory", False), 
                    SetVariable("showWallpaperScreen", False), 
                    SetVariable("ShowConversationScreen", False), 
                    SetVariable("Messanger", False),
                    SetVariable("showWallpaperPreview", False),
                    SetVariable("ShowCamera", False),
                    SetVariable("ShowPhone", False)]
    else:
        imagebutton:
            auto "Announce_%s.png" xpos 1670 ypos 10
            action NullAction()
        add "forbidden.png" xpos 1670 ypos 10
