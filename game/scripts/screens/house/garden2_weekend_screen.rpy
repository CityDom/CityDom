screen Garden2WeekendScreen():
    if calendar.Hours == HOUR_8AM:
        add "HouseScreens/Claire_Weekend_8AM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Claire_8AM_idle.png"
                hover "HouseScreens/Claire_8AM_hover.png"
                xpos 730
                ypos 348
                action [Hide("Garden2WeekendScreen"), Jump("Claire_weekend_8AM")]
                focus_mask True
    elif is_day_hour(calendar.Hours):
        add "HomeSubplace/garden2.png"
    elif is_evening_hour(calendar.Hours):
        add "HomeSubplace/garden2 evening.png"
    elif is_night_hour(calendar.Hours):
        add "HomeSubplace/garden2 night.png"
