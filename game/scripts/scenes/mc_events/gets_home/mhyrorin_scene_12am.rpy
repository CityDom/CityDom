init python:
    define_images("Mhyrorin_Scene_12AM_", "MCEvents/MC_GetsHome/Mhyrorin/12AM", "Mhyrorin_Scene_12AM_", 100)

label MC_GetsHome_Mhyrorin_12AM:
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
            scene Mhyrorin_Scene_12AM_5 with Dissolve(0.5)
            MC "{color=#808080}*God... it's so dark inside...*"
            scene Mhyrorin_Scene_12AM_6 with Dissolve(0.5)
            MC "{color=#808080}*Where the fuck is that light switch...*"
            MC "{color=#808080}*UGHHHH!!! I can't see shit...*"
            MC "{color=#808080}*Oh, there it is!"
            MC "{color=#808080}*EWWWW nevermind, what the fuck is that..."
            Mhyrorin "Dohn't beh mean, asshohle!"
            MC "Huh...?"
            scene Mhyrorin_Scene_12AM_7 with Dissolve(0.5)
            Mhyrorin "I'd appreciahte your fingersh outta my mouf."
            scene Mhyrorin_Scene_12AM_8 with Dissolve(0.5)
            MC "You. Scared.... The shit out of me..."
            scene Mhyrorin_Scene_12AM_7 with Dissolve(0.5)
            Mhyrorin "I'm shorry you're blind ash fuck."
            scene Mhyrorin_Scene_12AM_9 with Dissolve(0.5)
            MC "Not everyone has super powers okay?"
            scene Mhyrorin_Scene_12AM_10 with Dissolve(0.5)
            Mhyrorin "Yeah, wha'ever, did you get comfor'able in here?"
            scene Mhyrorin_Scene_12AM_11 with Dissolve(0.5)
            Mhyrorin "GUH-AGH..."
            scene Mhyrorin_Scene_12AM_12 with Dissolve(0.5)
            Mhyrorin "Yuh knoh I canh beh'the shih ou'ah yuh, righ'?"
            scene Mhyrorin_Scene_12AM_13 with Dissolve(0.5)
            MC "That's for almost causing me a heart attack."
            scene Mhyrorin_Scene_12AM_14 with Dissolve(0.5)
            MC "But god damn, don't you have a gag reflex at all?"
            scene Mhyrorin_Scene_12AM_15 with Dissolve(0.5)
            Mhyrorin "Ohf coursh noh!"
            scene Mhyrorin_Scene_12AM_17 with Dissolve(0.5)
            Mhyrorin "What kind of succubus would I be if I hadh one?"
            scene Mhyrorin_Scene_12AM_18 with Dissolve(0.5)
            Mhyrorin "But with the taste of these, I might just throw up a little..."
            scene Mhyrorin_Scene_12AM_19 with Dissolve(0.5)
            MC "Haha, you're so funny. But you took your time tasting them!"
            scene Mhyrorin_Scene_12AM_20 with Dissolve(0.5)
            Mhyrorin "Yeah... I was just checking..."
            scene Mhyrorin_Scene_12AM_21 with Dissolve(0.5)
            MC "Huh? Checking what? The taste?"
            scene Mhyrorin_Scene_12AM_22 with Dissolve(0.5)
            Mhyrorin "Uhhh, yeah, the taste..."
            scene Mhyrorin_Scene_12AM_23 with Dissolve(0.5)
            Mhyrorin "Anyway! See ya!"
            scene BlackScreen with Dissolve(0.1)
            $ renpy.pause(0.1, hard=True)
            scene Mhyrorin_Scene_12AM_24 with Dissolve(0.5)
            MC "She's so weird sometimes..."
            $ Location = "entrance"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")
