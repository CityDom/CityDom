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
                    $ reset_breakfast_weekend_9am_flags_for_new_day()
                    $ school_clock.reset()
                    $ calendar.advance_to_next_day()
                    scene SleepScene1 with Dissolve(0.5)
                    MC "....."
                    scene SleepScene2 with Dissolve(0.5)
                    MC "{color=#808080}*It's morning already...*{/color}"
                    MC "{color=#808080}*I should get out of bed...*{/color}"
                    $ Location = "my room"
                    $ calendar.Hours = 0
                    $ calendar.update_sub_place_data()
                    $ Location_img = ""
                    window hide
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
                $ reset_breakfast_weekend_9am_flags_for_new_day()
                $ school_clock.reset()
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
                        Jennifer "[MC_upper], ARE YOU AWAKE?!"
                        Jennifer "GET UP ALREADY, THE BREAKFAST IS ALMOST DONE!!!"
                        Jennifer "WHAT ARE YOU DOING?!"
                        Jennifer "I'M COMING IN!!"
                        scene SleepScene5 with Dissolve(0.5)
                        Jennifer "Come on, [MC]."
                        Jennifer "I told you to stop going to bad so late!"
                        scene SleepScene6 with Dissolve(0.5)
                        Jennifer "It's really not healthy!"
                        Jennifer "Now wake up alre-"
                        scene SleepScene7 with Dissolve(0.5)
                        Jennifer "...."
                        Jennifer "{color=#808080}*What the ....*{/color}"
                        scene SleepScene8 with Dissolve(0.5)
                        Jennifer "[MC_upper], WHY ARE YOU NAKED?!?!"
                        Jennifer "YOU ARE SO GROUNDED FOR THIS!!!!"
                        scene SleepScene3 with Dissolve(0.5)
                        MC "{color=#808080}*Huhh....*{/color}"
                        MC "{color=#808080}*I think I heard mom calling me...*{/color}"
                        scene SleepScene4 with Dissolve(0.5)
                        MC "{color=#808080}*She doesn't seem to be here.*{/color}"
                        MC "{color=#808080}*But I can swear that I heard her.*{/color}"
                        MC "{color=#808080}*And the door slamming shut.*{/color}"
                        MC "{color=#808080}*In any case, I should wake up...*{/color}"
                        $ Jennifer_Corruption = Jennifer_Corruption + 2
                        $ Jennifer_Obedience = Jennifer_Obedience + 2
                        $ Jennifer_love = Jennifer_love - 2
                        "{color=#808080}**Mom love - 2**{color=#808080}"
                        "{color=#808080}**Mom corruption + 2**{color=#808080}"
                        "{color=#808080}**Mom obedience + 2**{color=#808080}"
                        $ Location = "my room"
                        $ calendar.Hours = 2
                        $ calendar.update_sub_place_data()
                        $ Location_img = ""
                        window hide
                        $ renpy.call("GameLoop")
                    "Get out of bed":
                        MC "{color=#808080}*Yea... let's start the day.*{/color}"
                        $ Location = "my room"
                        $ calendar.Hours = 0
                        $ calendar.update_sub_place_data()
                        $ Location_img = ""
                        window hide
                        $ renpy.call("GameLoop")
            "Don't sleep yet":
                $ current_location = str(Location).lower()
                $ calendar._day_advanced_flag = False
                jump GameLoop
    else:
        MC "I'm so tiered, maybe I should go to my room to get some sleep."
        $ calendar._day_advanced_flag = False
        $ renpy.call("GameLoop")
