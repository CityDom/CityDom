screen IsabellaRoomWeekendScreen():
    if calendar.Hours == 0:
        add "HouseScreens/Isabella_Weekend_6AM.webp"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "HouseScreens/Isabella_6AM_idle.png"
                hover "HouseScreens/Isabella_6AM_hover.png"
                xpos 714
                ypos 403
                action [Hide("IsabellaRoomWeekendScreen"), Jump("Isabella_weekend_6AM")]
                focus_mask True
    elif calendar.Hours == 1:
        add "HouseScreens/Isabella_Weekend_7AM.webp"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "HouseScreens/Isabella_7AM_idle.png"
                hover "HouseScreens/Isabella_7AM_hover.png"
                xpos 795
                ypos 367
                action [Hide("IsabellaRoomWeekendScreen"), Jump("Isabella_weekend_7AM")]
                focus_mask True
    elif calendar.Hours < 12 and calendar.Hours >= 0:
        add "HomeSubplace/Isabella room.png"
    elif calendar.Hours < 16 and calendar.Hours >= 12:
        add "HomeSubplace/Isabella room evening.png"
    elif calendar.Hours > 15 and calendar.Hours <= 20:
        add "HomeSubplace/Isabella room night.png"