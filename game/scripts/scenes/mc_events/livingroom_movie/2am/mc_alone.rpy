init python:
    define_images("MC_Livingroom_Movie_2AM_Alone_", "MCEvents/MC_Livingroom_Movie/2AM/Alone", "MC_Livingroom_Movie_2AM_Alone_", 100)

label MC_Livingroom_Movie_2AM_Alone_Label:
    scene MC_Livingroom_Movie_2AM_Alone_1 with Dissolve(0.5)
    "{color=#808080}**One hour passes...**"
    $ advance_time_or_sleep()