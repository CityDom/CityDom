init python:
    define_images("Isabella_Scene_6AM_", "MCEvents/MC_GetsHome/Isabella/6AM", "Isabella_Scene_6AM_", 100)

label MC_GetsHome_Isabella_6AM:
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
            Isabella "Mom!! Someone is knocking at the door!!"
            "....."
            Isabella "MOOOOM!!!"
            "....."
            Isabella "GOD DAMN IT!"
            Jennifer "ISABELLA! WATCH YOUR MOUTH!"
            Isabella "OH, NOW YOU HEAR!"
            scene Isabella_Scene_6AM_1 with Dissolve(0.5)
            Isabella "What do you want? You know it's 6 AM, right?"
            scene Isabella_Scene_6AM_2 with Dissolve(0.5)
            Isabella "Huh? [MC]? What are you doing outside at this hour?"
            scene Isabella_Scene_6AM_3 with Dissolve(0.5)
            MC "I'm selling cocaine on the corner!"
            MC "Why do I need to give you explanations on what I'm doing?"
            scene Isabella_Scene_6AM_4 with Dissolve(0.5)
            Isabella "Oh, really?"
            scene Isabella_Scene_6AM_5 with Dissolve(0.5)
            Isabella "You kinda look like the type to do it, to be honest..."
            scene Isabella_Scene_6AM_6 with Dissolve(0.5)
            MC "Just move your ass already so I can get inside..."
            scene Isabella_Scene_6AM_7 with Dissolve(0.5)
            Isabella "Damn... so moody in the morning!"
            Isabella "I thought I was supposed to be the drama queen in this house!"
            scene Isabella_Scene_6AM_8 with Dissolve(0.5)
            MC "Move or I'm beating your ass, Isa..."
            scene Isabella_Scene_6AM_9 with Dissolve(0.5)
            Isabella "Alright, geez..."
            $ Location = "entrance"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")