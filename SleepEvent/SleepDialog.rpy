label SleepEvent:
    if str(Location).lower() == "my room":
        menu:
            "Sleep dressed":
                scene BlackScreen with Dissolve(2)
                "{color=#808080}**You fall asleep**{/color}"
                "{color=#808080}**The next day.**{/color}"
                label SleepDressed:
                    $ reset_EnglishClass_encounters()
                    $ reset_artClass_watched_scenes()
                    $ reset_bio_class_scenes()
                    $ reset_nurse_scene_variables()
                    $ reset_swim_class_scene_variables()
                    $ reset_principalOffice_scene_variables()
                    $ reset_GymClass_scene_variables()
                    $ reset_detention_scene_variables()
                    $ school_clock.hour = 12
                    $ school_clock.period = 0
                    $ calendar.advance_to_next_day()
                    scene SleepScene1 with Dissolve(0.5)
                    MC "....."
                    scene SleepScene2 with Dissolve(0.5)
                    MC "{color=#808080}*It's morning already...*{/color}"
                    MC "{color=#808080}*I should get out of bed...*{/color}"
                    $ Location = "my room"
                    $ calendar.Hours = 0
                    $ calendar.update_sub_place_data()
                    $ renpy.call("GameLoop")
            "Sleep naked":
                $ reset_EnglishClass_encounters()
                $ reset_artClass_watched_scenes()
                $ reset_bio_class_scenes()
                $ reset_nurse_scene_variables()
                $ reset_swim_class_scene_variables()
                $ reset_principalOffice_scene_variables()
                $ reset_GymClass_scene_variables()
                $ reset_detention_scene_variables()
                $ school_clock.hour = 12
                $ school_clock.period = 0
                scene BlackScreen with Dissolve(4)
                "{color=#808080}**You fall asleep.**{/color}"
                "{color=#808080}**The next day.**{/color}"
                $ calendar.advance_to_next_day()
                scene SleepScene3 with Dissolve(0.5)
                MC "....."
                scene SleepScene4 with Dissolve(0.5)
                MC "{color=#808080}*It's morning already...*{/color}"
                MC "{color=#808080}*Should I go back to sleep?*{/color}"
                menu:
                    "Sleep some more":
                        MC "{color=#808080}*Fuck it... it's way too early to get up.*{/color}"
                        MC "{color=#808080}*I'll sleep 5 more minutes...*{/color}"
                        scene BlackScreen with Dissolve(2)
                        "{size=+30}{color=#FF0000}~KNOCK KNOCK KNOCK~{/color}{/size}"
                        McMom "[MC_upper], ARE YOU AWAKE?!"
                        McMom "GET UP ALREADY, THE BREAKFAST IS ALMOST DONE!!!"
                        McMom "WHAT ARE YOU DOING?!"
                        McMom "I'M COMING IN!!"
                        scene SleepScene5 with Dissolve(0.5)
                        McMom "Come on, [MC]."
                        McMom "I told you to stop going to bad so late!"
                        scene SleepScene6 with Dissolve(0.5)
                        McMom "It's really not healthy!"
                        McMom "Now wake up alre-"
                        scene SleepScene7 with Dissolve(0.5)
                        McMom "...."
                        McMom "{color=#808080}*What the ....*{/color}"
                        scene SleepScene8 with Dissolve(0.5)
                        McMom "[MC_upper], WHY ARE YOU NAKED?!?!"
                        McMom "YOU ARE SO GROUNDED FOR THIS!!!!"
                        scene SleepScene3 with Dissolve(0.5)
                        MC "{color=#808080}*Huhh....*{/color}"
                        MC "{color=#808080}*I think I heard mom calling me...*{/color}"
                        scene SleepScene4 with Dissolve(0.5)
                        MC "{color=#808080}*She doesn't seem to be here.*{/color}"
                        MC "{color=#808080}*But I can swear that I heard her.*{/color}"
                        MC "{color=#808080}*And the door slamming shut.*{/color}"
                        MC "{color=#808080}*In any case, I should wake up...*{/color}"
                        $ Mom_Corruption = Mom_Corruption + 2
                        $ Mom_Obedience = Mom_Obedience + 2
                        $ Mom_love = Mom_love - 2
                        "{color=#808080}**Mom love - 2**{color=#808080}"
                        "{color=#808080}**Mom corruption + 2**{color=#808080}"
                        "{color=#808080}**Mom obedience + 2**{color=#808080}"
                        $ Location = "my room"
                        $ calendar.Hours = 2
                        $ calendar.update_sub_place_data()
                        $ renpy.call("GameLoop")
                    "Get out of bed":
                        MC "{color=#808080}*Yea... let's start the day.*{/color}"
                        $ Location = "my room"
                        $ calendar.Hours = 0
                        $ calendar.update_sub_place_data()
                        $ renpy.call("GameLoop")
            "Don't sleep yet":
                $ current_location = str(Location).lower()
                jump GameLoop
    else:
        MC "I'm so tiered, maybe I should go to my room to get some sleep."
        $ renpy.call("GameLoop")