init python:
    define_images("Claire_Scene_6AM_", "MCEvents/MC_GetsHome/Claire/6AM", "Claire_Scene_6AM_", 100)

label MC_GetsHome_Claire_6AM:
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
            "......."
            scene Jennifer_Scene_6AM_5 with Dissolve(0.5)
            MC "{color=#808080}*Is everyone still sleeping?*{color=#808080}"
            scene Jennifer_Scene_6AM_2 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_6AM_3 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_6AM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6AM_1 with Dissolve(0.5)
            "....."
            scene Claire_Scene_6AM_2 with Dissolve(0.5)
            MC "Oh, good morning, Claire!"
            MC "May I co-"
            scene Claire_Scene_6AM_3 with Dissolve(0.5)
            MC "{color=#808080}*I guess she's happy to see me...*{color=#808080}"
            $ Location = "entrance"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")