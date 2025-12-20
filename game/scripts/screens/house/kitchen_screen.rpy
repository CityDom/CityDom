screen KitchenScreen():
    if calendar.Day not in [0, 6]:
        if calendar.Hours == 2:
            add "ScenesScreens/JenniferSceneScreens/Jennifer24MorningScreen/JenniferMorning24Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/JenniferSceneScreens/Jennifer24MorningScreen/JenniferMorning24Button1_idle.png"
                    hover "ScenesScreens/JenniferSceneScreens/Jennifer24MorningScreen/JenniferMorning24Button1_hover.png"
                    xpos 952
                    ypos 233
                    action [Hide("KitchenScreen"), Jump("JenniferMorning24")]
        elif calendar.Hours == 15:
            add "ScenesScreens/JenniferSceneScreens/Jennifer44EveningScreen/JenniferEvening44Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/JenniferSceneScreens/Jennifer44EveningScreen/JenniferEvening44Button1_idle.png"
                    hover "ScenesScreens/JenniferSceneScreens/Jennifer44EveningScreen/JenniferEvening44Button1_hover.png"
                    xpos 923
                    ypos 274
                    action [Hide("KitchenScreen"), Jump("JenniferEvening44")]
        elif calendar.Hours < 12 and calendar.Hours >= 0:
            add "HomeSubplace/Kitchen.png"
        elif calendar.Hours < 16 and calendar.Hours >= 12:
            add "HomeSubplace/Kitchen evening.png"
        elif calendar.Hours > 15 and calendar.Hours <= 20:
            add "HomeSubplace/Kitchen night.png"
    if calendar.Day == 0 or calendar.Day == 6:
        if calendar.Hours == 2:
            add "HouseScreens/Kitchen_Weekend_8AM.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "HouseScreens/Kitchen_Weekend_8AM_Button_idle.png"
                    hover "HouseScreens/Kitchen_Weekend_8AM_Button_hover.png"
                    xpos 869
                    ypos 306
                    action [Hide("KitchenScreen"), Jump("Jennifer_weekend_8AM")]
                    focus_mask True
        elif calendar.Hours < 12 and calendar.Hours >= 0:
            add "HomeSubplace/Kitchen.png"
        elif calendar.Hours < 16 and calendar.Hours >= 12:
            add "HomeSubplace/Kitchen evening.png"
        elif calendar.Hours > 15 and calendar.Hours <= 20:
            add "HomeSubplace/Kitchen night.png"