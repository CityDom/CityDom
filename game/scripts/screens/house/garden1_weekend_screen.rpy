screen Garden1WeekendScreen():
    if calendar.Hours == 2:
        add "HouseScreens/Claire_Weekend_8AM.webp"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "HouseScreens/Claire_8AM_idle.png"
                hover "HouseScreens/Claire_8AM_hover.png"
                xpos 1199
                ypos 380
                action [Hide("Garden1WeekendScreen"), Jump("Claire_weekend_8AM")]
                focus_mask True
    elif calendar.Hours == 3:
        add "HouseScreens/Breakfast_9AM.webp"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "HouseScreens/Breakfast_9AM_idle.png"
                hover "HouseScreens/Breakfast_9AM_hover.png"
                xpos 1225
                ypos 385
                action [Hide("Garden1WeekendScreen"), Jump("Breakfast_weekend_9AM")]
                focus_mask True
    elif calendar.Hours == 5:
        add "HouseScreens/Isabella_weekend_11AM.webp"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "HouseScreens/Isabella_11AM_idle.png"
                hover "HouseScreens/Isabella_11AM_hover.png"
                xpos 752
                ypos 405
                action [Hide("Garden1WeekendScreen"), Jump("Isabella_weekend_11AM")]
                focus_mask True
    elif calendar.Hours == 6:
        add "HouseScreens/Isabella_weekend_12PM.webp"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "HouseScreens/Isabella_12PM_idle.png"
                hover "HouseScreens/Isabella_12PM_hover.png"
                xpos 147
                ypos 535
                action [Hide("Garden1WeekendScreen"), Jump("Isabella_weekend_12PM")]
                focus_mask True
    elif calendar.Hours == 7:
        add "HouseScreens/Isabella_weekend_1PM.webp"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "HouseScreens/Isabella_1PM_idle.png"
                hover "HouseScreens/Isabella_1PM_hover.png"
                xpos 409
                ypos 484
                action [Hide("Garden1WeekendScreen"), Jump("Isabella_weekend_1PM")]
                focus_mask True
    elif calendar.Hours < 12 and calendar.Hours >= 0:
        add "HomeSubplace/garden1.png"
    elif calendar.Hours < 16 and calendar.Hours >= 12:
        add "HomeSubplace/garden1 evening.png"
    elif calendar.Hours > 15 and calendar.Hours <= 20:
        add "HomeSubplace/garden1 night.png"