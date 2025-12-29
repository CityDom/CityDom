init 1 python:
    KITCHEN_WEEKDAY_EVENTS = {
        HOUR_8AM: {
            "bg": "ScenesScreens/JenniferSceneScreens/Jennifer24MorningScreen/JenniferMorning24Screen1.webp",
            "button": {
                "idle": "ScenesScreens/JenniferSceneScreens/Jennifer24MorningScreen/JenniferMorning24Button1_idle.png",
                "hover": "ScenesScreens/JenniferSceneScreens/Jennifer24MorningScreen/JenniferMorning24Button1_hover.png",
                "xpos": 952,
                "ypos": 233,
                "jump": "JenniferMorning24",
            },
        },
        HOUR_9PM: {
            "bg": "ScenesScreens/JenniferSceneScreens/Jennifer44EveningScreen/JenniferEvening44Screen1.webp",
            "button": {
                "idle": "ScenesScreens/JenniferSceneScreens/Jennifer44EveningScreen/JenniferEvening44Button1_idle.png",
                "hover": "ScenesScreens/JenniferSceneScreens/Jennifer44EveningScreen/JenniferEvening44Button1_hover.png",
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
                "hover": "HouseScreens/Kitchen_Weekend_8AM_Button_hover.png",
                "xpos": 869,
                "ypos": 306,
                "jump": "Jennifer_weekend_8AM",
                "focus_mask": True,
            },
        },
    }

screen KitchenScreen():
    if calendar.Day not in [0, 6]:
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
        if scene_def.get("button") and should_show_room_buttons():
            $ button = scene_def["button"]
            $ focus_mask_value = button.get("focus_mask")
            use event_imagebutton(
                idle=button["idle"],
                hover=button["hover"],
                xpos=button["xpos"],
                ypos=button["ypos"],
                bg=scene_def["bg"],
                label=button["jump"],
                focus_mask=focus_mask_value,
            )
