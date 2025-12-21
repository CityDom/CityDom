screen ClaireRoomScreen():
    if calendar.Day not in [0, 6]:
        if calendar.Hours == 0:
            add "ScenesScreens/ClaireSceneScreens/Claire14MorningScreen/ClaireMorning14Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/ClaireSceneScreens/Claire14MorningScreen/ClaireMorning14Button1_idle.png"
                    hover "ScenesScreens/ClaireSceneScreens/Claire14MorningScreen/ClaireMorning14Button1_hover.png"
                    xpos 719
                    ypos 277
                    action [Function(hideEventScreens), Jump("ClaireMorningEvent14")]
        elif calendar.Hours == 14:
            add "ScenesScreens/ClaireSceneScreens/Claire34EveningScreen/ClaireEvening34Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/ClaireSceneScreens/Claire34EveningScreen/ClaireEvening34Button1_idle.png"
                    hover "ScenesScreens/ClaireSceneScreens/Claire34EveningScreen/ClaireEvening34Button1_hover.png"
                    xpos 1012
                    ypos 264
                    action [Function(hideEventScreens), Jump("ClaireEveningEvent34")]
        elif calendar.Hours == 15:
            add "ScenesScreens/ClaireSceneScreens/Claire44EveningScreen/ClaireEvening44Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/ClaireSceneScreens/Claire44EveningScreen/ClaireEvening44Button1_idle.png"
                    hover "ScenesScreens/ClaireSceneScreens/Claire44EveningScreen/ClaireEvening44Button1_hover.png"
                    xpos 626
                    ypos 261
                    action [Function(hideEventScreens), Jump("ClaireEveningEvent44")]
        elif calendar.Hours == 20:
            add "ScenesScreens/ClaireSceneScreens/Claire14MidnightScreen/ClaireMidnight14Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/ClaireSceneScreens/Claire14MidnightScreen/ClaireMidnight14Button1_idle.png"
                    hover "ScenesScreens/ClaireSceneScreens/Claire14MidnightScreen/ClaireMidnight14Button1_hover.png"
                    xpos 712
                    ypos 322
                    action [Function(hideEventScreens), Jump("ClaireMidnightEvent14")]
        elif calendar.Hours < 12 and calendar.Hours >= 0:
            add "HomeSubplace/Claire room.png"
        elif calendar.Hours < 16 and calendar.Hours >= 12:
            add "HomeSubplace/Claire room evening.png"
        elif calendar.Hours > 15 and calendar.Hours <= 20:
            add "HomeSubplace/Claire room night.png"
    else:
        if calendar.Hours == 0:
            add "HouseScreens/Claire_Weekend_6AM.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "HouseScreens/Claire_6AM_idle.png"
                    hover "HouseScreens/Claire_6AM_hover.png"
                    xpos 730
                    ypos 348
                    action [Function(hideEventScreens), Jump("Claire_weekend_6AM")]
                    focus_mask True
        elif calendar.Hours < 12 and calendar.Hours >= 0:
            add "HomeSubplace/Claire room.png"
        elif calendar.Hours < 16 and calendar.Hours >= 12:
            add "HomeSubplace/Claire room evening.png"
        elif calendar.Hours > 15 and calendar.Hours <= 20:
            add "HomeSubplace/Claire room night.png"
