init python:
    define_images("MC_Livingroom_Movie_8AM_Jennifer_", "MCEvents/MC_Livingroom_Movie/8AM/Jennifer", "MC_Livingroom_Movie_8AM_Jennifer_", 100)

label MC_Livingroom_Movie_8AM_Jennifer_Label:
    scene MC_Livingroom_Movie_8AM_Jennifer_1 with Dissolve(0.5)
    MC "{color=#808080}*.....*"
    scene MC_Livingroom_Movie_8AM_Jennifer_2 with Dissolve(0.5)
    Jennifer "Oh, hey kiddo, What are you doing?"
    scene MC_Livingroom_Movie_8AM_Jennifer_3 with Dissolve(0.5)
    MC "Hey mom, I'm just watching TV."
    MC "Waiting for the food to be ready."
    scene MC_Livingroom_Movie_8AM_Jennifer_4 with Dissolve(0.5)
    Jennifer "Oh, okay."
    Jennifer "I'll leave you to it then!"
    $ advance_time_or_sleep()