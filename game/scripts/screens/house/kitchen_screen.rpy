init 1 python:
    KITCHEN_WEEKDAY_EVENTS = {
        HOUR_8AM: {
            "bg": "ScenesScreens/JenniferSceneScreens/Jennifer24MorningScreen/JenniferMorning24Screen1.webp",
            "button": {
                "idle": "ScenesScreens/JenniferSceneScreens/Jennifer24MorningScreen/JenniferMorning24Button1_idle.png",
                "hover_tint": CHARACTER_HOVER_TINT,
                "xpos": 952,
                "ypos": 233,
                "jump": "JenniferMorning24",
            },
        },
        HOUR_9PM: {
            "bg": "ScenesScreens/JenniferSceneScreens/Jennifer44EveningScreen/JenniferEvening44Screen1.webp",
            "button": {
                "idle": "ScenesScreens/JenniferSceneScreens/Jennifer44EveningScreen/JenniferEvening44Button1_idle.png",
                "hover_tint": CHARACTER_HOVER_TINT,
                "xpos": 923,
                "ypos": 274,
                "jump": "JenniferEvening44",
            },
        },
    }

    KITCHEN_WEEKEND_EVENTS = {
        HOUR_8AM: {
            "bg": "HouseScreens/Kitchen_Weekend_8AM.webp",
            "button": {
                "idle": "HouseScreens/Kitchen_Weekend_8AM_Button_idle.png",
                "hover_tint": CHARACTER_HOVER_TINT,
                "xpos": 869,
                "ypos": 306,
                "jump": "Jennifer_weekend_8AM",
                "focus_mask": True,
            },
        },
    }

screen KitchenScreen():
    if is_weekday_day(calendar.Day):
        $ scene_def = select_room_scene(
            calendar.Hours,
            KITCHEN_WEEKDAY_EVENTS,
            "HomeSubplace/Kitchen.png",
            "HomeSubplace/Kitchen evening.png",
            "HomeSubplace/Kitchen night.png",
        )
    else:
        $ scene_def = select_room_scene(
            calendar.Hours,
            KITCHEN_WEEKEND_EVENTS,
            "HomeSubplace/Kitchen.png",
            "HomeSubplace/Kitchen evening.png",
            "HomeSubplace/Kitchen night.png",
        )

    if scene_def:
        add scene_def["bg"]
        if should_show_room_buttons():
            use room_scene_buttons(scene_def)
