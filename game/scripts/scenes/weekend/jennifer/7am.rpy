init python:
    define_images("Jennifer_weekend_7AM_", "WeekendScenes/JenniferScenes/7AM", "Jennifer_weekend_7AM_", 100)

label Jennifer_weekend_7AM:
    scene Jennifer_weekend_7AM_1 with Dissolve(0.5)
    MC "{color=#808080}*Seems like someone is using the toilet.*{color=#808080}"
    menu:
        "Knock":
            "{color=#808080}**Knock Knock**{/color}"
            Jennifer "Occupied!!!"
            MC "Mom, I reaaaaaaly need to use the bathroom!"
            Jennifer "Go downstairs!"
            MC "It's occupied there as well!"
            Jennifer "Tsk... I'll be out in a minute."
            MC "But mom, it can't wait one more minute."
            Jennifer "I don't care, pee yourself."
            MC "{color=#808080}*Tsk... I guess I'll have to wait...*{/color}" 
            jump Jennifer_weekend_7AM
        "Peep":
            scene Jennifer_weekend_7AM_2 with Dissolve(0.5)
            MC "{color=#808080}*God damn...*{/color}"
            MC "{color=#808080}*She is so fucking hot!*{/color}"
            MC "{color=#808080}*I would pull out and jerk it right now but someone might see me in the hallway.*{/color}"
            MC "{color=#808080}*Let's leave...*{/color}"
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "Open":
            scene Jennifer_weekend_7AM_3 with Dissolve(0.5)
            Jennifer "WHAT ARE YOU DOING!!! GET OUT!!!!!"
            MC "Sorry m..."
            Jennifer "GET OUT NOW!!!!!!!"
            "{color=#808080}**Mom love - 5**{color=#808080}"
            $ Jennifer_love = Jennifer_love - 5
            $ check_and_update_character_stats("Jennifer")
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "Leave":
            $ Location = "Hallway"
            $ renpy.call("GameLoop")

