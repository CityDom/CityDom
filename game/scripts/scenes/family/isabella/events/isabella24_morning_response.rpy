label IsabellaMorning24:

    menu:
        "Knock":
            "{color=#808080}**Knock knock**{/color}"
            Isabella "It's occupied, don't you hear the shower running?"
            MC "It's me sis, I really need to go to the toilet, please, I'll be quick!"
            Isabella "No way [MC], go upstairs!"
            MC "The one upstairs is occupied, pleaaase!!"
            Isabella "Nope, piss yourself!"
            MC "{color=#808080}*Fuck... I guess I'll have to wait..*{/color}"
            $ Location = "washing room"
            $ renpy.call("GameLoop")
        "Peek":
            "{color=#808080}**You open the door as slowly and quietly as possible and get in.**{/color}"
            scene Isabella_morning24_19 with Dissolve(0.5)
            MC "{color=#808080}*I better be careful, if I'm caught I'm as good as dead!*{/color}"
            scene Isabella_morning24_18 with Dissolve(0.5)
            MC "{color=#808080}*I can't really see who is in the shower*{/color}"
            scene Isabella_morning24_17 with Dissolve(0.5)
            MC "{color=#808080}*I really need this curtain removed somehow..*{/color}"
            scene Isabella_morning24_16 with Dissolve(0.5)
            MC "{color=#808080}*Oh my god is Isabella!!!*{/color}"
            MC "{color=#808080}*Jackpot!!!*{/color}"
            scene Isabella_morning24_15 with Dissolve(0.5)
            MC "Oh.... my... god...."
            scene Isabella_morning24_14 with Dissolve(0.5)
            MC "{color=#808080}*I can't believe this is my little sister...*{/color}"
            MC "{color=#808080}*The last time I've seen her naked was when we were kids and taking baths together.*{/color}"
            MC "{color=#808080}*She's not so little anymore...*{/color}"
            scene Isabella_morning24_13 with Dissolve(0.5)
            MC "{color=#808080}*God her ass is massive!!!!*{/color}"
            MC "{color=#808080}*It looks so soft...I can't wait to get my hands on it*{/color}"
            MC "{color=#808080}*But I can't really see her that well...*{/color}"
            scene Isabella_morning24_12 with Dissolve(0.5)
            pause
            scene Isabella_morning24_11 with Dissolve(0.5)
            MC "{color=#808080}*I would risk it all and fuck her right now...*{/color}"
            MC "{color=#808080}*Only I'd be dead after making just a sound...*{/color}"
            scene Isabella_morning24_10 with Dissolve(0.5)
            MC "{color=#808080}*She's washing her breasts...*{/color}"
            MC "{color=#808080}*To have such big tits at her age...*{/color}"
            MC "{color=#808080}*A few years ago you would've thought she was a boy..*{/color}"
            scene Isabella_morning24_9 with Dissolve(0.5)
            MC "{color=#808080}*Puberty really did her justice*{/color}"
            MC "{color=#808080}*I'd give anything to be the one washing those tits...*{/color}"
            scene Isabella_morning24_8 with Dissolve(0.5)
            Isabella "{color=#808080}*Did I just hear something or am I going crazy...?*{/color}"
            scene Isabella_morning24_7 with Dissolve(0.5)
            MC "{color=#808080}*Fuck, she's turning around, she might see me!*{/color}"
            menu:
                "Stay":
                    MC "{color=#808080}*Fuck it, if I die I die!*{/color}"
                    scene Isabella_morning24_5 with Dissolve(0.5)
                    Isabella "{color=#808080}*Oh my fucking god there it's someone here... maybe is just mom or Claire...*{/color}"
                    scene Isabella_morning24_4 with Dissolve(0.5)
                    Isabella "{color=#808080}*I can't really see who it is....*{/color}"
                    Isabella "{color=#808080}*OH MY GOD IS [MC]*{/color}"
                    scene Isabella_morning24_2 with Dissolve(0.5)
                    Isabella "KYAAAAAAAAAAAAAAAAAAAHHHHHH!!!!!!!!"
                    scene Isabella_morning24_1 with Dissolve(0.5)
                    Isabella "[MC] GET THE FUCK OUT RIGHT NOW!!!!!!!!!"
                    MC "Sorry sis, I thought someone left the shower running, I just got in."
                    Isabella "GET OUT!!!!!!"
                    Isabella "NOOOOOOWWWWW!!!!!!!!!!!"
                    "{color=#808080}**You get out of the bathroom as fast as possible**{/color}"
                    call stat_reward({"Isabella": {"love": -5}}, return_to=None)
                    $ Location = "washing room"
                    $ advance_time_or_sleep()
                "Leave":
                    "{color=#808080}**Let's better get out before she sees me.**{/color}"
                    $ Location = "washing room"
                    call stat_reward({"Isabella": {"corruption": 2}}, return_to=None)
                    $ advance_time_or_sleep()
        "Open":
            scene Isabella_morning24_19 with Dissolve(0.5)
            Isabella "I'm taking a shower here!!!! get out!!!!!"
            MC "{color=#808080}*I better just leave...*{/color}"
            call stat_reward({"Isabella": {"love": -2}}, return_to=None)
            $ Location = "washing room"
            $ advance_time_or_sleep()
        "Leave":
            $ Location = "washing room"
            $ renpy.call("GameLoop")
