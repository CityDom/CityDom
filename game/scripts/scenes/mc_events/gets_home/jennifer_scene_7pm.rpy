init python:
    define_images("Jennifer_Scene_7PM_", "MCEvents/MC_GetsHome/Jennifer/7PM", "Jennifer_Scene_7PM_", 100)

label MC_GetsHome_Jennifer_7PM:
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
            scene Jennifer_Scene_7PM_1 with Dissolve(1)
            Isabella "....."
            scene Jennifer_Scene_7PM_2 with Dissolve(1)
            Claire "....."
            scene Jennifer_Scene_7PM_3 with Dissolve(1)
            MC "{color=#808080}*I guess I'm waiting for mom to get home...*"
            scene BlackScreen with Dissolve(1)
            "{color=#808080}**20 minutes later...**"
            scene Jennifer_Scene_7PM_4 with Dissolve(0.5)
            $ renpy.pause(0.4, hard=True)
            scene Jennifer_Scene_7PM_5 with Dissolve(0.5)
            $ renpy.pause(0.4, hard=True)
            scene Jennifer_Scene_7PM_4 with Dissolve(0.5)
            $ renpy.pause(0.4, hard=True)
            scene Jennifer_Scene_7PM_5 with Dissolve(0.5)
            $ renpy.pause(0.4, hard=True)
            scene Jennifer_Scene_7PM_4 with Dissolve(0.5)
            $ renpy.pause(0.4, hard=True)
            scene Jennifer_Scene_7PM_5 with Dissolve(0.5)
            $ renpy.pause(0.4, hard=True)
            scene Jennifer_Scene_7PM_6 with Dissolve(0.5)
            MC "C'mooooon"
            scene BlackScreen with Dissolve(1)
            "{color=#808080}**10 minutes later...**"
            scene Jennifer_Scene_7PM_7 with Dissolve(0.5)
            Jennifer "Huh? Is that..."
            scene Jennifer_Scene_7PM_8 with Dissolve(0.5)
            Jennifer "Oh my... [MC]!?"
            scene Jennifer_Scene_7PM_9 with Dissolve(0.5)
            MC "Ugh, finally..."
            scene Jennifer_Scene_7PM_10 with Dissolve(0.5)
            Jennifer "Oh, c'mon, [MC], what are you doing there?"
            Jennifer "Get up!"
            scene Jennifer_Scene_7PM_11 with Dissolve(0.5)
            MC "The ops got me, mom. It was a drive by."
            scene Jennifer_Scene_7PM_12 with Dissolve(0.5)
            MC "I think I'm done for..."
            scene Jennifer_Scene_7PM_13 with Dissolve(0.5)
            MC "Bang."
            scene Jennifer_Scene_7PM_14 with Dissolve(0.5)
            MC "......"
            scene Jennifer_Scene_7PM_15 with Dissolve(0.5)
            Jennifer "I told you I can't keep up with the words you kids use these days. I didn't understand a single thing."
            Jennifer "Now get up, the floor is cold, and you're getting your pants dirty!"
            scene Jennifer_Scene_7PM_16 with Dissolve(0.5)
            Jennifer "What are you doing laying on the ground here?!"
            scene Jennifer_Scene_7PM_17 with Dissolve(0.5)
            MC "Your offsprings don't know how to take the damn key out of the door after closing it!"
            scene Jennifer_Scene_7PM_18 with Dissolve(0.5)
            Isabella "Hey mommy!! Welcome home!"
            scene Jennifer_Scene_7PM_19 with Dissolve(0.5)
            Isabella "Huh?"
            scene Jennifer_Scene_7PM_20 with Dissolve(0.5)
            MC "............"
            scene Jennifer_Scene_7PM_21 with Dissolve(0.5)
            MC "Since when is this door opening both ways?"
            scene Jennifer_Scene_7PM_22 with Dissolve(0.5)
            MC "Do I have to kick the door down for you to hear it?!"
            scene Jennifer_Scene_7PM_23 with Dissolve(0.5)
            Isabella "KYAAAAAAA!!! A HOMELESS MAN!!!!"
            scene Jennifer_Scene_7PM_24 with Dissolve(0.5)
            Jennifer "Ughhh..."
            scene Jennifer_Scene_7PM_25 with Dissolve(0.5)
            Jennifer "Stop fighting and get in the house right now!"
            scene Jennifer_Scene_7PM_26 with Dissolve(0.5)
            IsaAndMC "...."
            scene Jennifer_Scene_7PM_27 with Dissolve(0.5)
            IsaAndMC "Okay, mom... Sorry..."
            $ advance_time_or_sleep()
            $ Location = "entrance"
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")