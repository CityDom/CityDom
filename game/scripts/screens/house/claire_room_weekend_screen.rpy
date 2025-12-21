screen ClaireRoomWeekendScreen():

    # Auto-redirect when it's '
    on "show" action If(
        (calendar.Day == 0 or calendar.Day == 6) and calendar.Hours == 4,
        [Hide("ClaireRoomWeekendScreen"), Jump("ClaireNoon14")]
    )

    if (calendar.Day == 0 or calendar.Day == 6) and calendar.Hours == 0:
        add "HouseScreens/Claire_Weekend_6AM.webp"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "HouseScreens/Claire_6AM_idle.png"
                hover "HouseScreens/Claire_6AM_hover.png"
                xpos 730
                ypos 348
                action [Hide("ClaireRoomWeekendScreen"), Jump("Claire_weekend_6AM")]
                focus_mask True
    elif calendar.Hours < 12 and calendar.Hours >= 0:
        add "HomeSubplace/Claire room.png"
    elif calendar.Hours < 16 and calendar.Hours >= 12:
        add "HomeSubplace/Claire room evening.png"
    elif calendar.Hours > 15 and calendar.Hours <= 20:
        add "HomeSubplace/Claire room night.png"
