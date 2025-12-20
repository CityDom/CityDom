screen Garden2WeekendScreen():
    if calendar.Hours == 2:
        add "HouseScreens/Claire_Weekend_8AM.webp"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "HouseScreens/Claire_8AM_idle.png"
                hover "HouseScreens/Claire_8AM_hover.png"
                xpos 730
                ypos 348
                action [Hide("Garden2WeekendScreen"), Jump("Claire_weekend_8AM")]
                focus_mask True
    elif calendar.Hours < 12 and calendar.Hours >= 0:
        add "HomeSubplace/garden2.png"
    elif calendar.Hours < 16 and calendar.Hours >= 12:
        add "HomeSubplace/garden2 evening.png"
    elif calendar.Hours > 15 and calendar.Hours <= 20:
        add "HomeSubplace/garden2 night.png"
