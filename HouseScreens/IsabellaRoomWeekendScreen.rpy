screen IsabellaRoomWeekendScreen():
    add "HouseScreens/Isabella_Weekend_6AM.webp"
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
    else:
        add "HouseScreens/Isabella_Weekend_6AM.webp"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "HouseScreens/Isabella_6AM_idle.png"
                hover "HouseScreens/Isabella_6AM_hover.png"
                xpos 714
                ypos 403
                action [Hide("IsabellaRoomWeekendScreen"), Jump("Isabella_weekend_6AM")]
                focus_mask True