init 1 python:
    ISABELLA_ROOM_WEEKDAY_EVENTS = {
        HOUR_6AM: {
            "bg": "ScenesScreens/IsabellaSceneScreens/Isabella14MorningScreen/IsabellaMorning14Screen1.webp",
            "button": {
                "idle": "ScenesScreens/IsabellaSceneScreens/Isabella14MorningScreen/IsabellaMorning14Button1_idle.png",
                "hover": "ScenesScreens/IsabellaSceneScreens/Isabella14MorningScreen/IsabellaMorning14Button1_hover.png",
                "xpos": 720,
                "ypos": 331,
                "jump": "IsabellaMorningEvent14",
            },
        },
        HOUR_7AM: {
            "bg": "ScenesScreens/IsabellaSceneScreens/Isabella34MorningScreen/IsabellaMorning34Screen1.webp",
            "button": {
                "idle": "ScenesScreens/IsabellaSceneScreens/Isabella34MorningScreen/IsabellaMorning34Button1_idle.png",
                "hover": "ScenesScreens/IsabellaSceneScreens/Isabella34MorningScreen/IsabellaMorning34Button1_hover.png",
                "xpos": 662,
                "ypos": 340,
                "jump": "IsabellaMorningEvent34",
            },
        },
        HOUR_8PM: {
            "bg": "ScenesScreens/IsabellaSceneScreens/Isabella34EveningScreen/IsabellaEvening34Screen1.webp",
            "button": {
                "idle": "ScenesScreens/IsabellaSceneScreens/Isabella34EveningScreen/IsabellaEvening34Button1_idle.png",
                "hover": "ScenesScreens/IsabellaSceneScreens/Isabella34EveningScreen/IsabellaEvening34Button1_hover.png",
                "xpos": 663,
                "ypos": 370,
                "jump": "IsabellaEveningEvent34",
            },
        },
        HOUR_12AM: {
            "bg": "ScenesScreens/IsabellaSceneScreens/Isabella44AfternoonScreen/IsabellaAfternoon44Screen1.webp",
            "button": {
                "idle": "ScenesScreens/IsabellaSceneScreens/Isabella44AfternoonScreen/IsabellaAfternoon44Button1_idle.png",
                "hover": "ScenesScreens/IsabellaSceneScreens/Isabella44AfternoonScreen/IsabellaAfternoon44Button1_hover.png",
                "xpos": 1263,
                "ypos": 339,
                "jump": "IsabellaAfterNoonEvent44",
            },
        },
        HOUR_1AM: {
            "bg": "ScenesScreens/IsabellaSceneScreens/Isabella44NightScreen/IsabellaNight44Screen1.webp",
            "button": {
                "idle": "ScenesScreens/IsabellaSceneScreens/Isabella44NightScreen/IsabellaNight44Button1_idle.png",
                "hover": "ScenesScreens/IsabellaSceneScreens/Isabella44NightScreen/IsabellaNight44Button1_hover.png",
                "xpos": 753,
                "ypos": 398,
                "jump": "IsabellaNightEvent44",
            },
        },
        HOUR_2AM: {
            "bg": "ScenesScreens/IsabellaSceneScreens/Isabella14MidnightScreen/IsabellaMidnight14Screen1.webp",
            "button": {
                "idle": "ScenesScreens/IsabellaSceneScreens/Isabella14MidnightScreen/IsabellaMidnight14Button1_idle.png",
                "hover": "ScenesScreens/IsabellaSceneScreens/Isabella14MidnightScreen/IsabellaMidnight14Button1_hover.png",
                "xpos": 823,
                "ypos": 401,
                "jump": "IsabellaMidnightEvent14",
            },
        },
    }

    ISABELLA_ROOM_WEEKEND_EVENTS = {
        HOUR_6AM: {
            "bg": "HouseScreens/Isabella_Weekend_6AM.webp",
            "button": {
                "idle": "HouseScreens/Isabella_6AM_idle.png",
                "hover": "HouseScreens/Isabella_6AM_hover.png",
                "xpos": 714,
                "ypos": 403,
                "jump": "Isabella_weekend_6AM",
                "focus_mask": True,
            },
        },
        HOUR_7AM: {
            "bg": "HouseScreens/Isabella_Weekend_7AM.webp",
            "button": {
                "idle": "HouseScreens/Isabella_7AM_idle.png",
                "hover": "HouseScreens/Isabella_7AM_hover.png",
                "xpos": 795,
                "ypos": 367,
                "jump": "Isabella_weekend_7AM",
                "focus_mask": True,
            },
        },
        HOUR_2PM: {
            "bg": "HouseScreens/Isabella_Weekend_2PM.webp",
            "button": {
                "idle": "HouseScreens/Isabella_2PM_idle.png",
                "hover": "HouseScreens/Isabella_2PM_hover.png",
                "xpos": 778,
                "ypos": 353,
                "jump": "Isabella_weekend_2PM",
                "focus_mask": True,
            },
        },
        HOUR_4PM: {
            "bg": "HouseScreens/Isabella_Weekend_4PM.webp",
            "button": {
                "idle": "HouseScreens/Isabella_4PM_idle.png",
                "hover": "HouseScreens/Isabella_4PM_hover.png",
                "xpos": 932,
                "ypos": 572,
                "jump": "Isabella_weekend_4PM",
                "focus_mask": True,
            },
        },
        HOUR_5PM: {
            "bg": "HouseScreens/Isabella_Weekend_5PM.webp",
            "button": {
                "idle": "HouseScreens/Isabella_5PM_idle.png",
                "hover": "HouseScreens/Isabella_5PM_hover.png",
                "xpos": 932,
                "ypos": 414,
                "jump": "Isabella_weekend_5PM",
                "focus_mask": True,
            },
        },
    }

screen IsabellaRoomScreen():
    if is_weekday_day(calendar.Day):
        $ scene_def = select_room_scene(
            calendar.Hours,
            ISABELLA_ROOM_WEEKDAY_EVENTS,
            "HomeSubplace/Isabella room.png",
            "HomeSubplace/Isabella room evening.png",
            "HomeSubplace/Isabella room night.png",
        )
    else:
        $ scene_def = select_room_scene(
            calendar.Hours,
            ISABELLA_ROOM_WEEKEND_EVENTS,
            "HomeSubplace/Isabella room.png",
            "HomeSubplace/Isabella room evening.png",
            "HomeSubplace/Isabella room night.png",
        )

    if scene_def:
        add scene_def["bg"]
        if should_show_room_buttons():
            use room_scene_buttons(scene_def)
