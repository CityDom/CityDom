init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)

    define_images("MC_Livingroom_Movie_Morning_Alone_", "MCEvents/MC_Livingroom_Movie/6AM/Alone", "MC_Livingroom_Movie_Morning_Alone_", 100)

label MC_Livingroom_Movie_Morning_Alone_Label:
    scene MC_Livingroom_Movie_Morning_Alone_1 with Dissolve(1)
    "{color=#808080}**One hour passes...**"
    $ advance_time_or_sleep()