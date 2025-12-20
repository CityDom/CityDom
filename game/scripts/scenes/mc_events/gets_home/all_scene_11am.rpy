init python:
    define_images("All_Scene_11AM_", "MCEvents/MC_GetsHome/All/11AM", "All_Scene_11AM_", 100)

label MC_GetsHome_All_11AM:
    scene Jennifer_Scene_6AM_1 with Dissolve(0.5)
    menu:
        "Knock":
            scene All_Scene_11AM_8 with Dissolve(0.2)
            MC "{color=#808080}*Ughhh, what are they doing? I am early one time and now they are late...*"
            scene All_Scene_11AM_1 with Dissolve(0.5)
            Claire "How much longer do you want us to wait, mom?!"
            Claire "Do you even know if he finished dressing up?!"
            scene All_Scene_11AM_2 with Dissolve(0.5)
            Jennifer "He should be here any moment now, Claire..."
            Jennifer "Have a little patience, please..."
            scene All_Scene_11AM_3 with Dissolve(0.5)
            "{color=#808080}*Knock, knock, knock!!!*"
            scene All_Scene_11AM_4 with Dissolve(0.5)
            Jennifer "Huh? Who can it be right now?"
            scene All_Scene_11AM_5 with Dissolve(0.5)
            Jennifer "YEAH, WHO IS IT?"
            scene All_Scene_11AM_9 with Dissolve(0.5)
            MC "Uhhh... Are you girls ready? I don't wanna pressure you or anything, but we're going to be late..."
            scene All_Scene_11AM_10 with Dissolve(0.5)
            Claire "You are all an embarrassment..."
            scene All_Scene_11AM_11 with Dissolve(0.5)
            Claire "Move!"
            scene All_Scene_11AM_12 with Dissolve(0.5)
            MC "Uhhh... did I do something wrong?"
            scene All_Scene_11AM_13 with Dissolve(0.5)
            Jennifer "No, honey..."
            scene All_Scene_11AM_14 with Dissolve(0.5)
            Jennifer "I will go get the car..."
            scene All_Scene_11AM_15 with Dissolve(0.5)
            MC "Are y'all matching periods or why is everyone acting weird? I didn't even hear you fight or something..."
            scene All_Scene_11AM_16 with Dissolve(0.5)
            Isabella "Nah, just Claire being a crybaby like usual."
            scene All_Scene_11AM_17 with Dissolve(0.5)
            Isabella "But it's annoying that mom gets sad about it. It pisses me off..."
            scene All_Scene_11AM_18 with Dissolve(0.5)
            Isabella "Can't you do anything about it?"
            scene All_Scene_11AM_19 with Dissolve(0.5)
            MC "Hmmm..."
            scene All_Scene_11AM_20 with Dissolve(0.5)
            MC "Well... I don't really wanna get involved with her crazy ass..."
            MC "But I guess it's all for mom..."
            MC "Plus..."
            scene All_Scene_11AM_21 with Dissolve(0.5)
            MC "I can't really refuse a request from my little sister, can I?"
            scene All_Scene_11AM_22 with Dissolve(0.5)
            Isabella "Hehe, the cute face always works!"
            scene All_Scene_11AM_23 with Dissolve(0.5)
            MC "But you'll have to help me with it."
            scene All_Scene_11AM_24 with Dissolve(0.5)
            Isabella "Sure, just tell me when you come up with something"
            scene All_Scene_11AM_25 with Dissolve(0.5)
            Isabella "But for now let's get in the car... Claire is going to throw another fit..."
            scene BlackScreen with Dissolve(0.5)
            "........."
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
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")