init python:
    define_images("MC_Livingroom_Movie_10PM_All_", "MCEvents/MC_Livingroom_Movie/10PM/All", "MC_Livingroom_Movie_10PM_All_", 100)

label MC_Livingroom_Movie_10PM_All_Label:
    scene MC_Livingroom_Movie_10PM_All_1 with Dissolve(0.5)
    Jennifer "Where do you think you're going, kiddo?"
    Jennifer "Food is getting cold."  
    scene MC_Livingroom_Movie_10PM_All_2 with Dissolve(0.5)
    MC "Oh, it's okay, I'm not that hungry right now."
    MC "I'll eat later."
    scene MC_Livingroom_Movie_10PM_All_3 with Dissolve(0.5)
    Jennifer "..."
    scene MC_Livingroom_Movie_10PM_All_4 with Dissolve(0.5)
    MC "Okay, I'm coming..."
    jump JumpFromLivingroomEvent10PM