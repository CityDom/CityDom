screen EntranceScreen():
    if calendar.Day not in [0, 6]:
        if calendar.Hours == HOUR_11AM:
            add "ScenesScreens/LeaveHomeSceneScreens/LeaveHomeScreen1/LeaveHomeScreen1.webp"
            imagebutton:
                idle "ScenesScreens/LeaveHomeSceneScreens/LeaveHomeScreen1/LeaveHomeScreenButton1_idle.png"
                hover "ScenesScreens/LeaveHomeSceneScreens/LeaveHomeScreen1/LeaveHomeScreenButton1_hover.png"
                xpos 1176
                ypos 252
                action [Hide("EntranceScreen"), Jump("LeaveHomeLVL1")]
                focus_mask True
        elif calendar.Hours == HOUR_4PM:
            add "ScenesScreens/IsabellaSceneScreens/Isabella24NoonScreen/IsabellaNoon24Screen1.webp"
            imagebutton:
                idle "ScenesScreens/IsabellaSceneScreens/Isabella24NoonScreen/IsabellaNoon24Button1_idle.png"
                hover "ScenesScreens/IsabellaSceneScreens/Isabella24NoonScreen/IsabellaNoon24Button1_hover.png"
                xpos 1332
                ypos 414
                action [Hide("EntranceScreen"), Jump("IsabellaNoonEvent24")]
                focus_mask True
        elif calendar.Hours == HOUR_6PM:
            add "ScenesScreens/ClaireSceneScreens/Claire14EveningScreen/ClaireEvening14Screen1.webp"
            imagebutton:
                idle "ScenesScreens/ClaireSceneScreens/Claire14EveningScreen/ClaireEvening14Button1_idle.png"
                hover "ScenesScreens/ClaireSceneScreens/Claire14EveningScreen/ClaireEvening14Button1_hover.png"
                xpos 1363   
                ypos 367
                action [Hide("EntranceScreen"), Jump("ClaireEveningEvent14")]
                focus_mask True
        elif calendar.Hours == HOUR_7PM:
            add "ScenesScreens/JenniferSceneScreens/Jennifer24EveningScreen/JenniferEvening24Screen1.webp"
            if should_show_room_buttons():
                imagebutton:
                    idle "ScenesScreens/JenniferSceneScreens/Jennifer24EveningScreen/JenniferEvening24Button1_idle.png"
                    hover "ScenesScreens/JenniferSceneScreens/Jennifer24EveningScreen/JenniferEvening24Button1_hover.png"
                    xpos 1355
                    ypos 350
                    action [Hide("EntranceScreen"), Jump("JenniferEveningEvent24")]
                    focus_mask True
        elif is_day_hour(calendar.Hours):
            add "Places/Entrance.png"
        elif is_evening_hour(calendar.Hours):
            add "Places/Entrance evening.png"
        elif is_night_hour(calendar.Hours):
            add "Places/Entrance night.png"
    if calendar.Day == 0 or calendar.Day == 6:
        if calendar.Hours == HOUR_10AM:
            add "HouseScreens/Isabella_Weekend_10AM.webp"
            if should_show_room_buttons():
                imagebutton:
                    idle "HouseScreens/Isabella_10AM_idle.png"
                    hover "HouseScreens/Isabella_10AM_hover.png"
                    xpos 1328
                    ypos 402
                    action [Hide("EntranceScreen"), Jump("Isabella_weekend_10AM")]
                    focus_mask True
        elif calendar.Hours == HOUR_1PM:
            add "HouseScreens/Jennifer_weekend_1PM.webp"
            if should_show_room_buttons():
                imagebutton:
                    idle "HouseScreens/Jennifer_1PM_idle.png"
                    hover "HouseScreens/Jennifer_1PM_hover.png"
                    xpos 1314
                    ypos 354
                    action [Hide("EntranceScreen"), Jump("Jennifer_weekend_1PM")]
                    focus_mask True
        elif is_day_hour(calendar.Hours):
            add "Places/Entrance.png"
        elif is_evening_hour(calendar.Hours):
            add "Places/Entrance evening.png"
        elif is_night_hour(calendar.Hours):
            add "Places/Entrance night.png"
