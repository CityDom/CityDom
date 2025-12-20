init python:
    define_images("Isabella_Scene_4PM_", "MCEvents/MC_GetsHome/Isabella/4PM", "Isabella_Scene_4PM_", 100)

label MC_GetsHome_Isabella_4PM:
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
            Isabella "JUST ENTER, IT'S OPEN!"
            scene Isabella_Scene_4PM_1 with Dissolve(0.5)
            MC "Oh..."
            scene Isabella_Scene_4PM_2 with Dissolve(0.5)
            MC "You already got home?"
            MC "Why didn't you tell me, we could've walked together."
            scene Isabella_Scene_4PM_3 with Dissolve(0.5)
            Isabella "Well... I thought that you were walking with Maria."
            Isabella "Aren't you with her all the time?"
            scene Isabella_Scene_4PM_4 with Dissolve(0.5)
            MC "Huh? What are you talking about? I don't even know where she lives..."
            MC "And we aren't even friends like that, I just got put in the same bench as her."
            scene Isabella_Scene_4PM_5 with Dissolve(0.5)
            Isabella "Yeah, whatever, I don't care anyway..."
            scene Isabella_Scene_4PM_6 with Dissolve(0.5)
            MC "....."
            $ Location = "entrance"
            $ advance_time_or_sleep()
        "Enter":    
            $ Location = "entrance"
            $ renpy.call("GameLoop")