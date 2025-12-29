init 1 python:
    CLAIRE_ROOM_WEEKDAY_EVENTS = {
        HOUR_6AM: {
            "bg": "ScenesScreens/ClaireSceneScreens/Claire14MorningScreen/ClaireMorning14Screen1.webp",
            "button": {
                "idle": "ScenesScreens/ClaireSceneScreens/Claire14MorningScreen/ClaireMorning14Button1_idle.png",
                "hover": "ScenesScreens/ClaireSceneScreens/Claire14MorningScreen/ClaireMorning14Button1_hover.png",
                "xpos": 719,
                "ypos": 277,
                "jump": "ClaireMorningEvent14",
            },
        },
        HOUR_8PM: {
            "bg": "ScenesScreens/ClaireSceneScreens/Claire34EveningScreen/ClaireEvening34Screen1.webp",
            "button": {
                "idle": "ScenesScreens/ClaireSceneScreens/Claire34EveningScreen/ClaireEvening34Button1_idle.png",
                "hover": "ScenesScreens/ClaireSceneScreens/Claire34EveningScreen/ClaireEvening34Button1_hover.png",
                "xpos": 1012,
                "ypos": 264,
                "jump": "ClaireEveningEvent34",
            },
        },
        HOUR_9PM: {
            "bg": "ScenesScreens/ClaireSceneScreens/Claire44EveningScreen/ClaireEvening44Screen1.webp",
            "button": {
                "idle": "ScenesScreens/ClaireSceneScreens/Claire44EveningScreen/ClaireEvening44Button1_idle.png",
                "hover": "ScenesScreens/ClaireSceneScreens/Claire44EveningScreen/ClaireEvening44Button1_hover.png",
                "xpos": 626,
                "ypos": 261,
                "jump": "ClaireEveningEvent44",
            },
        },
        HOUR_2AM: {
            "bg": "ScenesScreens/ClaireSceneScreens/Claire14MidnightScreen/ClaireMidnight14Screen1.webp",
            "button": {
                "idle": "ScenesScreens/ClaireSceneScreens/Claire14MidnightScreen/ClaireMidnight14Button1_idle.png",
                "hover": "ScenesScreens/ClaireSceneScreens/Claire14MidnightScreen/ClaireMidnight14Button1_hover.png",
                "xpos": 712,
                "ypos": 322,
                "jump": "ClaireMidnightEvent14",
            },
        },
    }

    CLAIRE_ROOM_WEEKEND_EVENTS = {
        HOUR_6AM: {
            "bg": "HouseScreens/Claire_Weekend_6AM.webp",
            "button": {
                "idle": "HouseScreens/Claire_6AM_idle.png",
                "hover": "HouseScreens/Claire_6AM_hover.png",
                "xpos": 730,
                "ypos": 348,
                "jump": "Claire_weekend_6AM",
                "focus_mask": True,
            },
        },
    }

screen ClaireRoomScreen():
    if calendar.Day not in [0, 6]:
        $ scene_def = select_room_scene(
            calendar.Hours,
            CLAIRE_ROOM_WEEKDAY_EVENTS,
            "HomeSubplace/Claire room.png",
            "HomeSubplace/Claire room evening.png",
            "HomeSubplace/Claire room night.png",
        )
    else:
        $ scene_def = select_room_scene(
            calendar.Hours,
            CLAIRE_ROOM_WEEKEND_EVENTS,
            "HomeSubplace/Claire room.png",
            "HomeSubplace/Claire room evening.png",
            "HomeSubplace/Claire room night.png",
        )

    if scene_def:
        add scene_def["bg"]
        if scene_def.get("button") and should_show_room_buttons():
            $ button = scene_def["button"]
            $ focus_mask_value = button.get("focus_mask")
            imagebutton:
                idle button["idle"]
                hover button["hover"]
                xpos button["xpos"]
                ypos button["ypos"]
                action Function(start_event_from_screen, scene_def["bg"], button["jump"])
                if focus_mask_value is not None:
                    focus_mask focus_mask_value
