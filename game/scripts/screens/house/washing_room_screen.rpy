init 1 python:
    WASHING_ROOM_WEEKEND_EVENTS = {
        HOUR_8PM: {
            "bg": "HouseScreens/Jennifer_weekend_8PM.webp",
            "button": {
                "idle": "HouseScreens/Jennifer_8PM_idle.png",
                "hover": "HouseScreens/Jennifer_8PM_hover.png",
                "xpos": 1307,
                "ypos": 615,
                "jump": "Jennifer_weekend_8PM",
                "focus_mask": True,
            },
        },
    }

screen WashingRoomScreen():
    if is_weekend_day(calendar.Day):
        $ scene_def = select_room_scene(
            calendar.Hours,
            WASHING_ROOM_WEEKEND_EVENTS,
            "HomeSubplace/Washing Room.png",
            "HomeSubplace/Washing Room evening.png",
            "HomeSubplace/Washing Room night.png",
        )
    else:
        $ scene_def = select_room_scene(
            calendar.Hours,
            {},
            "HomeSubplace/Washing Room.png",
            "HomeSubplace/Washing Room evening.png",
            "HomeSubplace/Washing Room night.png",
        )

    if scene_def:
        add scene_def["bg"]
        if should_show_room_buttons():
            use room_scene_buttons(scene_def)
