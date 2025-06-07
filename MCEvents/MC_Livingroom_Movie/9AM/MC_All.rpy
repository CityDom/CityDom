init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)

    define_images("MC_Livingroom_Movie_9AM_All_", "MCEvents/MC_Livingroom_Movie/9AM/All", "MC_Livingroom_Movie_9AM_All_", 100)

label MC_Livingroom_Movie_9AM_All_Label:
    scene MC_Livingroom_Movie_9AM_All_1 with Dissolve(0.5)
    McMom "...."
    scene MC_Livingroom_Movie_9AM_All_2 with Dissolve(0.5)
    McMom "Huh...?"
    scene MC_Livingroom_Movie_9AM_All_3 with Dissolve(0.5)
    McMom "What do you think you're doing?!"
    scene MC_Livingroom_Movie_9AM_All_4 with Dissolve(0.5)
    MC "Oh, I'm not really that hungry right now, y'all can eat without me."
    MC "I'm just going to watch some TV for a bit."
    scene MC_Livingroom_Movie_9AM_All_5 with Dissolve(0.5)
    McMom "I didn't ask you if you're hungry or not."
    McMom "I made the food so you're going to eat it."
    scene MC_Livingroom_Movie_9AM_All_6 with Dissolve(0.5)
    McMom "So I'm not saying it twice, come here and sit down already!"
    scene MC_Livingroom_Movie_9AM_All_7 with Dissolve(0.5)
    MC "Okay, okay, geez, sorry..."
    jump DinnerMenuLVL1