init python:
    define_images("MC_Livingroom_Movie_11AM_Jennifer_", "MCEvents/MC_Livingroom_Movie/11AM/Jennifer", "MC_Livingroom_Movie_11AM_Jennifer_", 100)

label MC_Livingroom_Movie_11AM_Jennifer_Label:
    scene MC_Livingroom_Movie_11AM_Jennifer_1 with Dissolve(0.5)
    MC "............"
    scene MC_Livingroom_Movie_11AM_Jennifer_2 with Dissolve(0.5)
    Jennifer "GGAAAAAAAAAAAHHHHHHH"
    Jennifer "[MC_upper]!!! WHY ARE YOU STILL WATCHING TV?!"
    scene MC_Livingroom_Movie_11AM_Jennifer_3 with Dissolve(0.5)
    Jennifer "GET DRESSED RIGHT NOW!!!"
    scene MC_Livingroom_Movie_11AM_Jennifer_4 with Dissolve(0.5)
    MC "Wait a second, mom!!"
    menu:
        "Go to school now" if beenToSchoolOnce:
            scene MC_Livingroom_Movie_11AM_Jennifer_5 with Dissolve(0.5)
            MC "Wait, it's already eleven?!"
            MC "Oh my God, sorry!!"
            scene MC_Livingroom_Movie_11AM_Jennifer_6 with Dissolve(0.5)
            Jennifer "GO GET DRESSED RIGHT NOW!!!"
            Jennifer "I WILL TAKE THIS TV AWAY FROM YOU!!!"
            scene MC_Livingroom_Movie_11AM_Jennifer_7 with Dissolve(0.5)
            $ renpy.pause(0.5)
            scene MC_Livingroom_Movie_11AM_Jennifer_8 with Dissolve(0.5)
            Jennifer "HURRY UP!!!"
            scene BlackScreen with Dissolve(0.5)
            "..."
            scene MC_Livingroom_Movie_11AM_Jennifer_9 with Dissolve(0.5)
            Jennifer "THE GIRLS ARE ALREADY IN THE CAR, WHAT ARE YOU DOING?!"
            scene MC_Livingroom_Movie_11AM_Jennifer_10 with Dissolve(0.5)
            MC "I'm here, I'm here, sorry, we can go."
            scene MC_Livingroom_Movie_11AM_Jennifer_11 with Dissolve(0.5)
            Jennifer "You better not do this again, understood?!"
            scene BlackScreen with Dissolve(0.5)
            "..."
            $ firstPosition = closer0
            $ MCclose = False
            $ isHandOnThigh = False
            $ isHandOnTits = False
            $ isHandOnMouth = False
            $ annoyed_counter = 0
            $ love_counter = 0
            $ reachButtonsActive = False
            $ hintLocationsActive = False
            $ default_mouse = "default"
            $ lastHandLocation = "thigh"
            call screen GoToSchoolFirstTimeScreen
        "Don't":
            scene MC_Livingroom_Movie_11AM_Jennifer_5 with Dissolve(0.5)
            MC "Wait, wait, mom!"
            MC "I forgot to tell you, I'm not coming with you today."
            scene MC_Livingroom_Movie_11AM_Jennifer_12 with Dissolve(0.5)
            Jennifer "Oh...."
            scene MC_Livingroom_Movie_11AM_Jennifer_13 with Dissolve(0.5)
            Jennifer "...."
            scene MC_Livingroom_Movie_11AM_Jennifer_12 with Dissolve(0.5)
            Jennifer "Well... you should have told me sooner and not make me wait for you this long!"
            scene MC_Livingroom_Movie_11AM_Jennifer_14 with Dissolve(0.5)
            MC "Sorry, mom, it won't happen again."
            scene MC_Livingroom_Movie_11AM_Jennifer_12 with Dissolve(0.5)
            Jennifer "Yeah, it better be that way!"
            $ advance_time_or_sleep()
