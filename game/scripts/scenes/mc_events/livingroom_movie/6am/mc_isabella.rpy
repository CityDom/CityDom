init python:
    define_images("MC_Livingroom_Movie_Morning_Isabella_", "MCEvents/MC_Livingroom_Movie/6AM/Isabella", "MC_Livingroom_Movie_Morning_Isabella_", 100)

label MC_Livingroom_Movie_Morning_Isabella_Label:
    scene MC_Livingroom_Movie_Morning_Isabella_1 with Dissolve(0.5)
    "......"
    scene MC_Livingroom_Movie_Morning_Isabella_2 with Dissolve(0.5)
    Isabella "YAAAAAAAAWN!!"
    scene MC_Livingroom_Movie_Morning_Isabella_3 with Dissolve(0.5)
    Isabella "Why are you up so early?"
    Isabella "Did you not sleep at all?"
    scene MC_Livingroom_Movie_Morning_Isabella_4 with Dissolve(0.5)
    MC "I did, I just woke up early..."
    scene MC_Livingroom_Movie_Morning_Isabella_5 with Dissolve(0.5)
    MC "How are you up so early?"
    scene MC_Livingroom_Movie_Morning_Isabella_6 with Dissolve(0.5)
    Isabella "I forgot to fill my water bottle before going to sleep..."
    scene MC_Livingroom_Movie_Morning_Isabella_7 with Dissolve(0.5)
    "......."
    $ advance_time_or_sleep()