label JenniferMorning24:
    scene Jennifer_morning24_1
    MC "{color=#808080}*Oh, mom is making breakfast, let's see how she's doing*{color=#808080}"
    MC "Hey mom, what's up?"
    scene Jennifer_morning24_2 with Dissolve(0.5)
    Jennifer "I'm making breakfast, wanna help me?"
    scene Jennifer_morning24_15 with Dissolve(0.5)
    menu:
        "Help with cooking":
            MC "Sure mom, tell me what you need."
            scene Jennifer_morning24_3 with Dissolve(0.5)
            Jennifer "Okay, so first you need...."
            scene BlackScreen with Dissolve(0.5)
            Jennifer "....."
            Jennifer ".........."
            Jennifer "................."
            "{color=#808080}**You finish making breakfast with your mom.**{/color}"
            scene Jennifer_morning24_16 with Dissolve(0.5)
            Jennifer "Thanks a lot, kiddo!"
            Jennifer "Come here, let me give you a kiss."
            scene Jennifer_morning24_5 with Dissolve(0.5)
            MC "{color=#808080}*Should I turn and kiss her?*{/color}"
            menu:
                "Turn":
                    scene Jennifer_morning24_8 with Dissolve(0.5)
                    MC "{color=#808080}*Fuck.. Her lips are so soft. I might be cumming just from this..*{/color}"
                    MC "{color=#808080}*She's gonna be so angry.*{/color}"
                    scene Jennifer_morning24_9 with Dissolve(0.5)
                    Jennifer "{color=#808080}*He is such a nice kid helping me with the breakfast, he earned a little kiss on the cheek.*{/color}"
                    scene Jennifer_morning24_10 with Dissolve(0.5)
                    Jennifer "{color=#808080}*And he is such a good kisser... Wait a second...*{/color}"
                    scene Jennifer_morning24_11 with Dissolve(0.5)
                    Jennifer "Whaa....."
                    scene Jennifer_morning24_12 with Dissolve(0.5)
                    Jennifer "[MC_upper] WHAT ARE YOU DOING?!?!?!?!"
                    MC "Sorry mom, I thought you are going for the other chick and.. and.."
                    MC "Sorry... I messed up."
                    scene Jennifer_morning24_13 with Dissolve(0.5)
                    Jennifer "Mistakes of that kind are not ok!!!"
                    Jennifer "Not between a mother and her son!!"
                    scene Jennifer_morning24_14 with Dissolve(0.5)
                    Jennifer "Now go to sit at the table!"
                    MC "Ok mom..."
                    MC "{color=#808080}*I hope she's not too mad..*{/color}"
                    $ Jennifer_love = Jennifer_love - 5
                    $ check_and_update_character_stats("Jennifer")
                    $ Location = "livingroom"
                    $ advance_time_or_sleep()
                "Stay":
                    scene Jennifer_morning24_7 with Dissolve(0.5)
                    MC "Her lips feel soo good and soft.."
                    scene Jennifer_morning24_6 with Dissolve(0.5)
                    Jennifer "He is such a nice kid helping me with breakfast, he earned a kiss."
                    scene Jennifer_morning24_4 with Dissolve(0.5)
                    Jennifer "Ok kiddo, now go sit at the table, let's eat breakfast"
                    MC "Oke mom, thanks for the kiss"
                    call stat_reward({"Jennifer": {"love": 2}}, show_black=False, return_to=None)
                    $ Location = "livingroom"
                    $ advance_time_or_sleep()
        "Leave":
            MC "Sorry mom, I don't have time right now, maybe next time!"
            Jennifer "It's ok kiddo, but breakfast it's almost done, be ready by then!"
            $ Location = "livingroom"
            $ renpy.call("GameLoop")
            return