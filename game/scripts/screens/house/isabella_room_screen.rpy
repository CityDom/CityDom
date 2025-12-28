screen IsabellaRoomScreen():
    if calendar.Day not in [0, 6]:
        if calendar.Hours == 0:
            add "ScenesScreens/IsabellaSceneScreens/Isabella14MorningScreen/IsabellaMorning14Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/IsabellaSceneScreens/Isabella14MorningScreen/IsabellaMorning14Button1_idle.png"
                    hover "ScenesScreens/IsabellaSceneScreens/Isabella14MorningScreen/IsabellaMorning14Button1_hover.png"
                    xpos 720
                    ypos 331
                    action [Function(hideEventScreens), Jump("IsabellaMorningEvent14")]
        elif calendar.Hours == 1:
            add "ScenesScreens/IsabellaSceneScreens/Isabella34MorningScreen/IsabellaMorning34Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/IsabellaSceneScreens/Isabella34MorningScreen/IsabellaMorning34Button1_idle.png"
                    hover "ScenesScreens/IsabellaSceneScreens/Isabella34MorningScreen/IsabellaMorning34Button1_hover.png"
                    xpos 662
                    ypos 340
                    action [Function(hideEventScreens), Jump("IsabellaMorningEvent34")]
        elif calendar.Hours == 14:
            add "ScenesScreens/IsabellaSceneScreens/Isabella34EveningScreen/IsabellaEvening34Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/IsabellaSceneScreens/Isabella34EveningScreen/IsabellaEvening34Button1_idle.png"
                    hover "ScenesScreens/IsabellaSceneScreens/Isabella34EveningScreen/IsabellaEvening34Button1_hover.png"
                    xpos 663
                    ypos 370
                    action [Function(hideEventScreens), Jump("IsabellaEveningEvent34")]
        elif calendar.Hours == 18:
            add "ScenesScreens/IsabellaSceneScreens/Isabella44AfternoonScreen/IsabellaAfternoon44Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/IsabellaSceneScreens/Isabella44AfternoonScreen/IsabellaAfternoon44Button1_idle.png"
                    hover "ScenesScreens/IsabellaSceneScreens/Isabella44AfternoonScreen/IsabellaAfternoon44Button1_hover.png"
                    xpos 1263
                    ypos 339
                    action [Function(hideEventScreens), Jump("IsabellaAfterNoonEvent44")]
        elif calendar.Hours == 19:
            add "ScenesScreens/IsabellaSceneScreens/Isabella44NightScreen/IsabellaNight44Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/IsabellaSceneScreens/Isabella44NightScreen/IsabellaNight44Button1_idle.png"
                    hover "ScenesScreens/IsabellaSceneScreens/Isabella44NightScreen/IsabellaNight44Button1_hover.png"
                    xpos 753
                    ypos 398
                    action [Function(hideEventScreens), Jump("IsabellaNightEvent44")]
        elif calendar.Hours == 20:
            add "ScenesScreens/IsabellaSceneScreens/Isabella14MidnightScreen/IsabellaMidnight14Screen1.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "ScenesScreens/IsabellaSceneScreens/Isabella14MidnightScreen/IsabellaMidnight14Button1_idle.png"
                    hover "ScenesScreens/IsabellaSceneScreens/Isabella14MidnightScreen/IsabellaMidnight14Button1_hover.png"
                    xpos 823
                    ypos 401
                    action [Function(hideEventScreens), Jump("IsabellaMidnightEvent14")]
        elif calendar.Hours < 12 and calendar.Hours >= 0:
            add "HomeSubplace/Isabella room.png"
        elif calendar.Hours < 16 and calendar.Hours >= 12:
            add "HomeSubplace/Isabella room evening.png"
        elif calendar.Hours > 15 and calendar.Hours <= 20:
            add "HomeSubplace/Isabella room night.png"
    else:
        if calendar.Hours == 0:
            add "HouseScreens/Isabella_Weekend_6AM.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "HouseScreens/Isabella_6AM_idle.png"
                    hover "HouseScreens/Isabella_6AM_hover.png"
                    xpos 714
                    ypos 403
                    action [Function(hideEventScreens), Jump("Isabella_weekend_6AM")]
                    focus_mask True
        elif calendar.Hours == 1:
            add "HouseScreens/Isabella_Weekend_7AM.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "HouseScreens/Isabella_7AM_idle.png"
                    hover "HouseScreens/Isabella_7AM_hover.png"
                    xpos 795
                    ypos 367
                    action [Function(hideEventScreens), Jump("Isabella_weekend_7AM")]
                    focus_mask True
        elif calendar.Hours == 8:
            add "HouseScreens/Isabella_Weekend_2PM.webp"
            if not MapScreenShown and not StatsScreenShown:
                imagebutton:
                    idle "HouseScreens/Isabella_2PM_idle.png"
                    hover "HouseScreens/Isabella_2PM_hover.png"
                    xpos 778
                    ypos 353
                    action [Function(hideEventScreens), Jump("Isabella_weekend_2PM")]
                    focus_mask True
        elif calendar.Hours < 12 and calendar.Hours >= 0:
            add "HomeSubplace/Isabella room.png"
        elif calendar.Hours < 16 and calendar.Hours >= 12:
            add "HomeSubplace/Isabella room evening.png"
        elif calendar.Hours > 15 and calendar.Hours <= 20:
            add "HomeSubplace/Isabella room night.png"
