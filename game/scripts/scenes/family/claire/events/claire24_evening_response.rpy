label ClaireEvening24:

    scene Claire_evening24_4 with Dissolve(0.5)
    menu:
        "Knock":
            Claire "Yea? Who is it?"
            MC "It's me sis, I just wanted to talk to you for a little bit."
            Claire "I don't care loser. Get lost!"
            MC "Just for a second! It won't take long!"
            Claire "....."
            MC "....."
            "......"
            MC "{color=#808080}*She's just ignoring me...*{/color}"
            jump ClaireNoon14
        "Peek":
            MC "{color=#808080}*Maybe I can take a little peak...*{/color}"
            scene Claire_evening24_1 with Dissolve(0.5)
            MC "{color=#808080}*Oh my god, I came at the perfect time!*{/color}"
            MC "{color=#808080}*She just started changing!*{/color}"
            scene Claire_evening24_2 with Dissolve(0.5)
            MC "{color=#808080}*If she catches me I'm so dead!*{/color}"
            MC "{color=#808080}*But it's worth if that means that I can see her tits.*{/color}"
            scene Claire_evening24_3 with Dissolve(0.5)
            MC "{color=#808080}*And I'm so close to see them!*{/color}"
            scene Claire_evening24_5 with Dissolve(0.5)
            MC "{color=#808080}*I can't get enough of her ass. I could stare at it all day!*{/color}"
            MC "{color=#808080}*But sadly I think I should leave.*{/color}"
            menu:
                "Stay":
                    MC "{color=#808080}*Fuck it, I hope I could at least see her tits before she catches me.*{/color}"
                    scene Claire_evening24_6 with Dissolve(0.5)
                    MC "{color=#808080}*If she kills me after that I would be at peace.*{/color}"
                    scene Claire_evening24_7 with Dissolve(0.5)
                    MC "{color=#808080}*Oh my god they are perfect!!!*{/color}"
                    MC "{color=#808080}*I wish I could get a good grip of them!*{/color}"
                    scene Claire_evening24_8 with Dissolve(0.5)
                    $ renpy.pause(0.5, hard=True)
                    scene Claire_evening24_9 with Dissolve(0.5)
                    MC "{color=#808080}*I got to see what I wanted...*{/color}"
                    MC "{color=#808080}*Her tits are gigantic!!*{/color}"
                    scene Claire_evening24_10 with Dissolve(0.5)
                    MC "{color=#808080}*I should get out now!*{/color}"
                    "{color=#808080}**As you try to slowly close the door, a slight squeak gets out.**{/color}"
                    scene Claire_evening24_11 with Dissolve(0.5)
                    Claire "{color=#808080}*What the fuck was that?*{/color}"
                    Claire "{color=#808080}*Don't tell me that loser is peeking on me again!*{/color}"
                    scene Claire_evening24_12 with Dissolve(0.5)
                    Claire "Who the fu..."
                    "{color=#808080}**You manage to get out before she catches you**{/color}"
                    scene Claire_evening24_13 with Dissolve(0.5)
                    Claire "{color=#808080}*The piece of shit got out before I could catch him.*{/color}"
                    Claire "{color=#808080}*When I see him, he's dead.*{/color}"
                    $ Location = "Entrance"
                    $ advance_time_or_sleep()
                "Leave":
                    MC "{color=#808080}*Maybe some other time.*{/color}"
                    $ Location = "Entrance"
                    $ advance_time_or_sleep()
        "Open":
            MC "{color=#808080}*This is such a dumb idea.*{/color}"
            MC "{color=#808080}*I won't even be able to see anything. I will be dead before anything like that would happen.*{/color}"
            jump ClaireNoon14
        "Leave":
            MC "{color=#808080}*Let's leave the bitch alone for now.*{/color}"
            $ Location = "Entrance"
            $ renpy.call("GameLoop")
