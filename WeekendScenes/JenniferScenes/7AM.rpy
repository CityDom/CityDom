init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)
    define_images("Jennifer_weekend_7AM_", "WeekendScenes/JenniferScenes/7AM", "Jennifer_weekend_7AM_", 100)

label Jennifer_weekend_7AM:
    scene Jennifer_weekend_7AM_1 with Dissolve(0.5)
    MC "{color=#808080}*Seems like someone is using the toilet.*{color=#808080}"
    menu:
        "Knock":
            "{color=#808080}**Knock Knock**{/color}"
            McMom "Occupied!!!"
            MC "Mom, I reaaaaaaly need to use the bathroom!"
            McMom "Go downstairs!"
            MC "It's occupied there as well!"
            McMom "Tsk... I'll be out in a minute."
            MC "But mom, it can't wait one more minute."
            McMom "I don't care, pee yourself."
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
            McMom "WHAT ARE YOU DOING!!! GET OUT!!!!!"
            MC "Sorry m..."
            McMom "GET OUT NOW!!!!!!!"
            "{color=#808080}**Mom love - 5**{color=#808080}"
            $ Mom_love = Mom_love - 5
            $ check_and_update_character_stats("Mom")
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "Leave":
            $ Location = "Hallway"
            $ renpy.call("GameLoop")

