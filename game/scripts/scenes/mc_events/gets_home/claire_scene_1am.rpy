init python:
    define_images("Claire_Scene_1AM_", "MCEvents/MC_GetsHome/Claire/1AM", "Claire_Scene_1AM_", 100)

label MC_GetsHome_Claire_1AM:
    scene Jennifer_Scene_10PM_1 with Dissolve(0.5)
    menu:
        "Knock":
            scene Jennifer_Scene_10PM_2 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_10PM_3 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_10PM_2 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_10PM_3 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_1AM_1 with Dissolve(0.5)
            Claire "Tsk..."
            scene Claire_Scene_1AM_2 with Dissolve(0.5)
            $ renpy.pause(0.5, hard=True)
            scene BlackScreen with Dissolve(0.5)
            $ renpy.pause(0.5, hard=True)
            scene Claire_Scene_1AM_3 with Dissolve(0.5)
            $ renpy.pause(0.5, hard=True)
            scene BlackScreen with Dissolve(0.5)
            $ renpy.pause(0.5, hard=True)
            scene Claire_Scene_1AM_4 with Dissolve(0.5)
            $ renpy.pause(0.5, hard=True)
            scene BlackScreen with Dissolve(0.5)
            $ renpy.pause(0.5, hard=True)
            scene Claire_Scene_1AM_5 with Dissolve(0.5)
            $ renpy.pause(0.5, hard=True)
            scene BlackScreen with Dissolve(0.5)
            MC "......"
            $ Location = "entrance"
            $ advance_time_or_sleep()
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")