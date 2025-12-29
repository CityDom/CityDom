default last_shower_time = -10 
default Bathroom_Shower_scene = []
default Bathroom_BrushTeeth_scene = []

screen BathroomScreen():
    $ scene_bg = ("HomeSubplace/Bathroom.png" if is_day_hour(calendar.Hours) else
        "HomeSubplace/Bathroom evening.png" if is_evening_hour(calendar.Hours) else
        "HomeSubplace/Bathroom night.png")
    add scene_bg
    if calendar.Day not in [0, 6]:
        if calendar.Hours == HOUR_6AM:
            $ last_shower_time = -10  # Allows showering again in the new day
        if should_show_room_buttons():
            if calendar.Hours == HOUR_6AM:
                    imagebutton:
                        idle "MCEvents/HouseButtons/BathroomSink_idle.webp"
                        hover "MCEvents/HouseButtons/BathroomSink_hover.webp"
                        xpos 1260
                        ypos 545
                        action Function(
                            start_event_from_screen,
                            scene_bg,
                            choose_housefront_scene(
                                ["MC_Bathroom_BrushTeeth_Isabella", "MC_Bathroom_BrushTeeth_Claire", "MC_Bathroom_BrushTeeth_Jennifer", "MC_Bathroom_BrushTeeth_Mhyrorin", "MC_Bathroom_BrushTeeth_Alone"],
                                Bathroom_BrushTeeth_scene
                            )
                        )
                        focus_mask True

            $ available_shower_scenes = ["MC_Bathroom_Shower_Alone"]
            if is_day_hour(calendar.Hours):
                $ available_shower_scenes.append("MC_Bathroom_Shower_Mhyrorin")

            imagebutton:
                idle "shower.png"
                hover "shower.png"
                xpos 600
                ypos 200
                action If(
                    (calendar.Hours - last_shower_time) >= 6 or last_shower_time == -10,
                    [
                        SetVariable("last_shower_time", calendar.Hours),
                        Function(start_event_from_screen, scene_bg, choose_housefront_scene(available_shower_scenes, Bathroom_Shower_scene))
                    ],
                    [
                        Function(start_event_from_screen, scene_bg, "TooSoonToShower")
                    ]
                )
                at bump
                focus_mask True
label TooSoonToShower:
    "I already showered recently, I don't get dirty that fast."
    $ renpy.call("GameLoop")

