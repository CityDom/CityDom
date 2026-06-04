screen Garden1WeekendScreen():
    if calendar.Hours == HOUR_7AM:
        add "HouseScreens/Jennifer_Weekend_7AM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Jennifer_7AM_idle.png"
                hover make_tinted_hover_displayable("HouseScreens/Jennifer_7AM_idle.png", CHARACTER_HOVER_TINT)
                xpos 562
                ypos 374
                action Function(start_event_from_screen, "HouseScreens/Jennifer_Weekend_7AM.webp", "Jennifer_weekend_7AM")
                focus_mask True
    elif calendar.Hours == HOUR_8AM:
        add "HouseScreens/Claire_Weekend_8AM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Claire_8AM_idle.png"
                hover make_tinted_hover_displayable("HouseScreens/Claire_8AM_idle.png", CHARACTER_HOVER_TINT)
                xpos 1199
                ypos 380
                action Function(start_event_from_screen, "HouseScreens/Claire_Weekend_8AM.webp", "Claire_weekend_8AM")
                focus_mask True
    elif calendar.Hours == HOUR_9AM:
        add "HouseScreens/Breakfast_9AM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Breakfast_9AM_idle.png"
                hover make_tinted_hover_displayable("HouseScreens/Breakfast_9AM_idle.png", CHARACTER_HOVER_TINT)
                xpos 1225
                ypos 385
                action Function(start_event_from_screen, "HouseScreens/Breakfast_9AM.webp", "Breakfast_weekend_9AM")
                focus_mask True
    elif calendar.Hours == HOUR_11AM:
        add "HouseScreens/Isabella_weekend_11AM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Isabella_11AM_idle.png"
                hover make_tinted_hover_displayable("HouseScreens/Isabella_11AM_idle.png", CHARACTER_HOVER_TINT)
                xpos 752
                ypos 405
                action Function(start_event_from_screen, "HouseScreens/Isabella_weekend_11AM.webp", "Isabella_weekend_11AM")
                focus_mask True
    elif calendar.Hours == HOUR_12PM:
        add "HouseScreens/Isabella_weekend_12PM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Isabella_12PM_idle.png"
                hover make_tinted_hover_displayable("HouseScreens/Isabella_12PM_idle.png", CHARACTER_HOVER_TINT)
                xpos 147
                ypos 535
                action Function(start_event_from_screen, "HouseScreens/Isabella_weekend_12PM.webp", "Isabella_weekend_12PM")
                focus_mask True
    elif calendar.Hours == HOUR_1PM:
        add "HouseScreens/Isabella_weekend_1PM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Isabella_1PM_idle.png"
                hover make_tinted_hover_displayable("HouseScreens/Isabella_1PM_idle.png", CHARACTER_HOVER_TINT)
                xpos 409
                ypos 484
                action Function(start_event_from_screen, "HouseScreens/Isabella_weekend_1PM.webp", "Isabella_weekend_1PM")
                focus_mask True
    elif calendar.Hours == HOUR_6PM:
        add "HouseScreens/Jennifer_Weekend_6PM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Jennifer_6PM_idle.png"
                hover make_tinted_hover_displayable("HouseScreens/Jennifer_6PM_idle.png", CHARACTER_HOVER_TINT)
                xpos 748
                ypos 333
                action Function(start_event_from_screen, "HouseScreens/Jennifer_Weekend_6PM.webp", "Jennifer_Weekend_6PM")
                focus_mask True
    elif calendar.Hours == HOUR_7PM:
        add "HouseScreens/Jennifer_Weekend_7PM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Jennifer_7PM_idle.png"
                hover make_tinted_hover_displayable("HouseScreens/Jennifer_7PM_idle.png", CHARACTER_HOVER_TINT)
                xpos 632
                ypos 376
                action Function(start_event_from_screen, "HouseScreens/Jennifer_Weekend_7PM.webp", "Jennifer_Weekend_7PM")
                focus_mask True                
    elif calendar.Hours == HOUR_8PM:
        add "HouseScreens/Claire_Weekend_8PM.webp"
        if should_show_room_buttons():
            imagebutton:
                idle "HouseScreens/Claire_8PM_idle.png"
                hover make_tinted_hover_displayable("HouseScreens/Claire_8PM_idle.png", CHARACTER_HOVER_TINT)
                xpos 185
                ypos 587
                action Function(start_event_from_screen, "HouseScreens/Claire_Weekend_8PM.webp", "Claire_Weekend_8PM")
                focus_mask True     
    elif is_day_hour(calendar.Hours):
        add "HomeSubplace/garden1.png"
    elif is_evening_hour(calendar.Hours):
        add "HomeSubplace/garden1 evening.png"
    elif is_night_hour(calendar.Hours):
        add "HomeSubplace/garden1 night.png"
