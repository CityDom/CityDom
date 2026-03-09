init 1 python:
    def make_livingroom_button(idle, hover, xpos, ypos, jump=None, choices=None, history_key=None, focus_mask=True):
        button = {
            "idle": idle,
            "hover": hover,
            "xpos": xpos,
            "ypos": ypos,
            "focus_mask": focus_mask,
        }
        if jump is not None:
            button["jump"] = jump
        elif choices and history_key:
            button["choices"] = choices
            button["history_key"] = history_key
        return button

    def make_livingroom_couch_button(jump=None, choices=None, history_key=None, evening=False):
        idle = "MCEvents/HouseButtons/CouchButton_Evening_idle.webp" if evening else "MCEvents/HouseButtons/CouchButton_idle.webp"
        hover = "MCEvents/HouseButtons/CouchButton_Evening_hover.webp" if evening else "MCEvents/HouseButtons/CouchButton_hover.webp"
        return make_livingroom_button(idle, hover, 975, 515, jump=jump, choices=choices, history_key=history_key)

    LIVINGROOM_WEEKDAY_SCENES = {
        HOUR_6AM: {
            "bg": "HomeSubplace/LivingRoom.png",
            "buttons": [
                make_livingroom_couch_button(
                    choices=[
                        "MC_Livingroom_Movie_Morning_Jennifer_Label",
                        "MC_Livingroom_Movie_Morning_Isabella_Label",
                        "MC_Livingroom_Movie_Morning_Alone_Label",
                    ],
                    history_key="livingroom_morning",
                )
            ],
        },
        HOUR_7AM: {
            "bg": "ScenesScreens/ClaireSceneScreens/Claire24MorningScreen/ClaireMorning24Screen1.png",
            "buttons": [
                make_livingroom_button(
                    "ScenesScreens/ClaireSceneScreens/Claire24MorningScreen/ClaireMorning24Button1_idle.png",
                    "ScenesScreens/ClaireSceneScreens/Claire24MorningScreen/ClaireMorning24Button1_hover.png",
                    1440,
                    274,
                    jump="ClaireMorningEvent24",
                ),
                make_livingroom_couch_button(jump="MC_Livingroom_Movie_7AM_Claire_Label"),
            ],
        },
        HOUR_8AM: {"bg": "HomeSubplace/LivingRoom.png", "buttons": [make_livingroom_couch_button(jump="MC_Livingroom_Movie_8AM_Jennifer_Label")]},
        HOUR_9AM: {
            "bg": "ScenesScreens/DinnerSceneScreens/DinnerScreen1/DinnerScreen1.png",
            "buttons": [
                make_livingroom_button(
                    "ScenesScreens/DinnerSceneScreens/DinnerScreen1/DinnerScreenButton1_idle.png",
                    "ScenesScreens/DinnerSceneScreens/DinnerScreen1/DinnerScreenButton1_hover.png",
                    1223,
                    274,
                    jump="DinnerGroupEvent",
                ),
                make_livingroom_couch_button(jump="MC_Livingroom_Movie_9AM_All_Label"),
            ],
        },
        HOUR_10AM: {"bg": "HomeSubplace/LivingRoom.png", "buttons": [make_livingroom_couch_button(jump="MC_Livingroom_Movie_Morning_Alone_Label")]},
        HOUR_11AM: {"bg": "HomeSubplace/LivingRoom.png", "buttons": [make_livingroom_couch_button(jump="MC_Livingroom_Movie_11AM_Jennifer_Label")]},
        HOUR_12PM: {
            "bg": "HomeSubplace/LivingRoom.png",
            "buttons": [
                make_livingroom_couch_button(
                    choices=["MC_Livingroom_Movie_Morning_Alone_Label", "MC_Livingroom_Movie_12PM_Mhyrorin_Label"],
                    history_key="livingroom_12PM",
                )
            ],
        },
        HOUR_1PM: {
            "bg": "HomeSubplace/LivingRoom.png",
            "buttons": [
                make_livingroom_couch_button(
                    choices=["MC_Livingroom_Movie_Morning_Alone_Label", "MC_Livingroom_Movie_1PM_Mhyrorin_Label"],
                    history_key="livingroom_1PM",
                )
            ],
        },
        HOUR_2PM: {
            "bg": "HomeSubplace/LivingRoom.png",
            "buttons": [
                make_livingroom_couch_button(
                    choices=["MC_Livingroom_Movie_Morning_Alone_Label", "MC_Livingroom_Movie_2PM_Mhyrorin_Label"],
                    history_key="livingroom_2PM",
                )
            ],
        },
        HOUR_3PM: {
            "bg": "HomeSubplace/LivingRoom.png",
            "buttons": [
                make_livingroom_couch_button(
                    choices=["MC_Livingroom_Movie_Morning_Alone_Label", "MC_Livingroom_Movie_3PM_Mhyrorin_Label"],
                    history_key="livingroom_3PM",
                )
            ],
        },
        HOUR_4PM: {
            "bg": "HomeSubplace/LivingRoom.png",
            "buttons": [
                make_livingroom_couch_button(
                    choices=["MC_Livingroom_Movie_Morning_Alone_Label", "MC_Livingroom_Movie_4PM_Isabella_Label"],
                    history_key="livingroom_4PM",
                )
            ],
        },
        HOUR_5PM: {
            "bg": "HomeSubplace/LivingRoom.png",
            "buttons": [
                make_livingroom_couch_button(
                    choices=["MC_Livingroom_Movie_Morning_Alone_Label", "MC_Livingroom_Movie_5PM_Isabella_Label"],
                    history_key="livingroom_5PM",
                )
            ],
        },
        HOUR_6PM: {
            "bg": "HomeSubplace/LivingRoom evening.png",
            "buttons": [
                make_livingroom_couch_button(
                    choices=["MC_Livingroom_Movie_Morning_Alone_Label", "MC_Livingroom_Movie_6PM_Isabella_Label"],
                    history_key="livingroom_6PM",
                    evening=True,
                )
            ],
        },
        HOUR_7PM: {
            "bg": "ScenesScreens/IsabellaSceneScreens/Isabella24EveningScreen/IsabellaEvening24Screen1.png",
            "buttons": [
                make_livingroom_button(
                    "ScenesScreens/IsabellaSceneScreens/Isabella24EveningScreen/IsabellaEvening24Button1_idle.png",
                    "ScenesScreens/IsabellaSceneScreens/Isabella24EveningScreen/IsabellaEvening24Button1_hover.png",
                    1125,
                    463,
                    jump="IsabellaEveningEvent24",
                )
            ],
        },
        HOUR_8PM: {"bg": "HomeSubplace/LivingRoom evening.png", "buttons": [make_livingroom_couch_button(jump="MC_Livingroom_Movie_8PM_MC_Alone_Label", evening=True)]},
        HOUR_9PM: {
            "bg": "MCEvents/HouseButtons/JenniferInTheKitchen.webp",
            "buttons": [
                make_livingroom_couch_button(
                    choices=["MC_Livingroom_Movie_8PM_MC_Alone_Label", "MC_Livingroom_Movie_9PM_Jennifer_Label"],
                    history_key="livingroom_9PM",
                    evening=True,
                )
            ],
        },
        HOUR_10PM: {
            "bg": "ScenesScreens/LunchSceneScreens/LunchScreen1/LunchScreen1.webp",
            "buttons": [
                make_livingroom_button(
                    "ScenesScreens/LunchSceneScreens/LunchScreen1/LunchScreenButton1_idle.png",
                    "ScenesScreens/LunchSceneScreens/LunchScreen1/LunchScreenButton1_hover.png",
                    1223,
                    278,
                    jump="LunchGroupEvent",
                ),
                make_livingroom_couch_button(jump="MC_Livingroom_Movie_10PM_All_Label", evening=True),
            ],
        },
        HOUR_11PM: {
            "bg": "ScenesScreens/MovieNightSceneScreens/MovieNightScreen1/MovieNightScreen1.webp",
            "buttons": [
                make_livingroom_button(
                    "ScenesScreens/MovieNightSceneScreens/MovieNightScreen1/MovieNightScreenButton1_idle.png",
                    "ScenesScreens/MovieNightSceneScreens/MovieNightScreen1/MovieNightScreenButton1_hover.png",
                    990,
                    344,
                    jump="MovieNightEvent",
                )
            ],
        },
        HOUR_12AM: {
            "bg": "MCEvents/HouseButtons/Livingroom_Night.webp",
            "buttons": [
                make_livingroom_couch_button(
                    choices=["MC_Livingroom_Movie_12AM_Alone_Label", "MC_Livingroom_Movie_12AM_Isabella_Label"],
                    history_key="livingroom_12AM",
                    evening=True,
                )
            ],
        },
        HOUR_1AM: {
            "bg": "ScenesScreens/ClaireSceneScreens/Claire44NightScreen/ClaireNight44Screen1.png",
            "buttons": [
                make_livingroom_button(
                    "ScenesScreens/ClaireSceneScreens/Claire44NightScreen/ClaireNight44Button1_idle.png",
                    "ScenesScreens/ClaireSceneScreens/Claire44NightScreen/ClaireNight44Button1_hover.png",
                    1187,
                    364,
                    jump="ClaireNightEvent44",
                )
            ],
        },
        HOUR_2AM: {
            "bg": "MCEvents/HouseButtons/Livingroom_Night.webp",
            "buttons": [
                make_livingroom_couch_button(
                    choices=[
                        "MC_Livingroom_Movie_2AM_Alone_Label",
                        "MC_Livingroom_Movie_2AM_Isabella_Label",
                        "MC_Livingroom_Movie_2AM_Jennifer_Label",
                        "MC_Livingroom_Movie_2AM_Claire_Label",
                        "MC_Livingroom_Movie_2AM_Mhyrorin_Label",
                    ],
                    history_key="livingroom_2AM",
                    evening=True,
                )
            ],
        },
    }

    LIVINGROOM_WEEKEND_SCENES = {
        HOUR_4PM: {
            "bg": "HouseScreens/Jennifer_weekend_4PM.webp",
            "buttons": [
                make_livingroom_button(
                    "HouseScreens/Jennifer_4PM_idle.png",
                    "HouseScreens/Jennifer_4PM_hover.png",
                    961,
                    537,
                    jump="Jennifer_weekend_4PM",
                )
            ],
        }
    }

    def get_livingroom_default_scene(hour):
        if is_day_hour(hour):
            return {"bg": "HomeSubplace/LivingRoom.png"}
        if is_evening_hour(hour):
            return {"bg": "HomeSubplace/LivingRoom evening.png"}
        return {"bg": "HomeSubplace/LivingRoom night.png"}

    def get_livingroom_scene(day, hour):
        scene_map = LIVINGROOM_WEEKEND_SCENES if is_weekend_day(day) else LIVINGROOM_WEEKDAY_SCENES
        scene_def = scene_map.get(hour)
        if scene_def:
            return scene_def
        return get_livingroom_default_scene(hour)


screen LivingroomScreen():
    $ scene_def = get_livingroom_scene(calendar.Day, calendar.Hours)

    add scene_def["bg"]

    if should_show_room_buttons():
        use room_scene_buttons(scene_def)
