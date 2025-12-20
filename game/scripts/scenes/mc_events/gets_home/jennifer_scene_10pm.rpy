init python:
    define_images("Jennifer_Scene_10PM_", "MCEvents/MC_GetsHome/Jennifer/10PM", "Jennifer_Scene_10PM_", 100)

label MC_GetsHome_Jennifer_10PM:
    scene Jennifer_Scene_10PM_1 with Dissolve(0.5)
    menu:
        "Knock":
            scene Jennifer_Scene_10PM_2 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_10PM_3 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_10PM_2 with Dissolve(0.5)
            "{color=#808080}*PLAP PLAP PLAP PLAP*"
            scene Jennifer_Scene_10PM_4 with Dissolve(0.5)
            MC "{color=#808080}*Ughh... I'm fucked...*"
            MC "{color=#808080}*I better take a step back...*"
            scene Jennifer_Scene_10PM_5 with Dissolve(0.5)
            "............"
            MC "Uhhh... sorry mom, I wa-"
            scene Jennifer_Scene_10PM_6 with Dissolve(0.5)
            Jennifer "Get in the house! Now!"
            scene Jennifer_Scene_10PM_7 with Dissolve(0.5)
            Jennifer "Wash you hands first then go eat!"
            Jennifer "The food must be cold by now!"
            scene Jennifer_Scene_10PM_8 with Dissolve(0.5)
            MC "Okay mom..."
            scene Jennifer_Scene_10PM_9 with Dissolve(0.5)
            Jennifer "And don't be late next time!"
            scene Jennifer_Scene_10PM_10 with Dissolve(0.5)
            Jennifer "Understood?!"
            scene Jennifer_Scene_10PM_11 with Dissolve(0.5)
            MC "Auch, yeah, I got it..."
            scene BlackScreen with Dissolve(0.5)
            $ Location = "entrance"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")
