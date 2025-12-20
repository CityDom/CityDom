init python:
    define_images("Claire_Scene_8PM_", "MCEvents/MC_GetsHome/Claire/8PM", "Claire_Scene_8PM_", 100)

label MC_GetsHome_Claire_8PM:
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
            MC "{color=#808080}*C'mooon....*"
            MC "{color=#808080}*I think they are all upstairs...*"
            scene Claire_Scene_8PM_1 with Dissolve(1)
            Jennifer "KIDS!! CAN ONE OF YOU ANSWER THE DOOR? I'M CHANGING!"
            scene Claire_Scene_8PM_2 with Dissolve(1)
            MC "{color=#808080}*Huh? Someone opened it...*"
            scene Claire_Scene_8PM_3 with Dissolve(0.5)
            MC "Oh, thank you, Claire!"
            scene Claire_Scene_8PM_4 with Dissolve(0.5)
            MC "....."
            $ Location = "entrance"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")