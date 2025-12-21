init python:
    define_images("Jennifer_weekend_10AM_", "WeekendScenes/JenniferScenes/10AM", "Jennifer_weekend_10AM_", 100)

label Jennifer_weekend_10AM:
    scene Jennifer_morning44_0
    menu:
        "Knock":
            Jennifer "What do you want?"
            MC "Can I come in?"
            Jennifer "Wait, I'm getting dressed, I'll be out in a moment!"
            menu:
                "Wait":
                    MC "{color=#808080}*I guess I'll wait...*{/color}"
                    scene blackscreen with Dissolve(0.5)
                    "{color=#808080}**Fifteen minutes later...**{color=#808080}"
                    scene Jennifer_weekend_10AM_13 with Dissolve(0.5)
                    MC "Make it three."
                    scene Jennifer_weekend_10AM_14 with Dissolve(0.5)
                    Mhyrorin "Hmmmmm..."
                    scene Jennifer_weekend_10AM_15 with Dissolve(0.5)
                    Mhyrorin "No way..."
                    scene Jennifer_weekend_10AM_16 with Dissolve(0.5)
                    Mhyrorin "I call bullshit!"
                    scene Jennifer_weekend_10AM_17 with Dissolve(0.5)
                    MC "Take 'em."
                    scene Jennifer_weekend_10AM_18 with Dissolve(0.5)
                    Mhyrorin "UGHHHH!!! Is not fair!!! How the fuck are you always winning?!!?"
                    scene Jennifer_weekend_10AM_19 with Dissolve(0.5)
                    Jennifer "[MC], honey, are you still waiting there?"
                    scene Jennifer_weekend_10AM_20 with Dissolve(0.5)
                    MC "Uhhhh... Yeah?"
                    scene Jennifer_weekend_10AM_19 with Dissolve(0.5)
                    Jennifer "Okay, you can come in, mommy's ready."
                    scene Jennifer_weekend_10AM_20 with Dissolve(0.5)
                    MC "Okay, just a second."
                    scene Jennifer_weekend_10AM_21 with Dissolve(0.5)
                    MC "{color=#808080}*Damn she's fast... I didn't even notice when she took my cards...*{/color}"
                    scene Jennifer_weekend_10AM_22 with Dissolve(0.5)
                    MC "Sorry to bother mom, I know you're about to go to church."
                    scene Jennifer_weekend_10AM_23 with Dissolve(0.5)
                    Jennifer "No problem honey, but when I tell you to wait a bit, you don't need to stay stuck outside the door until I'm ready, okay?"
                    scene Jennifer_weekend_10AM_24 with Dissolve(0.5)
                    MC "Oka-Gaaaaaaaahhh!!"
                    scene Jennifer_weekend_10AM_25 with Dissolve(0.5)
                    Jennifer "Huh? What is it?"
                    scene Jennifer_weekend_10AM_26 with Dissolve(0.5)
                    Jennifer "Did I do too much?"
                    scene Jennifer_weekend_10AM_27 with Dissolve(0.5)
                    Jennifer "I'll get changed..."
                    scene Jennifer_weekend_10AM_28 with Dissolve(0.5)
                    MC "No you're not, wait just a second!"
                    scene Jennifer_weekend_10AM_29 with Dissolve(0.5)
                    Jennifer "W-what? Why?"
                    scene Jennifer_weekend_10AM_30 with Dissolve(0.5)
                    MC "Because you look fu-... completely amazing! And I'm taking a picture!"
                    MC "Stop acting like it's the first day of highschool."
                    scene Jennifer_weekend_10AM_31 with Dissolve(0.5)
                    Jennifer "So I don't need to get changed?"
                    scene Jennifer_weekend_10AM_32 with Dissolve(0.5)
                    MC "No, you look perfect."
                    scene Jennifer_weekend_10AM_33 with Dissolve(0.5)
                    MC "But you need to smile, c'mon."
                    scene Jennifer_weekend_10AM_34 with Dissolve(0.5)
                    Jennifer "Honestly, [MC], stop scaring me like that..."
                    scene Jennifer_weekend_10AM_35 with Dissolve(0.5)
                    pause
                    $ background_buttons.update({"JenniferChurchBackground": False,})   
                    $ background_previews.update({"JenniferChurchBackground": "WallpaperPreview_Lingerie_Scarlet.png",})
                    $ background_buttons["JenniferChurchBackground"] = True
                    scene Jennifer_weekend_10AM_36 with Dissolve(0.5)
                    Jennifer "Did you take it? Do I look okay?"
                    scene Jennifer_weekend_10AM_37 with Dissolve(0.5)
                    MC "Yep, it turned out great! Let me show you."
                    scene Jennifer_weekend_10AM_38 with Dissolve(0.5)
                    Jennifer "You should've taken it with sunlight coming towards me."
                    scene Jennifer_weekend_10AM_39 with Dissolve(0.5)
                    MC "It's good enough for me."
                    scene Jennifer_weekend_10AM_40 with Dissolve(0.5)
                    Jennifer "Okay then, I have to go, church starts soon, what did you want to ask mom about?"
                    scene Jennifer_weekend_10AM_41 with Dissolve(0.5)
                    MC "Uhhhh... to be honest, I don't even remember..."
                    scene Jennifer_weekend_10AM_42 with Dissolve(0.5)
                    Jennifer "Eh, I can't even be mad about it, you probably got that from me..."
                    scene Jennifer_weekend_10AM_43 with Dissolve(0.5)
                    Jennifer "Okay, get out of here, I'm running late!"
                    call stat_reward({"Jennifer": {"love": 2}}, return_to=None)
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
                "Leave":
                    MC "{color=#808080}*I guess I'll have to do something else until then.*{/color}"
                    $ Location = "Hallway"
                    $ renpy.call("GameLoop")
        "Peek":
            scene Jennifer_weekend_10AM_1 with Dissolve(0.5)
            MC "{color=#808080}*Jackpot!*{/color}"
            scene Jennifer_weekend_10AM_2 with Dissolve(0.5)
            MC "{color=#808080}*My timing is impeccable, sometimes my genius is scary!*{/color}"
            scene Jennifer_weekend_10AM_3 with Dissolve(0.5)
            MC "{color=#808080}*The angle could be better, but her tits are so massive you can see them from any angle.*{/color}"
            scene Jennifer_weekend_10AM_4 with Dissolve(0.5)
            MC "{color=#808080}*God she's so fucking hot, but maybe I should leave before someone finds me here...*"
            menu:
                "Stay":
                    scene Jennifer_weekend_10AM_5 with Dissolve(0.5)
                    MC "{color=#808080}*Ok, maybe just a bit more... at least until I get a better angle.*"
                    scene Jennifer_weekend_10AM_6 with Dissolve(0.5)
                    MC "{color=#808080}*Holy Jesus...*"
                    scene Jennifer_weekend_10AM_7 with Dissolve(0.5)
                    MC "{color=#808080}*Hughhhhhhhhh!!!*"
                    scene Jennifer_weekend_10AM_8 with Dissolve(0.5)
                    Jennifer "Huh?"
                    scene Jennifer_weekend_10AM_9 with Dissolve(0.5)
                    Jennifer "{color=#808080}*Is someone...?*"  
                    scene Jennifer_weekend_10AM_10 with Dissolve(0.5)
                    MC "{color=#808080}*Does she have fucking X-rays?! What the hell is this?!*"
                    MC "{color=#808080}*Anyway, time to go!*"
                    scene Jennifer_weekend_10AM_11 with Dissolve(0.5)
                    Jennifer "{color=#808080}*UGHHHHH!!!! [MC_upper]!!!!*"
                    call stat_reward({"Jennifer": {"love": -5}}, return_to=None)
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
                "Leave":
                    MC "{color=#808080}Let's better not risk it.*"
                    call stat_reward({"Jennifer": {"corruption": 2}}, return_to=None)
                    $ Location = "Hallway"
                    $ renpy.call("GameLoop")
        "Open":
            scene Jennifer_weekend_10AM_12 with Dissolve(0.5)
            Jennifer "WHAT THE HELL ARE YOU DOING!!! GET OUT!!!!!"
            Jennifer "KNOCK ON THAT GODDAMN DOOR NEXT TIME!!!!!"
            call stat_reward({"Jennifer": {"love": -5}}, return_to=None)
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "Leave":
            MC "{color=#808080}*Maybe some other time.*{/color}"
            $ Location = "Hallway"
            $ renpy.call("GameLoop")
