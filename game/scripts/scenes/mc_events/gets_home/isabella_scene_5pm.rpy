init python:
    define_images("Isabella_Scene_5PM_", "MCEvents/MC_GetsHome/Isabella/5PM", "Isabella_Scene_5PM_", 100)

label MC_GetsHome_Isabella_5PM:
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
            scene Isabella_Scene_5PM_1 with Dissolve(0.5)
            Isabella "God damn it, who is it this time?"
            scene Isabella_Scene_5PM_2 with Dissolve(0.5)
            "KNOCK KNOCK KNOCK!!!"
            scene Isabella_Scene_5PM_3 with Dissolve(0.5)
            Isabella "ONE SECOND!! GEEZ!!"
            scene Isabella_Scene_5PM_4 with Dissolve(0.5)
            "KNOCK KNOCK KNOCK!!!"
            scene Isabella_Scene_5PM_5 with Dissolve(0.5)
            Isabella "I swear I'm doing everything in this house..."
            scene Isabella_Scene_5PM_6 with Dissolve(0.5)
            Isabella "{color=#808080}*Nobody has a key...*"
            scene Isabella_Scene_5PM_7 with Dissolve(0.5)
            Isabella "...."
            scene Isabella_Scene_5PM_8 with Dissolve(0.5)
            Isabella "I swear to god, [MC], if you don't take that god damn key with you..."
            scene Isabella_Scene_5PM_9 with Dissolve(0.5)
            MC "I am..."
            MC "Maybe stop leaving the key in the door after you close it."
            scene Isabella_Scene_5PM_10 with Dissolve(0.5)
            Isabella "Uhhhh..."
            scene Isabella_Scene_5PM_11 with Dissolve(0.5)
            Isabella "Welcome home, big bro!!"
            scene Isabella_Scene_5PM_12 with Dissolve(0.5)
            MC "You are lucky you are cute..."
            scene Isabella_Scene_5PM_13 with Dissolve(0.5)
            Isabella "Ughhh..."
            scene Isabella_Scene_5PM_14 with Dissolve(0.5)
            Isabella "You are so petty!!"
            scene Isabella_Scene_5PM_15 with Dissolve(0.5)
            MC "Learned it from the best!"
            $ Location = "entrance"
            $ renpy.call("GameLoop")
            #! lvl 2 isa jumps on his back
        "Enter":    
            $ Location = "entrance"
            $ renpy.call("GameLoop")