screen ClaireRoomWeekendScreen():
    add "HouseScreens/Claire_Weekend_6AM.webp"
    if calendar.Hours == 0:
        add "HouseScreens/Claire_Weekend_6AM.webp"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "HouseScreens/Claire_6AM_idle.png"
                hover "HouseScreens/Claire_6AM_hover.png"
                xpos 730
                ypos 348
                action [Hide("ClaireRoomWeekendScreen"), Jump("Claire_weekend_6AM")]
                focus_mask True
    else:
        add "HouseScreens/Claire_Weekend_6AM.webp"
        if not MapScreenShown and not StatsScreenShown:
            imagebutton:
                idle "HouseScreens/Claire_6AM_idle.png"
                hover "HouseScreens/Claire_6AM_hover.png"
                xpos 730
                ypos 348
                action [Hide("ClaireRoomWeekendScreen"), Jump("Claire_weekend_6AM")]
                focus_mask True