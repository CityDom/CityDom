screen Garden1WeekendScreen():
    if calendar.Hours == HOUR_8AM:
        add "HouseScreens/Claire_Weekend_8AM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Claire_8AM_idle.png"
                hover "HouseScreens/Claire_8AM_hover.png"
                xpos 1199
                ypos 380
                action Function(start_event_from_screen, "HouseScreens/Claire_Weekend_8AM.webp", "Claire_weekend_8AM")
                focus_mask True
    elif calendar.Hours == HOUR_9AM:
        add "HouseScreens/Breakfast_9AM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Breakfast_9AM_idle.png"
                hover "HouseScreens/Breakfast_9AM_hover.png"
                xpos 1225
                ypos 385
                action Function(start_event_from_screen, "HouseScreens/Breakfast_9AM.webp", "Breakfast_weekend_9AM")
                focus_mask True
    elif calendar.Hours == HOUR_11AM:
        add "HouseScreens/Isabella_weekend_11AM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Isabella_11AM_idle.png"
                hover "HouseScreens/Isabella_11AM_hover.png"
                xpos 752
                ypos 405
                action Function(start_event_from_screen, "HouseScreens/Isabella_weekend_11AM.webp", "Isabella_weekend_11AM")
                focus_mask True
    elif calendar.Hours == HOUR_12PM:
        add "HouseScreens/Isabella_weekend_12PM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Isabella_12PM_idle.png"
                hover "HouseScreens/Isabella_12PM_hover.png"
                xpos 147
                ypos 535
                action Function(start_event_from_screen, "HouseScreens/Isabella_weekend_12PM.webp", "Isabella_weekend_12PM")
                focus_mask True
    elif calendar.Hours == HOUR_1PM:
        add "HouseScreens/Isabella_weekend_1PM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Isabella_1PM_idle.png"
                hover "HouseScreens/Isabella_1PM_hover.png"
                xpos 409
                ypos 484
                action Function(start_event_from_screen, "HouseScreens/Isabella_weekend_1PM.webp", "Isabella_weekend_1PM")
                focus_mask True
    elif is_day_hour(calendar.Hours):
        add "HomeSubplace/garden1.png"
    elif is_evening_hour(calendar.Hours):
        add "HomeSubplace/garden1 evening.png"
    elif is_night_hour(calendar.Hours):
        add "HomeSubplace/garden1 night.png"
