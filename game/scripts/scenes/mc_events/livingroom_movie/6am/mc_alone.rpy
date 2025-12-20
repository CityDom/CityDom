init python:
    define_images("MC_Livingroom_Movie_Morning_Alone_", "MCEvents/MC_Livingroom_Movie/6AM/Alone", "MC_Livingroom_Movie_Morning_Alone_", 100)

label MC_Livingroom_Movie_Morning_Alone_Label:
    scene MC_Livingroom_Movie_Morning_Alone_1 with Dissolve(1)
    "{color=#808080}**One hour passes...**"
    $ advance_time_or_sleep()