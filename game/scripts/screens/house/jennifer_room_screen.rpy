init 1 python:
    JENNIFER_ROOM_WEEKDAY_EVENTS = {
        HOUR_6AM: {
            "bg": "ScenesScreens/JenniferSceneScreens/Jennifer14MorningScreen/JenniferMorning14Screen1.png",
            "button": {
                "idle": "ScenesScreens/JenniferSceneScreens/Jennifer14MorningScreen/JenniferMorning14Button1_idle.png",
                "hover": "ScenesScreens/JenniferSceneScreens/Jennifer14MorningScreen/JenniferMorning14Button1_hover.png",
                "xpos": 927,
                "ypos": 361,
                "jump": "JenniferMorningEvent14",
            },
        },
        HOUR_9PM: {
            "bg": "ScenesScreens/IsabellaSceneScreens/Isabella44EveningScreen/IsabellaEvening44Screen1.webp",
            "button": {
                "idle": "ScenesScreens/IsabellaSceneScreens/Isabella44EveningScreen/IsabellaEvening44Button1_idle.png",
                "hover": "ScenesScreens/IsabellaSceneScreens/Isabella44EveningScreen/IsabellaEvening44Button1_hover.png",
                "xpos": 1699,
                "ypos": 515,
                "jump": "IsabellaEveningEvent44",
            },
        },
        HOUR_1AM: {
            "bg": "ScenesScreens/JenniferSceneScreens/Jennifer34NightScreen/JenniferNight34Screen1.webp",
            "button": {
                "idle": "ScenesScreens/JenniferSceneScreens/Jennifer34NightScreen/JenniferNight34Button1_idle.png",
                "hover": "ScenesScreens/JenniferSceneScreens/Jennifer34NightScreen/JenniferNight34Button1_hover.png",
                "xpos": 995,
                "ypos": 285,
                "jump": "JenniferNightEvent34",
            },
        },
        HOUR_2AM: {
            "bg": "ScenesScreens/JenniferSceneScreens/Jennifer44NightScreen/JenniferNight44Screen1.webp",
            "button": {
                "idle": "ScenesScreens/JenniferSceneScreens/Jennifer44NightScreen/JenniferNight44Button1_idle.png",
                "hover": "ScenesScreens/JenniferSceneScreens/Jennifer44NightScreen/JenniferNight44Button1_hover.png",
                "xpos": 1080,
                "ypos": 457,
                "jump": "JenniferNightEvent44",
            },
        },
    }

    JENNIFER_ROOM_WEEKEND_EVENTS = {
        HOUR_6AM: {
            "bg": "HouseScreens/Jennifer_Weekend_6AM.webp",
            "button": {
                "idle": "HouseScreens/Jennifer_6AM_idle.png",
                "hover": "HouseScreens/Jennifer_6AM_hover.png",
                "xpos": 1119,
                "ypos": 396,
                "jump": "Jennifer_weekend_6AM",
                "focus_mask": True,
            },
        },
    }

screen JenniferRoomScreen():
    if calendar.Day not in [0, 6]:
        $ scene_def = select_room_scene(
            calendar.Hours,
            JENNIFER_ROOM_WEEKDAY_EVENTS,
            "HomeSubplace/Jennifer room.png",
            "HomeSubplace/Jennifer room evening.png",
            "HomeSubplace/Jennifer room night.png",
        )
    else:
        $ scene_def = select_room_scene(
            calendar.Hours,
            JENNIFER_ROOM_WEEKEND_EVENTS,
            "HouseScreens/Jennifer_Room_Weekend_Day.webp",
            "HomeSubplace/Jennifer room evening.png",
            "HomeSubplace/Jennifer room night.png",
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
