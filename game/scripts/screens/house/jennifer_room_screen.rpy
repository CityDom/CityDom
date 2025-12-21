screen JenniferRoomScreen():
    if calendar.Day not in [0, 6]:
        if calendar.Hours == 0:
            add "ScenesScreens/JenniferSceneScreens/Jennifer14MorningScreen/JenniferMorning14Screen1.png"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/JenniferSceneScreens/Jennifer14MorningScreen/JenniferMorning14Button1_idle.png"
                    hover "ScenesScreens/JenniferSceneScreens/Jennifer14MorningScreen/JenniferMorning14Button1_hover.png"
                    xpos 927
                    ypos 361
                    action [Function(hideEventScreens), Jump("JenniferMorningEvent14")]
        elif calendar.Hours == 15:
            add "ScenesScreens/IsabellaSceneScreens/Isabella44EveningScreen/IsabellaEvening44Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/IsabellaSceneScreens/Isabella44EveningScreen/IsabellaEvening44Button1_idle.png"
                    hover "ScenesScreens/IsabellaSceneScreens/Isabella44EveningScreen/IsabellaEvening44Button1_hover.png"
                    xpos 1699
                    ypos 515
                    action [Function(hideEventScreens), Jump("IsabellaEveningEvent44")]
        elif calendar.Hours == 19:
            add "ScenesScreens/JenniferSceneScreens/Jennifer34NightScreen/JenniferNight34Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/JenniferSceneScreens/Jennifer34NightScreen/JenniferNight34Button1_idle.png"
                    hover "ScenesScreens/JenniferSceneScreens/Jennifer34NightScreen/JenniferNight34Button1_hover.png"
                    xpos 995
                    ypos 285
                    action [Function(hideEventScreens), Jump("JenniferNightEvent34")]
        elif calendar.Hours == 20:
            add "ScenesScreens/JenniferSceneScreens/Jennifer44NightScreen/JenniferNight44Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/JenniferSceneScreens/Jennifer44NightScreen/JenniferNight44Button1_idle.png"
                    hover "ScenesScreens/JenniferSceneScreens/Jennifer44NightScreen/JenniferNight44Button1_hover.png"
                    xpos 1080
                    ypos 457
                    action [Function(hideEventScreens), Jump("JenniferNightEvent44")]
        elif calendar.Hours < 12 and calendar.Hours >= 0:
            add "HomeSubplace/Jennifer room.png"
        elif calendar.Hours < 16 and calendar.Hours >= 12:
            add "HomeSubplace/Jennifer room evening.png"
        elif calendar.Hours > 15 and calendar.Hours <= 20:
            add "HomeSubplace/Jennifer room night.png"
    else:
        if calendar.Hours == 0:
            add "HouseScreens/Jennifer_Weekend_6AM.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "HouseScreens/Jennifer_6AM_idle.png"
                    hover "HouseScreens/Jennifer_6AM_hover.png"
                    xpos 1119
                    ypos 396
                    action [Function(hideEventScreens), Jump("Jennifer_weekend_6AM")]
                    focus_mask True
        elif calendar.Hours < 12 and calendar.Hours >= 0:
            add "HouseScreens/Jennifer_Room_Weekend_Day.webp"
        elif calendar.Hours < 16 and calendar.Hours >= 12:
            add "HomeSubplace/Jennifer room evening.png"
        elif calendar.Hours > 15 and calendar.Hours <= 20:
            add "HomeSubplace/Jennifer room night.png"
