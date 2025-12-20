init python:
    define_images("Jennifer_Scene_9AM_", "MCEvents/MC_GetsHome/Jennifer/9AM", "Jennifer_Scene_9AM_", 100)

label MC_GetsHome_Jennifer_9AM:
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
            Jennifer "This better be [MC]! He is already late!"
            scene Jennifer_Scene_9AM_1 with Dissolve(0.5)
            MC "{color=#808080}*Aahhh... fuck... i forgot about breakfast...*{color=#808080}"
            scene Jennifer_Scene_9AM_2 with Dissolve(0.5)
            MC "{color=#808080}*I better get away and come later, mom is going to kill me...*{color=#808080}"
            scene Jennifer_Scene_9AM_3 with Dissolve(0.5)
            Jennifer "And where exactly do you think you're going?!"
            scene Jennifer_Scene_9AM_4 with Dissolve(0.5)
            MC "Oh, hey mom, I was ju-"
            scene Jennifer_Scene_9AM_5 with Dissolve(0.5)
            Jennifer "Get in here, mister!"
            scene Jennifer_Scene_9AM_6 with Dissolve(0.5)
            MC "Au, au, au, okay, okay!"
            scene Jennifer_Scene_9AM_7 with Dissolve(0.5)
            Jennifer "Go wash your hands, fast, food is already getting cold!"
            $ Location = "entrance"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")