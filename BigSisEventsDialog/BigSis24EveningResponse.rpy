label BigSisEvening24:

    scene EVENING24BIGSIS4 with Dissolve(0.5)
    menu:
        "Knock":
            Clair "Yea? Who is it?"
            MC "It's me sis, I just wanted to talk to you for a little bit."
            Clair "I don't care loser. Get lost!"
            MC "Just for a second! It won't take long!"
            Clair "....."
            MC "....."
            "......"
            MC "{color=#808080}*She's just ignoring me...*{/color}"
            jump BigSisNoon14
        "Peek":
            MC "{color=#808080}*Maybe I can take a little peak...*{/color}"
            scene EVENING24BIGSIS1 with Dissolve(0.5)
            MC "{color=#808080}*Oh my god, I came at the perfect time!*{/color}"
            MC "{color=#808080}*She just started changing!*{/color}"
            scene EVENING24BIGSIS2 with Dissolve(0.5)
            MC "{color=#808080}*If she catches me I'm so dead!*{/color}"
            MC "{color=#808080}*But it's worth if that means that I can see her tits.*{/color}"
            scene EVENING24BIGSIS3 with Dissolve(0.5)
            MC "{color=#808080}*And I'm so close to see them!*{/color}"
            scene EVENING24BIGSIS5 with Dissolve(0.5)
            MC "{color=#808080}*I can't get enough of her ass. I could stare at it all day!*{/color}"
            MC "{color=#808080}*But sadly I think I should leave.*{/color}"
            menu:
                "Stay":
                    MC "{color=#808080}*Fuck it, I hope I could at least see her tits before she catches me.*{/color}"
                    scene EVENING24BIGSIS6 with Dissolve(0.5)
                    MC "{color=#808080}*If she kills me after that I would be at peace.*{/color}"
                    scene EVENING24BIGSIS7 with Dissolve(0.5)
                    MC "{color=#808080}*Oh my god they are perfect!!!*{/color}"
                    MC "{color=#808080}*I wish I could get a good grip of them!*{/color}"
                    scene EVENING24BIGSIS8 with Dissolve(0.5)
                    $ renpy.pause(0.5, hard=True)
                    scene EVENING24BIGSIS9 with Dissolve(0.5)
                    MC "{color=#808080}*I got to see what I wanted...*{/color}"
                    MC "{color=#808080}*Her tits are gigantic!!*{/color}"
                    scene EVENING24BIGSIS10 with Dissolve(0.5)
                    MC "{color=#808080}*I should get out now!*{/color}"
                    "{color=#808080}**As you try to slowly close the door, a slight squeak gets out.**{/color}"
                    scene EVENING24BIGSIS11 with Dissolve(0.5)
                    Clair "{color=#808080}*What the fuck was that?*{/color}"
                    Clair "{color=#808080}*Don't tell me that loser is peeking on me again!*{/color}"
                    scene EVENING24BIGSIS12 with Dissolve(0.5)
                    Clair "Who the fu..."
                    "{color=#808080}**You manage to get out before she catches you**{/color}"
                    scene EVENING24BIGSIS13 with Dissolve(0.5)
                    Clair "{color=#808080}*The piece of shit got out before I could catch him.*{/color}"
                    Clair "{color=#808080}*When I see him, he's dead.*{/color}"
                    $ Location = "Entrance"
                    $ advance_time_or_sleep()
                "Leave":
                    MC "{color=#808080}*Maybe some other time.*{/color}"
                    $ Location = "Entrance"
                    $ advance_time_or_sleep()
        "Open":
            MC "{color=#808080}*This is such a dumb idea.*{/color}"
            MC "{color=#808080}*I won't even be able to see anything. I will be dead before anything like that would happen.*{/color}"
            jump BigSisNoon14
        "Leave":
            MC "{color=#808080}*Let's leave the bitch alone for now.*{/color}"
            $ Location = "Entrance"