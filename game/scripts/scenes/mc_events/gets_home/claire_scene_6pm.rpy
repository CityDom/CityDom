init python:
    define_images("Claire_Scene_6PM_", "MCEvents/MC_GetsHome/Claire/6PM", "Claire_Scene_6PM_", 100)

label MC_GetsHome_Claire_6PM:
    scene Claire_Scene_6PM_4 with Dissolve(0.5)
    menu:
        "Knock":
            scene Claire_Scene_6PM_1 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_1 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_1 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_5 with Dissolve(1)
            MC "{color=#808080}*What the fuck is Isa doing?*"
            MC "{color=#808080}*She should be home by now...*"
            scene Claire_Scene_6PM_3 with Dissolve(1)
            Isabella "{color=#808080}*Myeah, no way I'm answering that...*"
            scene Claire_Scene_6PM_5 with Dissolve(1)
            MC "{color=#808080}*Well... I guess I'll be connecting with the nature for a bit...*"
            Claire "Move."
            scene Claire_Scene_6PM_6 with Dissolve(0.5)
            MC "Huh?!"
            scene Claire_Scene_6PM_7 with Dissolve(0.5)
            Claire "I said get the fuck out of my way."
            Claire "I won't repeat myself again."
            scene Claire_Scene_6PM_8 with Dissolve(0.5)
            MC "Ah, shit, Claire!"
            MC "Sorry, I didn't realize it was you!"
            scene Claire_Scene_6PM_9 with Dissolve(0.5)
            Claire "Pay more attention next time."
            scene BlackScreen with Dissolve(0.5)
            MC "...."
            $ Location = "entrance"
            $ advance_time_or_sleep()
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")