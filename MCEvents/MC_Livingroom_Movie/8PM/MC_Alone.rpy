init python:
    define_images("MC_Livingroom_Movie_8PM_MC_Alone_", "MCEvents/MC_Livingroom_Movie/8PM", "MC_Livingroom_Movie_8PM_MC_Alone_", 100)

label MC_Livingroom_Movie_8PM_MC_Alone_Label:
    scene MC_Livingroom_Movie_8PM_MC_Alone_1 with Dissolve(0.5)
    "{color=#808080}**One hour passes...**"
    $ advance_time_or_sleep()