init python:
    define_images("Jennifer_Scene_6AM_", "MCEvents/MC_GetsHome/Jennifer/6AM", "Jennifer_Scene_6AM_", 100)

label MC_GetsHome_Jennifer_6AM:
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
            Jennifer "I'm coming, I'm coming, wait a second!"
            scene Jennifer_Scene_6AM_5 with Dissolve(0.5)
            MC "{color=#808080}*That sounded like mom, I think she just woke up...*{color=#808080}"
            scene Jennifer_Scene_6AM_6 with Dissolve(0.5)
            Jennifer "Yes, is there a problem?"
            scene Jennifer_Scene_6AM_7 with Dissolve(0.5)
            Jennifer "Huh...?"
            scene Jennifer_Scene_6AM_8 with Dissolve(0.5)
            Jennifer "[MC], what are you doing outside?!"
            scene Jennifer_Scene_6AM_9 with Dissolve(0.5)
            Jennifer "Ughhh, don't tell me you were out all night and you just got home!"
            scene Jennifer_Scene_6AM_10 with Dissolve(0.5)
            MC "No, mom, I just woke up early and took a stroll outside..."
            scene Jennifer_Scene_6AM_11 with Dissolve(0.5)
            Jennifer "Oufff, [MC], don't lie to me!"
            Jennifer "I hope you didn't got involved into some bad friend groups!"
            scene Jennifer_Scene_6AM_12 with Dissolve(0.5)
            MC "Ughh, no, mom, I don't even got any friends yet!"
            MC "Can I get in the house already?"
            scene Jennifer_Scene_6AM_13 with Dissolve(0.5)
            Jennifer "Alright, get in, but you better be telling me the truth!"
            scene Jennifer_Scene_6AM_14 with Dissolve(0.5)
            MC "Yeah, yeah..."
            $ Location = "entrance"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")