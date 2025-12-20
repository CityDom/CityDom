label ClaireNight44:

    scene Claire_night44_1 with Dissolve(0.5)
    MC "{color=#808080}*It seems that Claire is watching a movie. Should I spend some time with her?*{/color}"
    menu:
        "Watch a movie with her":
            scene Claire_night44_2 with Dissolve(0.5)
            MC "Hey, Claire. What are you watching?"
            scene Claire_night44_3 with Dissolve(0.5)
            "....."
            scene Claire_night44_4 with Dissolve(0.5)
            MC "Uhhhh.... Claire?"
            scene Claire_night44_5 with Dissolve(0.5)
            Claire "Are you still here?"
            scene Claire_night44_6 with Dissolve(0.5)
            MC "Does that mean you don't want me to watch the movie with you?"
            scene Claire_night44_7 with Dissolve(0.5)
            Claire "....."
            scene Claire_night44_8 with Dissolve(0.5)
            MC "{color=#808080}*Tsk... bitch...*{/color}"
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**You leave the room**{/color}"
            $ Location = "Entrance"
            $ renpy.call("GameLoop")
        "Leave":
            MC "{color=#808080}*The bitch would kick me out anyway*{/color}"
            $ Location = "Entrance"
            $ renpy.call("GameLoop")