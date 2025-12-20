init python:
    define_images("Claire_weekend_7AM_", "WeekendScenes/ClaireScenes/7AM", "Claire_weekend_7AM_", 100)

label Claire_weekend_7AM:
    scene Claire_weekend_7AM_1 with Dissolve(0.5)
    menu:
        "Knock":
            MC "Hey! Anyone in there?"
            scene Claire_weekend_7AM_2 with Dissolve(0.5)
            Claire "Ughh... not now..."
            scene Claire_weekend_7AM_3 with Dissolve(0.5)
            Claire "GET LOST ALREADY!"
            scene Claire_weekend_7AM_1 with Dissolve(0.5)
            MC "Tsk...."
            $ Location = "washing room"
            $ renpy.call("GameLoop")
        "Peek":
            MC "{color=#808080}*Ughhh.... I'm really trying my luck here.*"
            scene Claire_weekend_7AM_4 with Dissolve(0.5)
            Claire "Mmmm..."
            scene Claire_weekend_7AM_5 with Dissolve(0.5)
            MC "{color=#808080}*What the hell am I doing...? I should leave.*"
            scene Claire_weekend_7AM_6 with Dissolve(0.5)
            MC "{color=#808080}*But... she didn't lock the door. Maybe she forgot. Or maybe she wanted to be caught...*"
            scene Claire_weekend_7AM_7 with Dissolve(0.5)
            MC "{color=#808080}*No, that's stupid... What am I thinking?*"
            scene Claire_weekend_7AM_8 with Dissolve(0.5)
            MC "{color=#808080}*Just take a peek. Quick. No sound. No trace.*"
            MC "{color=#808080}*And if she catches me, I'll just say I thought someone left the water running. Yeah, good one...*"
            scene Claire_weekend_7AM_9 with Dissolve(0.5)
            MC "{color=#808080}*Gaahhh*{/color}"
            scene Claire_weekend_7AM_10 with Dissolve(0.5)
            MC "{color=#808080}*Hoooly fuck...*{/color}"
            MC "{color=#808080}*I get chills every time I see her like this.*{/color}"
            scene Claire_weekend_7AM_11 with Dissolve(0.5)
            MC "{color=#808080}*She may be a bitch... but those tits totally make up for it.*{/color}"
            scene Claire_weekend_7AM_12 with Dissolve(0.5)
            MC "{color=#808080}*But... Tch... I can't see her pussy from here.*{/color}"
            MC "{color=#808080}*If I moved up a bit, maybe I could.*{/color}"
            menu:
                "Peek further":
                    scene Claire_weekend_7AM_13 with Dissolve(0.5)
                    MC "{color=#808080}*Nah... I'm not dying over a peek.*{/color}"
                    MC "{color=#808080}*That pussy isn't worth a hospital visit.*{/color}"
                    $ Location = "washing room"
                    $ advance_time_or_sleep()
                "Leave":
                    scene Claire_weekend_7AM_13 with Dissolve(0.5)
                    MC "{color=#808080}*I think I tried my luck enough, let's just leave.*{/color}"
                    $ Location = "washing room"
                    $ advance_time_or_sleep()
        "Open":
            "**You enter the bathroom without a care in the world.**"
            scene Claire_weekend_7AM_14 with Dissolve(0.5)
            Claire "Hmmm...?"
            scene Claire_weekend_7AM_15 with Dissolve(0.5)
            Claire "Huh?!"
            scene Claire_weekend_7AM_16 with Dissolve(0.5)
            Claire "GET THE FUCK OUT OF HERE NOW YOU DISGUSTING CREEP!!!!"
            Claire "DON'T YOU KNOW HOW TO FUCKING KNOCK?!!!"
            scene BlackScreen with Dissolve(0.5)
            "**You bolt out of the bathroom**"
            $ Location = "washing room"
            $ renpy.call("GameLoop")
        "Leave":
            MC "{color=#808080}*Yeah... let's leave the crazy bitch alone for today*{/color}"
            $ Location = "washing room"
            $ renpy.call("GameLoop")
