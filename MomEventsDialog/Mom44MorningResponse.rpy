label MomMorning44:

    menu:
        "Knock":
            McMom "What do you want?"
            MC "May I come in?"
            McMom "Please wait, I'm getting dressed, I'll be out in a moment!"
            MC "I guess I'll have to do something else until then."
            $ Location = "Hallway"
            return
        "Peek":
            MC "{color=#808080}*A little peek won't hurt nobody right?*{/color}"
            "{color=#808080}**You open the door slowly and making as little sound as possible.**"
            scene MORNINGS44MOM0 with Dissolve(0.5)
            $ renpy.pause(0.5, hard=True)
            scene MORNINGS44MOM1 with Dissolve(0.5)
            MC "{color=#808080}*Nice, I struck gold!*{/color}"
            MC "{color=#808080}*She has no bra!!! Her tits are so big and beautiful, simply amazing.*{/color}"
            scene MORNINGS44MOM2 with Dissolve(0.5)
            MC "{color=#808080}*Oh my god, she took it completely off!!*{/color}"
            MC "{color=#808080}*Fuck, I gotta leave, she might turn any second...*{/color}"
            menu:
                "Stay":
                    # if (Mom_love > 10):
                    #     MC "{color=#808080}*Nah, fuck it, I'm all in.*{/color}"
                    #     "......"
                    #     MC "{color=#808080}*Okay, now the pants..*"
                    #     scene MORNINGS44MOM3 with Dissolve(0.5)
                    #     $ renpy.pause(0.5, hard=True)
                    #     scene MORNINGS44MOM4 with Dissolve(0.5)
                    #     MC "{color=#808080}*Now the bottoms, I can already see her ass through the leggings.*{/color}"
                    #     MC "{color=#808080}*God damn she is so hot!*{/color}"
                    #     MC "{color=#808080}*Her ass is big as fuck... I'm amazed those leggings are not ripping apart.*{/color}"
                    #     scene MORNINGS44MOM5 with Dissolve(0.5)
                    #     $ renpy.pause(0.5, hard=True)
                    #     scene MORNINGS44MOM6 with Dissolve(0.5)
                    #     $ renpy.pause(0.5, hard=True)
                    #     scene MORNINGS44MOM7 with Dissolve(0.5)
                    #     MC "{color=#808080}*Oh my GOD, completely she's naked!!!*{/color}"
                    #     MC "{color=#808080}*She's so fucking hot!!!*{/color}"
                    #     MC "{color=#808080}*I can't believe that's my mother!*{/color}"
                    #     scene MORNINGS44MOM8 with Dissolve(0.5)
                    #     MC "{color=#808080}*And she's not wearing any panties...*{/color}"
                    #     scene MORNINGS44MOM9 with Dissolve(0.5)
                    #     MC "{color=#808080}*You could never see them even if she was wearing any...*{/color}"
                    #     MC "{color=#808080}*She always wears old modest clothing...*{/color}"
                    #     scene MORNINGS44MOM10 with Dissolve(0.5)
                    #     $ renpy.pause(0.5, hard=True)
                    #     scene MORNINGS44MOM11 with Dissolve(0.5)
                    #     MC "{color=#808080}*She's getting dressed up..*{/color}"
                    #     scene MORNINGS44MOM12 with Dissolve(0.5)
                    #     $ renpy.pause(0.5, hard=True)
                    #     scene MORNINGS44MOM13 with Dissolve(0.5)
                    #     $ renpy.pause(0.5, hard=True)
                    #     scene MORNINGS44MOM14 with Dissolve(0.5)
                    #     $ renpy.pause(0.5, hard=True)
                    #     scene MORNINGS44MOM15 with Dissolve(0.5)
                    #     MC "{color=#808080}*Same old suit i bet... not showing an inch of her body*{/color}"
                    #     scene MORNINGS44MOM16 with Dissolve(0.5)
                    #     MC "{color=#808080}*But her tits and ass are so big even those clothes can't hide them.*{/color}"
                    #     scene MORNINGS44MOM17 with Dissolve(0.5)
                    #     $ renpy.pause(0.5, hard=True)
                    #     scene MORNINGS44MOM18 with Dissolve(0.5)
                    #     MC "{color=#808080}*Okay, she's about to turn around, time to leave*{/color}"
                    #     "You slowly close the door and get out as soon as possible."
                    #     $ advance_time_or_sleep()
                    #     $ Location = "Hallway"
                    #     return
                    # else:
                    MC "{color=#808080}*Nah, fuck it, I'm all in.*{/color}"
                    "......"
                    MC "Okay, now the pants.."
                    scene MORNINGS44MOM3 with Dissolve(0.5)
                    $ renpy.pause(0.5, hard=True)
                    scene MORNINGS44MOM4 with Dissolve(0.5)
                    MC "{color=#808080}*Now the bottoms... I can already see her ass through the leggings.*{/color}"
                    MC "{color=#808080}*God damn, she is so hot!*{/color}"
                    MC "{color=#808080}*Her ass is big as fuck... I'm amazed those leggings are not ripping apart.*{/color}"
                    scene MORNINGS44MOM5 with Dissolve(0.5)
                    $ renpy.pause(0.5, hard=True)
                    scene MORNINGS44MOM6 with Dissolve(0.5)
                    $ renpy.pause(0.5, hard=True)
                    scene MORNINGS44MOM7 with Dissolve(0.5)
                    MC "{color=#808080}*Oh my god, she's completely naked!!!*{/color}"
                    MC "{color=#808080}*She's so fucking hot!!!*{/color}"
                    MC "{color=#808080}*I can't believe that's my mother!*{/color}"
                    scene MORNINGS44MOM8 with Dissolve(0.5)
                    MC "{color=#808080}*And she's not wearing any panties...*{/color}"
                    scene MORNINGS44MOM9 with Dissolve(0.5)
                    McMom "Huh??"
                    scene MORNINGS44MOM20 with Dissolve(0.5)
                    McMom "AAAAAAHHHH !!!!!!!!"
                    MC "{color=#808080}*Fuck.. I pushed my luck too much..*{/color}"
                    scene MORNINGS44MOM21 with Dissolve(0.5)
                    McMom "[MC_upper] GET OUT RIGHT NOW!!!!!!"
                    MC "{color=#808080}*I hope she won't stay mad for long..*{/color}"
                    "{color=#808080}**Mom love - 5**{color=#808080}"
                    $ Mom_love = Mom_love - 5
                    $ check_and_update_character_stats("Mom")
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
                "Leave":
                    MC "{color=#808080}*Yeah... I'm not risking that.*{/color}"
                    "{color=#808080}**Mom corruption + 2**{color=#808080}"
                    $ Mom_Corruption = Mom_Corruption + 2
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
        "Open":
            "{color=#808080}**You open the door and barge in.**"
            scene MORNINGS44MOM20 with Dissolve(0.5)
            McMom "AAAAAAHHHH !!!!!!!!"
            MC "{color=#808080}*Fuck... what was i thinking?*{/color}"
            MC "{color=#808080}*.... god damn she's hot... whatever punishment I get for this it was worth it.*{/color}"
            scene MORNINGS44MOM21 with Dissolve(0.5)
            McMom "WHAT ARE YOU DOING BARGING IN LIKE THIS?!?!?!"
            McMom "GET OUT RIGHT NOW!!!!!!!!"
            MC "{color=#808080}*I hope she won't be mad at me for long...*{/color}"
            "{color=#808080}**Mom love - 5**{color=#808080}"
            $ Mom_love = Mom_love - 5
            $ check_and_update_character_stats("Mom")
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "Leave":
            MC "Maybe another time..."
            "{color=#808080}**You leave.**"
            $ Location = "Hallway"


