screen JenniferRoomWeekendScreen():
    add "HouseScreens/Jennifer_Weekend_6AM.webp"
    if calendar.Hours == 0:
        add "HouseScreens/Jennifer_Weekend_6AM.webp"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "HouseScreens/Jennifer_6AM_idle.png"
                hover "HouseScreens/Jennifer_6AM_hover.png"
                xpos 1119
                ypos 396
                action [Hide("JenniferRoomWeekendScreen"), Jump("Jennifer_weekend_6AM")]
                focus_mask True
    else:
        add "HouseScreens/Jennifer_Weekend_6AM.webp"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "HouseScreens/Jennifer_6AM_idle.png"
                hover "HouseScreens/Jennifer_6AM_hover.png"
                xpos 1119
                ypos 396
                action [Hide("JenniferRoomWeekendScreen"), Jump("Jennifer_weekend_6AM")]
                focus_mask True