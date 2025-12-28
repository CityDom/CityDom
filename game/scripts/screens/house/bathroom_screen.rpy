default last_shower_time = -10 
default Bathroom_Shower_scene = []
default Bathroom_BrushTeeth_scene = []

screen BathroomScreen():
    add ("HomeSubplace/Bathroom.png" if calendar.Hours < 12 else 
        "HomeSubplace/Bathroom evening.png" if calendar.Hours < 16 else 
        "HomeSubplace/Bathroom night.png")
    if calendar.Day not in [0, 6]:
        if calendar.Hours == 0:
            $ last_shower_time = -10  # Allows showering again in the new day
        if not MapScreenShown and not StatsScreenShown:
            if calendar.Hours == 0:
                imagebutton:
                    idle "MCEvents/HouseButtons/BathroomSink_idle.webp"
                    hover "MCEvents/HouseButtons/BathroomSink_hover.webp"
                    xpos 1260
                    ypos 545
                    action [
                        Hide("BathroomScreen"), 
                        Jump(choose_housefront_scene(
                            ["MC_Bathroom_BrushTeeth_Isabella", "MC_Bathroom_BrushTeeth_Claire", "MC_Bathroom_BrushTeeth_Jennifer", "MC_Bathroom_BrushTeeth_Mhyrorin", "MC_Bathroom_BrushTeeth_Alone"], 
                            Bathroom_BrushTeeth_scene
                        ))
                    ]
                    focus_mask True

            $ available_shower_scenes = ["MC_Bathroom_Shower_Alone"]
            if calendar.Hours < 12:
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
                        Hide("BathroomScreen"), 
                        Jump(choose_housefront_scene(available_shower_scenes, Bathroom_Shower_scene))
                    ],
                    [
                        Hide("BathroomScreen"),
                        Jump("TooSoonToShower")
                    ]
                )
                at bump
                focus_mask True
label TooSoonToShower:
    "I already showered recently, I don't get dirty that fast."
    $ renpy.call("GameLoop")

