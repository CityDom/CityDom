label ClaireNoon14:

    scene Claire_noon14_13 with Dissolve(0.5)
    menu:
        "Knock":
            Claire "Who is it?!"
            MC "Hey Claire, It's me!"
            Claire "What do you want?!"
            MC "I just wanted to see you before you left for school!"
            MC "Can I enter?"
            Claire "No, you can't!"
            Claire "Fuck off!"
            MC "{color=#808080}*It was worth a try I guess*{/color}"
            jump ClaireNoon14
        "Peek":
            scene Claire_noon14_12 with Dissolve(0.5)
            MC "{color=#808080}*Oh my fucking God, Claire is changing!*{/color}"
            scene Claire_noon14_11 with Dissolve(0.5)
            MC "{color=#808080}*I can finally see her naked!*{/color}"
            scene Claire_noon14_10 with Dissolve(0.5)
            MC "{color=#808080}*But she's turned away, I can't see much...*{/color}"
            MC "{color=#808080}*She seems to have the same lingerie as Isabella...*{/color}"
            scene Claire_noon14_9 with Dissolve(0.5)
            MC "{color=#808080}*But Claire's tits are bigger than Isabella's!*{/color}"
            MC "{color=#808080}*She is older as well, so Isabella's are still growing.*{/color}"
            scene Claire_noon14_8 with Dissolve(0.5)
            MC "{color=#808080}*She's taking her pants off!!*{/color}"
            MC "{color=#808080}*And I have the perfect view for her ass!*{/color}"
            scene Claire_noon14_7 with Dissolve(0.5)
            MC "{color=#808080}*She definitely has mom's ass. Just like Isabella.*{/color}"
            MC "{color=#808080}*But in that category, Isabella might actually be winning.*{/color}"
            scene Claire_noon14_6 with Dissolve(0.5)
            MC "{color=#808080}*She has such a great body! Too bad she's such a bitch all the time!*{/color}"
            scene Claire_noon14_5 with Dissolve(0.5)
            MC "{color=#808080}*Maybe I should leave... She could catch me at any minute.*{/color}"
            MC "{color=#808080}*Or someone in the hallway might.*{/color}"
            menu:
                "Stay":
                    MC "{color=#808080}*Fuck it, if she catches me I'll just make a run for it.*{/color}"
                    MC "{color=#808080}*There is no reason to try to apologize to this bitch.*{/color}"
                    scene Claire_noon14_4 with Dissolve(0.5)
                    MC "{color=#808080}*She is taking her bra off!*{/color}"
                    MC "{color=#808080}*I can't quite see her tits, but they are so big that u can see them from behind as well.*{/color}"
                    scene Claire_noon14_2 with Dissolve(0.5)
                    MC "{color=#808080}*Such a mean cow with those gigantic tits.*{/color}"
                    MC "{color=#808080}*She should be taking her panties off now, and I have a first row ticket to her ass.*{/color}"
                    "{color=#808080}*As you try to get a closer lookay the door squeaks a little.*{/color}"
                    scene Claire_noon14_1 with Dissolve(0.5)
                    Claire "{color=#808080}*What the fuck was that?*{/color}"
                    Claire "{color=#808080}*Maybe it's mom barging in my room like always...*{/color}"
                    Claire "{color=#808080}*So annoying....*{/color}"
                    scene Claire_noon14_14 with Dissolve(0.5)
                    Claire "What mom? I told you a million times to knock on my door, I'm not ten years old anymore!"
                    scene Claire_noon14_15 with Dissolve(0.5)
                    Claire "WHAT THE FUCK ARE YOU DOING HERE YOU LITTLE SHIT?! GET THE FUCK OUT OF MY ROOM NOW!!!"
                    "{color=#808080}**You don't even say anything, you run out of there hoping she won't kill you later.**{/color}"
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
                "Leave":
                    MC "{color=#808080}*I shouldn't risk it.*{/color}"
                    MC "{color=#808080}*I don't have a death wish.*{/color}"
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
        "Open":
            MC "{color=#808080}*This is such a dumb idea.*{/color}"
            MC "{color=#808080}*I won't even be able to see anything. I will be dead before anything like that would happen.*{/color}"
            jump ClaireNoon14
        "Leave":
            $ Location = "Hallway"
            $ renpy.call("GameLoop")
