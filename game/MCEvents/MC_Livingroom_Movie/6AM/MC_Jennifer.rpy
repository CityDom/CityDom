init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)

    define_images("MC_Livingroom_Movie_Morning_Jennifer_", "MCEvents/MC_Livingroom_Movie/6AM/Jennifer", "MC_Livingroom_Movie_Morning_Jennifer_", 100)

label MC_Livingroom_Movie_Morning_Jennifer_Label:
    scene MC_Livingroom_Movie_Morning_Jennifer_1 with Dissolve(0.5)
    MC "............"
    scene MC_Livingroom_Movie_Morning_Jennifer_2 with Dissolve(0.5)
    McMom "GGAAAAAAAAAAAHHHHHHH"
    scene MC_Livingroom_Movie_Morning_Jennifer_3 with Dissolve(0.5)
    McMom "[MC_upper]!!! DON'T TELL ME YOU'VE BEEN UP ALL NIGHT WATCHING TV!!!"
    scene MC_Livingroom_Movie_Morning_Jennifer_4 with Dissolve(0.5)
    MC "Wait, wait, wait, mom!"
    MC "I just woke up! I swear!"
    scene MC_Livingroom_Movie_Morning_Jennifer_6 with Dissolve(0.5)
    McMom "Hmpf....."
    scene MC_Livingroom_Movie_Morning_Jennifer_5 with Dissolve(0.5)
    McMom "You better not lie to me, understood?"
    scene MC_Livingroom_Movie_Morning_Jennifer_7 with Dissolve(0.5)
    MC "Yeah, yeah, you just scared me!"
    scene MC_Livingroom_Movie_Morning_Jennifer_8 with Dissolve(0.5)
    McMom "Sorry, I'll leave you to it then..."
    $ advance_time_or_sleep()
