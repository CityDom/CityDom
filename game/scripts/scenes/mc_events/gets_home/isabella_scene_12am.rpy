init python:
    define_images("Isabella_Scene_12PM_", "MCEvents/MC_GetsHome/Isabella/12PM", "Isabella_Scene_12PM_", 100)

label MC_GetsHome_Isabella_12PM:
    scene Jennifer_Scene_10PM_1 with Dissolve(0.5)
    menu:
        "Knock":
            scene Jennifer_Scene_10PM_2 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_10PM_3 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_10PM_2 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_10PM_3 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Isabella_Scene_12PM_1 with Dissolve(0.5)
            Claire "ISABELLAAAAA"
            scene Isabella_Scene_12PM_2 with Dissolve(0.5)
            Jennifer "ISABELLAAAAAAA!!!!"
            scene Isabella_Scene_12PM_3 with Dissolve(0.5)
            Isabella "IM IN THE GAME!!! I CAN'T PAUSE THEM!!!"
            scene Isabella_Scene_12PM_4 with Dissolve(0.5)
            MC "I guess I'm sleeping outside..."
            scene Isabella_Scene_12PM_5 with Dissolve(0.5)
            Mhyrorin "Heyaaaaaa"
            scene Isabella_Scene_12PM_6 with Dissolve(0.5)
            MC "......"
            scene Isabella_Scene_12PM_7 with Dissolve(0.5)
            Mhyrorin "Really? What's with that face?"
            scene Isabella_Scene_12PM_8 with Dissolve(0.5)
            Mhyrorin "You are so not fun to scare..."
            scene Isabella_Scene_12PM_9 with Dissolve(0.5)
            MC "My face cramped..."
            scene Isabella_Scene_12PM_10 with Dissolve(0.5)
            MC "I almost passed out, are you stupid?"
            MC "Stop doing this shit!"
            scene Isabella_Scene_12PM_11 with Dissolve(0.5)
            Mhyrorin "Hehe, so I did get you!"
            scene Isabella_Scene_12PM_12 with Dissolve(0.5)
            Mhyrorin "So do you plan on camping here for the rest of the night or..."
            scene Isabella_Scene_12PM_13 with Dissolve(0.5)
            MC "My wonderful family likes to stick keys in doors after they close them."
            MC "So now I'm stuck here with Gwendolyne Maxine..."
            MC "What are you doing here? Are you actually stalking me 24/7?"
            scene Isabella_Scene_12PM_14 with Dissolve(0.5)
            Mhyrorin "Nah, I was just passing by, and saw your ass mean mugging the door."
            Mhyrorin "I couldn't let my MJ sit here all sad and lonely."
            scene Isabella_Scene_12PM_15 with Dissolve(0.5)
            Mhyrorin "Heh..."
            scene Isabella_Scene_12PM_16 with Dissolve(0.5)
            Mhyrorin "So what do you say, Mary?"
            scene Isabella_Scene_12PM_17 with Dissolve(0.5)
            Mhyrorin "Why don't you give spidey a kiss for saving you?"
            scene Isabella_Scene_12PM_18 with Dissolve(0.5)
            MC "Huh? Really? What's the catch?"
            scene Isabella_Scene_12PM_19 with Dissolve(0.5)
            Mhyrorin "Huh? What catch? I just thought we could recreate the scene, it could be fun..."
            Mhyrorin "I never kissed someone upside down, but if you don't want to it's oke..."
            scene Isabella_Scene_12PM_20 with Dissolve(0.5)
            MC "I would never refuse such an offer ma'am!"
            scene Isabella_Scene_12PM_21 with Dissolve(0.5)
            Mhyrorin "Then what are you waiting for?"
            scene Isabella_Scene_12PM_22 with Dissolve(0.5)
            MC "Mmmmmmmmm"
            scene BlackScreen with Dissolve(0.5)
            MC "............"
            MC "C'mon, what are you doing?!"
            scene Isabella_Scene_12PM_23 with Dissolve(0.5)
            pause
            scene Isabella_Scene_12PM_24 with Dissolve(0.5)
            pause
            scene Isabella_Scene_12PM_25 with Dissolve(0.5)
            Isabella "I swear sometimes I think I'm the only one normal in this family..."
            scene BlackScreen with Dissolve(0.5)
            $ Location = "entrance"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")
