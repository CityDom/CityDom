label JenniferEvening34:

    menu:
        "Knock":
            Jennifer "What do you want?"
            MC "May I come in?"
            Jennifer "Please wait, I'm getting dressed, I'll be out in a moment!"
            MC "{color=#808080}*I guess I'll have to do something else until then.*{/color}"
            $ Location = "Hallway"
            return        
        "Peek":
            MC "{color=#808080}*Just a quick look.*{/color}"
            scene Jennifer_evening34_1 with Dissolve(0.5)
            MC "{color=#808080}*Nice, just in time!*{/color}"
            scene Jennifer_evening34_2 with Dissolve(0.5)
            Jennifer "......."
            scene Jennifer_evening34_3 with Dissolve(0.5)
            MC "{color=#808080}*Huh, is she saying something?*{/color}"
            scene Jennifer_evening34_4 with Dissolve(0.5)
            Jennifer "Every day is the same..."
            scene Jennifer_evening34_6 with Dissolve(0.5)
            MC "{color=#808080}*Heh, this is getting interesting in every kind of way!*{/color}"
            scene Jennifer_evening34_7 with Dissolve(0.5)
            MC "{color=#808080}*And she's almost fully naked!*{/color}"
            scene Jennifer_evening34_8 with Dissolve(0.5)
            MC "{color=#808080}*Wait... I should listen to what she's saying...*{/color}"
            scene Jennifer_evening34_9 with Dissolve(0.5)
            Jennifer "Ever since that piece of shit left me...."
            Jennifer "Huh?" with Dissolve(0.5)
            MC "{color=#808080}*Fuck I think she heard me... should I leave?*"
            menu:
                "Stay":
                    # if (Jennifer_love > 10):
                    MC "{color=#808080}*Fuck it, all or nothing!*{/color}"
                    Jennifer "I must be hearing things.."
                    scene Jennifer_evening34_10 with Dissolve(0.5)
                    MC "{color=#808080}*Nice, she didn't notice me!*{/color}"
                    Jennifer "I'm not even surprised... ever since that asshole left me I've gone crazy..."
                    scene Jennifer_evening34_11 with Dissolve(0.5)
                    Jennifer "Not like he was anything special..."
                    scene Jennifer_evening34_12 with Dissolve(0.5)
                    Jennifer "I don't even got the time to meet someone new."
                    Jennifer "I gotta take care of the kids.."
                    MC "{color=#808080}*So she would like to meet someone...*{/color}"
                    MC "{color=#808080}*Interesting...*{/color}"
                    scene Jennifer_evening34_13 with Dissolve(0.5)
                    Jennifer "What am I saying..."
                    Jennifer "I gotta put myself together!"
                    scene Jennifer_evening34_14 with Dissolve(0.5)
                    MC "{color=#808080}*Damn... I never knew mom felt that way...*{/color}"
                    MC "{color=#808080}*That's perfect!!!!!!*{/color}"
                    scene Jennifer_evening34_15 with Dissolve(0.5)
                    MC "{color=#808080}*No worries mom, I'll take good care of you.*{/color}"
                    MC "{color=#808080}*I've seen what I wanted, I should leave for now!*{/color}"
                    scene Jennifer_evening34_16 with Dissolve(0.5)
                    Jennifer "Huh..."
                    scene Jennifer_evening34_17 with Dissolve(0.5)
                    Jennifer "AAAAAAAHH!!!!!!!!"
                    scene Jennifer_evening34_18 with Dissolve(0.5)
                    MC "{color=#808080}*fuck...*{/color}"
                    Jennifer "[MC_upper], WHAT ARE YOU DOING?!?!?!"
                    MC "Sorry, mom, I was just...."
                    Jennifer "I DON'T WANT TO HEAR A THING!!!!"
                    Jennifer "LEAVE!!!!!!!!!"
                    call stat_reward({"Jennifer": {"love": -5, "corruption": -5}}, show_black=False, return_to=None)
                    $ Location = "Hallway" 
                    $ advance_time_or_sleep()
                "Leave":
                    "You close the door as slowly as you can and leave."
                    call stat_reward({"Jennifer": {"corruption": 2}}, show_black=False, return_to=None)
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
        "Open":
            scene Jennifer_evening34_16 with Dissolve(0.5)
            Jennifer "Huh..."
            scene Jennifer_evening34_17 with Dissolve(0.5)
            Jennifer "AAAAAAAHH!!!!!!!!"
            scene Jennifer_evening34_18 with Dissolve(0.5)
            MC "{color=#808080}*fuck...*{/color}"
            Jennifer "[MC_upper], WHAT ARE YOU DOING!!!!!!"
            MC "Sorry mom I was just...."
            Jennifer "I DON'T WANT TO HEAR A THING!!!!"
            Jennifer "LEAVE!!!!!!!!!"
            call stat_reward({"Jennifer": {"love": -5, "corruption": -5}}, show_black=False, return_to=None)
            $ Location = "Hallway" 
            $ advance_time_or_sleep()
        "Leave":
            MC "{color=#808080}*Maybe some other time.*{/color}"
            $ Location = "Hallway"
            $ renpy.call("GameLoop")
    
