screen phone_screen():
    $ init_background_buttons()
    $ update_current_message()
    frame:
        xpos 1550
        ypos 100
        background "PhoneBackground/[setBackgroundPhoto]"
        image "battery_status.png":
            xpos 295
            ypos 10
        image "signal.png":
            xpos 270
            ypos 10
        image "wifi.png":
            xpos 245
            ypos 10
        image "alarm_clock.png":
            xpos 215
            ypos 10
        for icon, (start, end), label in time_icons:
            if start <= calendar.Hours < end:
                # Convert game hour to real-world hour, assuming game starts at 7:00 AM
                $ real_hour = to_real_hour(calendar.Hours)
                $ hour_12_format = real_hour % 12
                $ hour_12_format = 12 if hour_12_format == 0 else hour_12_format
                $ am_pm = "AM" if real_hour < 12 or real_hour == 24 else "PM"
                
                if not is_in_school(LocationID):
                    # For simplicity, minutes are not displayed; adjust if needed
                    text f"{hour_12_format}:00 {am_pm}" xpos 5 ypos 7 style "digital_text" color "#000000" size 25
                    #text f"{label}" xpos 123 ypos 50 style "digital_text" color "#000000"

                # Add the school clock time display
                if is_in_school(LocationID) and 12 <= school_clock.hour < 18:
                    text f"{school_clock.Output} {am_pm}" xpos 5 ypos 7 style "digital_text" color "#000000" size 25
                    #text f"{label}" xpos 110 ypos 50 style "digital_text" color "#000000"

        # backpack icon
        imagebutton:
            xpos 10
            ypos 610
            auto "BackPackIcon_%s.png"
            action [SetVariable("ShowInventory", True), 
                    SetVariable("ShowPhone", False)]

        #  background icon
        imagebutton:
            xpos 90
            ypos 610
            auto "BackgroundIcon_%s.png"
            action [SetVariable("showWallpaperScreen", True), 
                    SetVariable("ShowPhone", False)]

        # photo stats icon 
        imagebutton:
            xpos 170
            ypos 610
            auto "StatsIcon_%s.png"
            action [Hide("MainHud"),
                    Show("StatsScreen"),
                    Show("character_select_screen"),
                    SetVariable("CharacterSelectionIsShowing", True), 
                    SetVariable("StatsScreenShown", True), 
                    SetVariable("ShowPhone", False)]

        # photo stats icon 
        imagebutton:
            xpos 10
            ypos 540
            auto "timeTable_%s.png"
            action [Hide("MainHud"),
                    Show("TimeTableScreen"),
                    SetVariable("ShowPhone", False)]

        # if ShowStatsIcon:
        #     imagebutton:
        #         xpos 250
        #         ypos 610
        #         auto "dikcok_%s.png"
        #         action [SetVariable("ShowBackPackIcon", False), SetVariable("ShowStatsIcon", False), SetVariable("ShowBackgroundIcon", False),
        #         Return("ChooseCharacterStats"), SetVariable("ShowInventory", False), SetVariable("showWallpaperScreen", False), SetVariable("CharacterSelectionIsShowing", True)]

        imagebutton:
            xpos 250
            ypos 610
            auto "chat_%s.png"
            action [SetVariable("Messanger", True), 
                    SetVariable("ShowPhone", False)]

        # imagebutton:
        #     xpos 250
        #     ypos 610
        #     auto "camera_%s.png"
        #     action [SetVariable("ShowCamera", True),
        #             SetVariable("ShowPhone", False)]
