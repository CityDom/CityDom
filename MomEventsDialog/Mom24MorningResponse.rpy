label MomMorning24:

    MC "Hey mom, what's up?"
    scene MORNINGS24MOM2 with Dissolve(0.5)
    McMom "I'm making breakfast, wanna help me?"
    scene MORNINGS24MOM15 with Dissolve(0.5)
    menu:
        "Help with cooking":
            MC "Sure mom, tell me what you need."
            scene MORNINGS24MOM3 with Dissolve(0.5)
            McMom "Okay, so first you need...."
            scene BlackScreen with Dissolve(0.5)
            McMom "....."
            McMom ".........."
            McMom "................."
            "{color=#808080}**You finish making breakfast with your mom.**{/color}"
            scene MORNINGS24MOM16 with Dissolve(0.5)
            McMom "Thanks a lot, kiddo!"
            McMom "Come here, let me give you a kiss."
            scene MORNINGS24MOM5 with Dissolve(0.5)
            MC "{color=#808080}*Should I turn and kiss her?*{/color}"
            menu:
                "Turn":
                    scene MORNINGS24MOM8 with Dissolve(0.5)
                    MC "{color=#808080}*Fuck.. Her lips are so soft. I might be cumming just from this..*{/color}"
                    MC "{color=#808080}*She's gonna be so angry.*{/color}"
                    scene MORNINGS24MOM9 with Dissolve(0.5)
                    McMom "{color=#808080}*He is such a nice kid helping me with the breakfast, he earned a little kiss on the cheek.*{/color}"
                    scene MORNINGS24MOM10 with Dissolve(0.5)
                    McMom "{color=#808080}*And he is such a good kisser... Wait a second...*{/color}"
                    scene MORNINGS24MOM11 with Dissolve(0.5)
                    McMom "Whaa....."
                    scene MORNINGS24MOM12 with Dissolve(0.5)
                    McMom "[MC_upper] WHAT ARE YOU DOING?!?!?!?!"
                    MC "Sorry mom, I thought you are going for the other chick and.. and.."
                    MC "Sorry... I messed up."
                    scene MORNINGS24MOM13 with Dissolve(0.5)
                    McMom "Mistakes of that kind are not ok!!!"
                    McMom "Not between a mother and her son!!"
                    scene MORNINGS24MOM14 with Dissolve(0.5)
                    McMom "Now go to sit at the table!"
                    MC "Ok mom..."
                    MC "{color=#808080}*I hope she's not too mad..*{/color}"
                    $ Mom_love = Mom_love - 5
                    $ check_and_update_character_stats("Mom")
                    $ Location = "livingroom"
                    $ advance_time_or_sleep()
                "Stay":
                    scene MORNINGS24MOM7 with Dissolve(0.5)
                    MC "Her lips feel soo good and soft.."
                    scene MORNINGS24MOM6 with Dissolve(0.5)
                    McMom "He is such a nice kid helping me with breakfast, he earned a kiss."
                    scene MORNINGS24MOM4 with Dissolve(0.5)
                    McMom "Ok kiddo, now go sit at the table, let's eat breakfast"
                    MC "Oke mom, thanks for the kiss"
                    "{color=#808080}**Mom love + 2**{color=#808080}"
                    $ Mom_love = Mom_love + 2
                    $ check_and_update_character_stats("Mom")
                    $ Location = "livingroom"
                    $ advance_time_or_sleep()
        "Leave":
            MC "Sorry mom, I don't have time right now, maybe next time!"
            McMom "It's ok kiddo, but breakfast it's almost done, be ready by then!"
            $ Location = "livingroom"
            $ renpy.call("GameLoop")
            return