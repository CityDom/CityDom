init 1 python:
    def make_housefront_button(jump=None, choices=None, history_key=None, return_to=None, hide_screen=None):
        button = {
            "idle": "EntranceScreen/EntranceDoor_idle.png",
            "hover_tint": OBJECT_HOVER_TINT,
            "xpos": 915,
            "ypos": 199,
            "focus_mask": True,
        }
        if jump is not None:
            button["jump"] = jump
        elif choices and history_key:
            button["choices"] = choices
            button["history_key"] = history_key
        elif return_to is not None:
            button["return_to"] = return_to
            if hide_screen is not None:
                button["hide_screen"] = hide_screen
        return button

    HOUSEFRONT_EVENT_SCENES = {
        HOUR_6AM: {
            "bg": "HomeSubplace/Housefront.png",
            "buttons": [
                make_housefront_button(
                    choices=["MC_GetsHome_Claire_6AM", "MC_GetsHome_Jennifer_6AM", "MC_GetsHome_Isabella_6AM"],
                    history_key="housefront_6AM",
                )
            ],
        },
        HOUR_7AM: {
            "bg": "HomeSubplace/Housefront.png",
            "buttons": [
                make_housefront_button(
                    choices=["MC_GetsHome_Claire_6AM", "MC_GetsHome_Isabella_7AM"],
                    history_key="housefront_7AM",
                )
            ],
        },
        HOUR_8AM: {"bg": "HomeSubplace/Housefront.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Isabella_8AM")]},
        HOUR_9AM: {"bg": "HomeSubplace/Housefront.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Jennifer_9AM")]},
        HOUR_10AM: {"bg": "HomeSubplace/Housefront.png", "buttons": [make_housefront_button(jump="MC_GetsHome_All_10AM")]},
        HOUR_11AM: {"bg": "HomeSubplace/Housefront.png", "buttons": [make_housefront_button(jump="MC_GetsHome_All_11AM")]},
        HOUR_12PM: {"bg": "HomeSubplace/Housefront.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Mhyrorin_12PM")]},
        HOUR_1PM: {"bg": "HomeSubplace/Housefront.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Mhyrorin_1PM")]},
        HOUR_2PM: {"bg": "HomeSubplace/Housefront.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Mhyrorin_2PM")]},
        HOUR_3PM: {"bg": "HomeSubplace/Housefront.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Mhyrorin_3PM")]},
        HOUR_4PM: {"bg": "HomeSubplace/Housefront.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Isabella_4PM")]},
        HOUR_5PM: {"bg": "HomeSubplace/Housefront.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Isabella_5PM")]},
        HOUR_6PM: {"bg": "HomeSubplace/Housefront evening.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Claire_6PM")]},
        HOUR_7PM: {"bg": "HomeSubplace/Housefront evening.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Jennifer_7PM")]},
        HOUR_8PM: {
            "bg": "HomeSubplace/Housefront evening.png",
            "buttons": [
                make_housefront_button(
                    choices=["MC_GetsHome_Claire_8PM", "MC_GetsHome_Isabella_8PM"],
                    history_key="housefront_8PM",
                )
            ],
        },
        HOUR_9PM: {"bg": "HomeSubplace/Housefront evening.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Jennifer_9PM")]},
        HOUR_10PM: {"bg": "HomeSubplace/Housefront night.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Jennifer_10PM")]},
        HOUR_11PM: {"bg": "HomeSubplace/Housefront night.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Isabella_11PM")]},
        HOUR_12AM: {"bg": "HomeSubplace/Housefront night.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Isabella_12AM")]},
        HOUR_1AM: {"bg": "HomeSubplace/Housefront night.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Claire_1AM")]},
        HOUR_2AM: {"bg": "HomeSubplace/Housefront night.png", "buttons": [make_housefront_button(jump="MC_GetsHome_Mhyrorin_2AM")]},
    }

    def get_housefront_fallback_scene(hour):
        if is_day_hour(hour):
            bg = "HomeSubplace/Housefront.png"
        elif is_evening_hour(hour):
            bg = "HomeSubplace/Housefront evening.png"
        else:
            bg = "HomeSubplace/Housefront night.png"

        return {
            "bg": bg,
            "buttons": [
                make_housefront_button(
                    return_to="Entrance",
                    hide_screen="HousefrontScreen",
                )
            ],
        }

    def get_housefront_scene(hour):
        scene_def = HOUSEFRONT_EVENT_SCENES.get(hour)
        if scene_def:
            return scene_def
        return get_housefront_fallback_scene(hour)


screen HousefrontScreen():
    $ scene_def = get_housefront_scene(calendar.Hours)

    add scene_def["bg"]

    if should_show_room_buttons():
        use room_scene_buttons(scene_def)
