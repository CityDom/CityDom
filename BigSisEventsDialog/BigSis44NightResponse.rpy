label BigSisNight44:

    scene NIGHT44BIGSIS1 with Dissolve(0.5)
    MC "{color=#808080}*It seems that Claire is watching a movie. Should I spend some time with her?*{/color}"
    menu:
        "Watch a movie with her":
            scene NIGHT44BIGSIS2 with Dissolve(0.5)
            MC "Hey, Claire. What are you watching?"
            scene NIGHT44BIGSIS3 with Dissolve(0.5)
            "....."
            scene NIGHT44BIGSIS4 with Dissolve(0.5)
            MC "Uhhhh.... Claire?"
            scene NIGHT44BIGSIS5 with Dissolve(0.5)
            Clair "Are you still here?"
            scene NIGHT44BIGSIS6 with Dissolve(0.5)
            MC "Does that mean you don't want me to watch the movie with you?"
            scene NIGHT44BIGSIS7 with Dissolve(0.5)
            Clair "....."
            scene NIGHT44BIGSIS8 with Dissolve(0.5)
            MC "{color=#808080}*Tsk... bitch...*{/color}"
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**You leave the room**{/color}"
            $ Location = "Entrance"
            $ renpy.call("GameLoop")
        "Leave":
            MC "{color=#808080}*The bitch would kick me out anyway*{/color}"
            $ Location = "Entrance"
            $ renpy.call("GameLoop")