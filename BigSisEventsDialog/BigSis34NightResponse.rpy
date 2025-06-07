label BigSisNight34:

    scene NIGHT34BIGSIS3 with Dissolve(0.5)
    menu:
        "Knock":
            MC "Hey! Can I enter? I really need to use the bathroom!"
            Clair "Can't your deaf ass hear the shower running?!"
            Clair "Get lost loser!"
            MC "But I really need to go sis! Please!"
            Clair "If you touch that door knob you are dead!"
            MC "{color=#808080}*Fuck... I'll just leave...*{/color}"
            $ Location = "washing room"
            $ renpy.call("GameLoop")
        "Peek":
            scene NIGHT34BIGSIS1 with Dissolve(0.5)
            MC "{color=#808080}*I have to be really quiet!*{/color}"
            MC "{color=#808080}*If she catches me I'm dead!*{/color}"
            scene NIGHT34BIGSIS2 with Dissolve(0.5)
            MC "{color=#808080}*Holy shit, I can see her!*{/color}"
            MC "{color=#808080}*I can finally see her fully naked!*{/color}"
            scene NIGHT34BIGSIS4 with Dissolve(0.5)
            MC "{color=#808080}*She is so fucking hot.*{/color}"
            MC "{color=#808080}*If only she wasn't such a fucking bitch!*{/color}"
            scene NIGHT34BIGSIS5 with Dissolve(0.5)
            MC "{color=#808080}*She has mom's body, her tits and her ass are a hundred percent from her.*{/color}"
            MC "{color=#808080}*Even her legs and her waste are perfect.*{/color}"
            MC "{color=#808080}*Fuck... I'm getting hard...*{/color}"
            MC "{color=#808080}*I should get out fast...*{/color}"
            menu:
                "Watch closer":
                    MC "{color=#808080}*Fuck it, I want to see more!*{/color}"
                    scene NIGHT34BIGSIS6 with Dissolve(0.5)
                    MC "{color=#808080}*No way I can see her pussy as well.*{/color}"
                    MC "{color=#808080}*Barely though...*{/color}"
                    MC "{color=#808080}*If only she would bow down a little, it would be on full display!*{/color}"
                    scene NIGHT34BIGSIS7 with Dissolve(0.5)
                    Clair "{color=#808080}*Ughhhh...*{/color}"
                    Clair "{color=#808080}*Am I seeing things?!*{/color}"
                    Clair "{color=#808080}*For sure that is not....*{/color}"
                    scene NIGHT34BIGSIS8 with Dissolve(0.5)
                    Clair "{color=#808080}*No fucking way!!*{/color}"
                    scene NIGHT34BIGSIS9 with Dissolve(0.5)
                    Clair "GET THE FUCK OUT OF HERE NOW YOU DISGUSTING CREEP!!!!"
                    MC "I'm so sorry Claire, I didn't reali-"
                    Clair "GET THE FUCK OUT NOW YOU PIECE OF SHIT!!! YOU ARE DEAD!!!"
                    "{color=#808080}**You rush out of the bathroom scared for your life.**{/color}"
                    $ Location = "washing room"
                    $ advance_time_or_sleep()
                "Leave":
                    MC "{color=#808080}*I can't risk it...*{/color}"
                    MC "{color=#808080}*She would kill me if she were to catch me*{/color}"
                    "{color=#808080}**You leave the bathroom as quietly as possible**{/color}"
                    $ Location = "washing room"
                    $ advance_time_or_sleep()
        "Open":
            scene NIGHT34BIGSIS8 with Dissolve(0.5)
            Clair "What the fuck...."
            scene NIGHT34BIGSIS10 with Dissolve(0.5)
            Clair "GET OUT NOW!!!!!!"
            Clair "DON'T YOU KNOW HOW TO FUCKING KNOCK YOU STUPID SHIT?!?!"
            "{color=#808080}**You rush out as fast as possible**{/color}"
            $ Location = "washing room"
            $ advance_time_or_sleep()
        "Leave":
            MC "{color=#808080}*Maybe some other time.*{/color}"
            $ Location = "washing room"
            $ renpy.call("GameLoop")