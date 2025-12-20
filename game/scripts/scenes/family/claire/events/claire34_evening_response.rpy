label ClaireEvening34:

    scene Claire_evening34_1 with Dissolve(0.5)
    MC "{color=#808080}*Claire is here!*{/color}"
    MC "{color=#808080}*Should I see how she's doing?*{/color}"
    menu:
        "Talk to her":
            MC "Hey Claire! What are you doing?"
            Claire "What do you want?"
            MC "Ummm... I want to see how you are doing?"
            Claire "Now that you are here, bad."
            Claire "Bye."
            MC "But I just wanted to ask h-"
            Claire "Just leave already loser, I'm not in the mood."
            MC "{color=#808080}*God I can't have the slightest conversation with her.*{/color}"
            "{color=#808080}*You leave the room.*{/color}"
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "Leave":
            MC "{color=#808080}*Maybe not now.*{/color}"
            $ Location = "Hallway"
            $ renpy.call("GameLoop")
