default last_pee_time = -10
default Bathroom_Pee_scene = []

screen HouseToiletScreen():
    add "HomeSubplace/HouseToilet.png"
    if calendar.Day not in [0, 6]:
        if calendar.Hours == HOUR_6AM:
            $ last_pee_time = -10

        
        if should_show_room_buttons():
            
            if is_in_window(calendar.Hours, HOUR_6AM, HOUR_2AM, inclusive_end=True):
                
                $ available_scenes = ["MC_Toilet_Piss_Alone"]
                
                if not is_in_window(calendar.Hours, HOUR_12PM, HOUR_4PM):
                    $ available_scenes.append("MC_Toilet_Piss_Isabella")
                
                if not is_in_window(calendar.Hours, HOUR_12PM, HOUR_7PM):
                    $ available_scenes.append("MC_Toilet_Piss_Jennifer")
                
                if is_day_hour(calendar.Hours):
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
label TooSoonToPee:
    "I already peed, I don't need to go again so soon."
    $ renpy.call("GameLoop")

