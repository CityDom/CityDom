screen KitchenScreen():
    if calendar.Day not in [0, 6]:
        if calendar.Hours == HOUR_8AM:
            add "ScenesScreens/JenniferSceneScreens/Jennifer24MorningScreen/JenniferMorning24Screen1.webp"
            if should_show_room_buttons():
                imagebutton:
                    idle "ScenesScreens/JenniferSceneScreens/Jennifer24MorningScreen/JenniferMorning24Button1_idle.png"
                    hover "ScenesScreens/JenniferSceneScreens/Jennifer24MorningScreen/JenniferMorning24Button1_hover.png"
                    xpos 952
                    ypos 233
                    action Function(start_event_from_screen, "ScenesScreens/JenniferSceneScreens/Jennifer24MorningScreen/JenniferMorning24Screen1.webp", "JenniferMorning24")
        elif calendar.Hours == HOUR_9PM:
            add "ScenesScreens/JenniferSceneScreens/Jennifer44EveningScreen/JenniferEvening44Screen1.webp"
            if should_show_room_buttons():
                imagebutton:
                    idle "ScenesScreens/JenniferSceneScreens/Jennifer44EveningScreen/JenniferEvening44Button1_idle.png"
                    hover "ScenesScreens/JenniferSceneScreens/Jennifer44EveningScreen/JenniferEvening44Button1_hover.png"
                    xpos 923
                    ypos 274
                    action Function(start_event_from_screen, "ScenesScreens/JenniferSceneScreens/Jennifer44EveningScreen/JenniferEvening44Screen1.webp", "JenniferEvening44")
        elif is_day_hour(calendar.Hours):
            add "HomeSubplace/Kitchen.png"
        elif is_evening_hour(calendar.Hours):
            add "HomeSubplace/Kitchen evening.png"
        elif is_night_hour(calendar.Hours):
            add "HomeSubplace/Kitchen night.png"
    if calendar.Day == 0 or calendar.Day == 6:
        if calendar.Hours == HOUR_8AM:
            add "HouseScreens/Kitchen_Weekend_8AM.webp"
            if should_show_room_buttons():
                imagebutton:
                    idle "HouseScreens/Kitchen_Weekend_8AM_Button_idle.png"
                    hover "HouseScreens/Kitchen_Weekend_8AM_Button_hover.png"
                    xpos 869
                    ypos 306
                    action Function(start_event_from_screen, "HouseScreens/Kitchen_Weekend_8AM.webp", "Jennifer_weekend_8AM")
                    focus_mask True
        elif is_day_hour(calendar.Hours):
            add "HomeSubplace/Kitchen.png"
        elif is_evening_hour(calendar.Hours):
            add "HomeSubplace/Kitchen evening.png"
        elif is_night_hour(calendar.Hours):
            add "HomeSubplace/Kitchen night.png"
