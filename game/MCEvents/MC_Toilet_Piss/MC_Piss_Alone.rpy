init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)
    define_images("MC_Toilet_Alone_Piss_", "MCEvents/MC_Toilet_Piss/Alone", "MC_Toilet_Alone_Piss_", 100)

label MC_Toilet_Piss_Alone:
    scene MC_Toilet_Alone_Piss_1 with Dissolve(0.5)
    MC "..."
    scene MC_Toilet_Alone_Piss_2 with Dissolve(0.5)
    pause 3
    scene MC_Toilet_Alone_Piss_1 with Dissolve(0.5)
    "{color=#808080}**One hour passes...**"
    $ Location = "Hallway" 
    $ advance_time_or_sleep()