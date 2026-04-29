screen phone_screen():
    $ init_background_buttons()
    $ update_current_message()

    frame:
        xpos 1550
        ypos 100
        xysize (334, 700)
        background None

        add "gui/new_ui/phone/home.png"

        for icon, (start, end), label in time_icons:
            if start <= calendar.Hours < end:
                $ real_hour = to_real_hour(calendar.Hours)
                $ hour_12_format = real_hour % 12
                $ hour_12_format = 12 if hour_12_format == 0 else hour_12_format
                $ am_pm = "AM" if real_hour < 12 or real_hour == 24 else "PM"

                if not is_in_school(LocationID):
                    text f"{hour_12_format}:00 {am_pm}" xpos 24 ypos 15 style "digital_text" color "#ffffff" size 16 outlines [(1, "#00000080", 0, 0)]

                if is_in_school(LocationID) and 12 <= school_clock.hour < 18:
                    text f"{school_clock.Output} {am_pm}" xpos 24 ypos 15 style "digital_text" color "#ffffff" size 16 outlines [(1, "#00000080", 0, 0)]

        button:
            xpos 35
            ypos 570
            xysize (63, 63)
            background None
            hover_background "#ffffff18"
            action [SetVariable("showWallpaperScreen", True), SetVariable("ShowPhone", False)]

        button:
            xpos 136
            ypos 570
            xysize (63, 63)
            background None
            hover_background "#ffffff18"
            action [Hide("MainHud"),
                    Show("StatsScreen"),
                    Show("character_select_screen"),
                    SetVariable("CharacterSelectionIsShowing", True),
                    SetVariable("StatsScreenShown", True),
                    SetVariable("ShowPhone", False)]

        button:
            xpos 237
            ypos 570
            xysize (63, 63)
            background None
            hover_background "#ffffff18"
            action [SetVariable("ShowInventory", True), SetVariable("ShowPhone", False)]

        button:
            xpos 135
            ypos 490
            xysize (63, 63)
            background None
            hover_background "#ffffff18"
            action [SetVariable("Messanger", True), SetVariable("ShowPhone", False)]

        button:
            xpos 238
            ypos 490
            xysize (63, 63)
            background None
            hover_background "#ffffff18"
            action [Hide("MainHud"), Show("TimeTableScreen"), SetVariable("ShowPhone", False)]

        button:
            xpos 74
            ypos 658
            xysize (24, 24)
            background None
            hover_background "#ffffff18"
            action SetVariable("ShowPhone", False)

        button:
            xpos 150
            ypos 658
            xysize (25, 24)
            background None
            hover_background "#ffffff18"
            action NullAction()
