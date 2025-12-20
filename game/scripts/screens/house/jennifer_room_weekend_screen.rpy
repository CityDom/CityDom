screen JenniferRoomWeekendScreen():

    # Auto-redirect when it's 4
    
    on "show" action If(
        calendar.Hours == 4,
        [Hide("JenniferRoomWeekendScreen"), Jump("Jennifer_weekend_10AM")]
    )
    on "show" action If(
        calendar.Hours == 8,
        [Hide("JenniferRoomWeekendScreen"), Jump("Jennifer_weekend_2PM")]
    )

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

    elif calendar.Hours < 12 and calendar.Hours >= 0:
        add "HouseScreens/Jennifer_Room_Weekend_Day.webp"

    elif calendar.Hours < 16 and calendar.Hours >= 12:
        add "HomeSubplace/Jennifer room evening.png"

    elif calendar.Hours > 15 and calendar.Hours <= 20:
        add "HomeSubplace/Jennifer room night.png"
