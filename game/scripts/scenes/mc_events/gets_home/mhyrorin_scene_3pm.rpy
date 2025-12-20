init python:
    define_images("Mhyrorin_Scene_3PM_", "MCEvents/MC_GetsHome/Mhyrorin/3PM", "Mhyrorin_Scene_3PM_", 100)

label MC_GetsHome_Mhyrorin_3PM:
    scene Jennifer_Scene_6AM_1 with Dissolve(0.5)
    menu:
        "Knock":
            scene Mhyrorin_Scene_12AM_1 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Mhyrorin_Scene_12AM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Mhyrorin_Scene_12AM_1 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Mhyrorin_Scene_12AM_2 with Dissolve(0.2)
            $ renpy.pause(0.5, hard=True)
            scene Mhyrorin_Scene_12AM_3 with Dissolve(0.5)
            MC "....."
            scene Mhyrorin_Scene_12AM_4 with Dissolve(0.5)
            MC "{color=#808080}*Oh, right... nobody is home...*"
            scene Mhyrorin_Scene_1PM_1 with Dissolve(0.5)
            MC "{color=#808080}*What the...*"
            MC "{color=#808080}*Oh wait... is she here again...*"
            scene Mhyrorin_Scene_3PM_1 with Dissolve(0.5)
            Mhyrorin "Ohh, hey sweetie... you're home early."
            Mhyrorin "Mommy was a bit... uhhh"
            scene Mhyrorin_Scene_3PM_2 with Dissolve(0.5)
            Mhyrorin "Occupied right now..."
            scene Mhyrorin_Scene_3PM_3 with Dissolve(0.5)
            MC "Huh?"
            scene Mhyrorin_Scene_3PM_4 with Dissolve(0.5)
            Mhyrorin "HMMMMMMMMM!!!"
            scene Mhyrorin_Scene_3PM_5 with Dissolve(0.5)
            MC "Ughhh... yes mommy, my tummy hurt so I came home early..."
            scene Mhyrorin_Scene_3PM_6 with Dissolve(0.5)
            Mhyrorin "Awwwwww, poor boy, come here!"
            scene Mhyrorin_Scene_3PM_7 with Dissolve(0.5)
            Mhyrorin "Mommy will take good care of you."
            scene Mhyrorin_Scene_3PM_8 with Dissolve(0.5)
            MC "Here I co-"
            scene Mhyrorin_Scene_3PM_9 with Dissolve(0.5)
            MC "Huh...?"
            scene Mhyrorin_Scene_3PM_10 with Dissolve(0.5)
            "......................................."
            scene Mhyrorin_Scene_3PM_11 with Dissolve(0.5)
            Mhyrorin "....."
            scene Mhyrorin_Scene_3PM_12 with Dissolve(0.5)
            MC "........"
            scene Mhyrorin_Scene_3PM_13 with Dissolve(0.5)
            MC "If you don't close the door right now you'll find me hanging by the tree outside."
            scene Mhyrorin_Scene_3PM_14 with Dissolve(0.5)
            Mhyrorin "Now, now, sweetie, no need to talk like that."
            Mhyrorin "I will make the tummy ache away in a second!"
            scene Mhyrorin_Scene_3PM_15 with Dissolve(0.5)
            MC "Yeah... Maybe I just need some milk..."
            scene Mhyrorin_Scene_3PM_16 with Dissolve(0.5)
            Mhyrorin "Touch mommy's tits again and I'll knock your teeth out."
            scene Mhyrorin_Scene_3PM_17 with Dissolve(0.5)
            MC "Damn... so aggressive, bad day at work?"
            scene Mhyrorin_Scene_3PM_18 with Dissolve(0.5)
            Mhyrorin "Maybe someone just needs a little discipline."
            scene Mhyrorin_Scene_3PM_19 with Dissolve(0.5)
            MC "Uhhh... sure, no butt stuff, besides that, I'm all yours."
            scene BlackScreen with Dissolve(0.5)
            $ Location = "entrance"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")
