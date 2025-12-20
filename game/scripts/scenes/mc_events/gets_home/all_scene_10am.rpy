init python:
    define_images("All_Scene_10AM_", "MCEvents/MC_GetsHome/All/10AM", "All_Scene_10AM_", 100)

label MC_GetsHome_All_10AM:
    scene Jennifer_Scene_6AM_1 with Dissolve(0.5)
    menu:
        "Knock":
            scene Jennifer_Scene_6AM_2 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_6AM_3 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_6AM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_6AM_3 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_6AM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_6AM_3 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_6AM_4 with Dissolve(0.5)
            MC "{color=#808080}*Why is nobody answering... they should all be home...*{color=#808080}"
            scene All_Scene_10AM_1 with Dissolve(0.5)
            Jennifer "GIRLS! CAN YOU PLEASE CHECK ON THE DOOR? I'M CHANGING!"
            scene All_Scene_10AM_2 with Dissolve(0.5)
            Isabella "I'M CHANGING AS WELL! TELL CLAIRE!"
            scene All_Scene_10AM_3 with Dissolve(0.5)
            Claire "YEAH, GOOD LUCK WITH THAT, I'M BUTT ASS NAKED TOO!"
            scene All_Scene_10AM_4 with Dissolve(0.5)
            Jennifer "LANGUAGE, CLAIRE!"
            scene All_Scene_10AM_5 with Dissolve(0.5)
            Isabella "[MC_upper]!!!, GO CHECK THE DOOR!!"
            scene All_Scene_10AM_3 with Dissolve(0.5)
            Claire "HE IS AT THE DOOR, MOST LIKELY..."
            scene All_Scene_10AM_6 with Dissolve(0.5)
            Isabella "THEN HE CAN WAIT!"
            scene Jennifer_Scene_6AM_4 with Dissolve(0.5)
            MC "{color=#808080}*...*{color=#808080}"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")