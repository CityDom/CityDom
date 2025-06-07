label MomEvening34:

    menu:
        "Knock":
            McMom "What do you want?"
            MC "May I come in?"
            McMom "Please wait, I'm getting dressed, I'll be out in a moment!"
            MC "{color=#808080}*I guess I'll have to do something else until then.*{/color}"
            $ Location = "Hallway"
            return        
        "Peek":
            MC "{color=#808080}*Just a quick look.*{/color}"
            scene EVENINGS34MOM1 with Dissolve(0.5)
            MC "{color=#808080}*Nice, just in time!*{/color}"
            scene EVENINGS34MOM2 with Dissolve(0.5)
            McMom "......."
            scene EVENINGS34MOM3 with Dissolve(0.5)
            MC "{color=#808080}*Huh, is she saying something?*{/color}"
            scene EVENINGS34MOM4 with Dissolve(0.5)
            McMom "Every day is the same..."
            scene EVENINGS34MOM6 with Dissolve(0.5)
            MC "{color=#808080}*Heh, this is getting interesting in every kind of way!*{/color}"
            scene EVENINGS34MOM7 with Dissolve(0.5)
            MC "{color=#808080}*And she's almost fully naked!*{/color}"
            scene EVENINGS34MOM8 with Dissolve(0.5)
            MC "{color=#808080}*Wait... I should listen to what she's saying...*{/color}"
            scene EVENINGS34MOM9 with Dissolve(0.5)
            McMom "Ever since that piece of shit left me...."
            McMom "Huh?" with Dissolve(0.5)
            MC "{color=#808080}*Fuck I think she heard me... should I leave?*"
            menu:
                "Stay":
                    # if (Mom_love > 10):
                    MC "{color=#808080}*Fuck it, all or nothing!*{/color}"
                    McMom "I must be hearing things.."
                    scene EVENINGS34MOM10 with Dissolve(0.5)
                    MC "{color=#808080}*Nice, she didn't notice me!*{/color}"
                    McMom "I'm not even surprised... ever since that asshole left me I've gone crazy..."
                    scene EVENINGS34MOM11 with Dissolve(0.5)
                    McMom "Not like he was anything special..."
                    scene EVENINGS34MOM12 with Dissolve(0.5)
                    McMom "I don't even got the time to meet someone new."
                    McMom "I gotta take care of the kids.."
                    MC "{color=#808080}*So she would like to meet someone...*{/color}"
                    MC "{color=#808080}*Interesting...*{/color}"
                    scene EVENINGS34MOM13 with Dissolve(0.5)
                    McMom "What am I saying..."
                    McMom "I gotta put myself together!"
                    scene EVENINGS34MOM14 with Dissolve(0.5)
                    MC "{color=#808080}*Damn... I never knew mom felt that way...*{/color}"
                    MC "{color=#808080}*That's perfect!!!!!!*{/color}"
                    scene EVENINGS34MOM15 with Dissolve(0.5)
                    MC "{color=#808080}*No worries mom, I'll take good care of you.*{/color}"
                    MC "{color=#808080}*I've seen what I wanted, I should leave for now!*{/color}"
                    #     if (Mom_love > 20):
                    #         scene EVENINGS34MOM19 with Dissolve(0.5)
                    #         McMom "And [MC]..."
                    #         MC "{color=#808080}*Wait what?*{/color}"
                    #         McMom "I would've never believe.."
                    #         scene EVENINGS34MOM20 with Dissolve(0.5)
                    #         MC "{color=#808080}*Oh... is she going to bitch about me aswell*{/color}"
                    #         MC "{color=#808080}*Yeah... let's leave..*{/color}"
                    #         McMom "{color=#808080}*❤️❤️❤️ I would've never believe he has such a big dick ❤️❤️❤️*{/color}"
                    #         MC "{color=#808080}*WAIT WHAT*{/color}"
                    #         scene EVENINGS34MOM21 with Dissolve(0.5)
                    #         McMom "{color=#808080}*❤️❤️❤️ It's the biggest one I've ever seen by far ❤️❤️❤️*{/color}"
                    #         MC "{color=#808080}*I knew all females were sluts with a little push... but to feel like that for her own son...*{/color}"
                    #         MC "{color=#808080}*She will be the perfect personal slut!!!!!*{/color}"
                    #         scene EVENINGS34MOM22 with Dissolve(0.5)
                    #         MC "{color=#808080}*I'm hard just thinking about it...*{/color}"
                    #         McMom "Okay... I've officially gone completely crazy!"
                    #         McMom "He is my son... I have to get rid of this thoughts!"
                    #         scene EVENINGS34MOM23 with Dissolve(0.5)
                    #         MC "{color=#808080}*You don't have to get rid of them, slut.*{/color}"
                    #         scene EVENINGS34MOM24 with Dissolve(0.5)
                    #         MC "{color=#808080}*I'll engrave those thoughts deep into you!*{/color}"
                    #         scene EVENINGS34MOM25 with Dissolve(0.5)
                    #         McMom "Anyway... I should go prepare dinner."
                    #         scene EVENINGS34MOM26 with Dissolve(0.5)
                    #         MC "Okay, she's done dressing, time to go!"
                    #         "You close the door as slowly as you can and leave."
                    #         $ Mom_Corruption = Mom_Corruption + 2
                    #         $ advance_time_or_sleep()
                    #         $ Location = "Hallway"
                    #     else:
                    #         "You close the door as slowly as you can and leave."
                    #         $ Mom_Corruption = Mom_Corruption + 2
                    #         $ advance_time_or_sleep()
                    #         $ Location = "Hallway"
                    # else:
                    scene EVENINGS34MOM16 with Dissolve(0.5)
                    McMom "Huh..."
                    scene EVENINGS34MOM17 with Dissolve(0.5)
                    McMom "AAAAAAAHH!!!!!!!!"
                    scene EVENINGS34MOM18 with Dissolve(0.5)
                    MC "{color=#808080}*fuck...*{/color}"
                    McMom "[MC_upper], WHAT ARE YOU DOING?!?!?!"
                    MC "Sorry, mom, I was just...."
                    McMom "I DON'T WANT TO HEAR A THING!!!!"
                    McMom "LEAVE!!!!!!!!!"
                    "{color=#808080}**Mom love - 5**{color=#808080}"
                    "{color=#808080}**Mom corruption - 5**{color=#808080}"
                    $ Mom_Corruption = Mom_Corruption - 5
                    $ Mom_love = Mom_love - 5
                    $ check_and_update_character_stats("Mom")
                    $ Location = "Hallway" 
                    $ advance_time_or_sleep()
                "Leave":
                    "You close the door as slowly as you can and leave."
                    $ Mom_Corruption = Mom_Corruption + 2
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
        "Open":
            scene EVENINGS34MOM16 with Dissolve(0.5)
            McMom "Huh..."
            scene EVENINGS34MOM17 with Dissolve(0.5)
            McMom "AAAAAAAHH!!!!!!!!"
            scene EVENINGS34MOM18 with Dissolve(0.5)
            MC "{color=#808080}*fuck...*{/color}"
            McMom "[MC_upper], WHAT ARE YOU DOING!!!!!!"
            MC "Sorry mom I was just...."
            McMom "I DON'T WANT TO HEAR A THING!!!!"
            McMom "LEAVE!!!!!!!!!"
            "{color=#808080}**Mom love - 5**{color=#808080}"
            "{color=#808080}**Mom corruption - 5**{color=#808080}"
            $ Mom_Corruption = Mom_Corruption - 5
            $ Mom_love = Mom_love - 5 
            $ check_and_update_character_stats("Mom")
            $ Location = "Hallway" 
            $ advance_time_or_sleep()
        "Leave":
            MC "{color=#808080}*Maybe some other time.*{/color}"
            $ Location = "Hallway"
    
