default last_pee_time = -10
default Bathroom_Pee_scene = []

screen HouseToiletScreen():
    add "HomeSubplace/HouseToilet.png"
    if calendar.Day not in [0, 6]:
        on "show" action If(calendar.Hours == 2, [Hide("HouseToiletScreen"), Jump("ClaireMorningEvent34")])
        on "show" action If(calendar.Hours == 12, [Hide("HouseToiletScreen"), Jump("IsabellaNightEvent34")])
        on "show" action If(calendar.Hours == 18, [Hide("HouseToiletScreen"), Jump("Jennifer_weekend_7AM")])

        if calendar.Hours == 0:
            $ last_pee_time = -10

        
        if not MapScreenShown and not StatsScreenShown:
            
            if 0 <= calendar.Hours <= 20:
                
                $ available_scenes = ["MC_Toilet_Piss_Alone"]
                
                if not (6 <= calendar.Hours < 10):
                    $ available_scenes.append("MC_Toilet_Piss_Isabella")
                
                if not (6 <= calendar.Hours < 13):
                    $ available_scenes.append("MC_Toilet_Piss_Jennifer")
                
                if calendar.Hours < 12:
                    $ available_scenes.append("MC_Toilet_Piss_Mhyrorin")
                
                imagebutton:
                    idle "MCEvents/HouseButtons/ToiletButton_idle.webp"
                    hover "MCEvents/HouseButtons/ToiletButton_hover.webp"
                    xpos 805
                    ypos 422
                    action If(
                        (calendar.Hours - last_pee_time) >= 4 or last_pee_time == -10,
                        [
                            SetVariable("last_pee_time", calendar.Hours),
                            Hide("HouseToiletScreen"), 
                            Jump(choose_housefront_scene(available_scenes, Bathroom_Pee_scene))  # Use the correct variable
                        ],
                        [
                            Hide("HouseToiletScreen"),
                            Jump("TooSoonToPee")
                        ]
                    )
                    focus_mask True
    if calendar.Day == 0 or calendar.Day == 6:  # Weekend logic
        # on "show" action If(calendar.Hours == 2, [Hide("HouseToiletScreen"), Jump("ClaireMorningEvent34")])
        # on "show" action If(calendar.Hours == 12, [Hide("HouseToiletScreen"), Jump("IsabellaNightEvent34")])
        on "show" action If(calendar.Hours == 1, [Hide("HouseToiletScreen"), Jump("Jennifer_weekend_7AM")])
label TooSoonToPee:
    "I already peed, I don't need to go again so soon."
    $ renpy.call("GameLoop")

