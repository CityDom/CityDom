init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)
    define_images("Claire_weekend_6AM_", "WeekendScenes/ClaireScenes/6AM", "Claire_weekend_6AM_", 100)

label Claire_weekend_6AM:
    scene Claire_weekend_6AM_1 with Dissolve(0.5)
    MC "Hey, Claire! Good morning!"
    scene Claire_weekend_6AM_2 with Dissolve(0.5)
    Clair "Ugh, why do I have to hear his dumbass voice first thing in the morning."
    Clair "Get lost already!"
    scene Claire_weekend_6AM_3 with Dissolve(0.5)
    MC "{color=#808080}*Tsk... bitch...*"
    scene BlackScreen with Dissolve(0.5)
    $ Location = "Hallway"
    $ advance_time_or_sleep()