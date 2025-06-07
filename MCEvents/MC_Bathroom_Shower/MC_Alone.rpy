init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)
    define_images("MC_Bathroom_Shower_Alone_", "MCEvents/MC_Bathroom_Shower/Alone", "MC_Bathroom_Shower_Alone_", 100)

label MC_Bathroom_Shower_Alone:
    scene MC_Bathroom_Shower_Alone_1 with Dissolve(0.5)
    MC "..."
    pause 3
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}**One hour passes...**"
    $ Location = "washing room"
    $ advance_time_or_sleep()