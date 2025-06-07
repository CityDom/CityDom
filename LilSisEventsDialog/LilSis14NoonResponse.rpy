label LilSisNoon14:

    scene NOON14LILSIS6 with Dissolve(0.5)
    menu:
        "Knock":
            Isabella "What do you want?!"
            MC "I just wanted to see you before you leave for school."
            Isabella "I'm changing and I'm in a rush, we'll talk after I'm done with school."
            MC "Oke..."
            $ Location = "Hallway"
        "Peek":
            scene NOON14LILSIS5 with Dissolve(0.5)
            "{color=#808080}*You open the door quietly and peek through the door crack*{color=#808080}"
            MC "{color=#808080}*Isa is changing into uniform.*{color=#808080}"
            MC "{color=#808080}*I hope she won't notice me*{color=#808080}"
            scene NOON14LILSIS4 with Dissolve(0.5)
            MC "{color=#808080}*Wow...*{color=#808080}"
            MC "{color=#808080}*She is so hot!*{color=#808080}"
            scene NOON14LILSIS3 with Dissolve(0.5)
            MC "{color=#808080}*I hope she won't notice me*{color=#808080}"
            MC "{color=#808080}*Maybe I should leave*{color=#808080}"
            menu:
                "Stay":
                    scene NOON14LILSIS2 with Dissolve(0.5)
                    MC "{color=#808080}*Fuck it, I'll risk it.*{color=#808080}"
                    MC "{color=#808080}*Maybe I'll get to see her naked...*{color=#808080}"
                    scene NOON14LILSIS1 with Dissolve(0.5)
                    MC "{color=#808080}*I just have to make sure to not make any sound!*{color=#808080}"
                    scene NOON14LILSIS10 with Dissolve(0.5)
                    MC "{color=#808080}*Omg, thank god I waited a bit longer.*{color=#808080}"
                    MC "{color=#808080}*I can finally see her naked tits!*{color=#808080}"
                    scene NOON14LILSIS11 with Dissolve(0.5)
                    "{color=#808080}**The floor squeaks as you try to get a closer look.**{color=#808080}"
                    Isabella "{color=#808080}*Huh, did I just hear something??*{color=#808080}"
                    scene NOON14LILSIS8 with Dissolve(0.5)
                    Isabella "KYAAAAAAAAA!!!!!!!"
                    Isabella "GET THE FUCK OUT YOU PERVERT!!!!!"
                    MC "I'm so sorry, I just came in, I didn't see anything I swea-"
                    Isabella "GET OUT!!!!!! NOW!!!!!"
                    "{color=#808080}**You leave the room immediately.**{color=#808080}"
                    $ LilSis_love = LilSis_love - 5
                    $ check_and_update_character_stats("LilSis")
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
                "Leave":
                    MC "{color=#808080}*It's better if I just leave.*{color=#808080}"
                    "{color=#808080}**You leave the room quietly**{color=#808080}"
                    "{color=#808080}**Isabella corruption + 2**{color=#808080}"
                    $ LilSis_Corruption = LilSis_Corruption + 2
                    $ check_and_update_character_stats("LilSis")
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
        "Open":
            "{color=#808080}**You storm into the room without a care in the world.**{color=#808080}"
            scene NOON14LILSIS7 with Dissolve(0.5)
            Isabella "KYAAAAAAA!!!!!"
            Isabella "WHAT THE FUCK ARE YOU DOING??!?!!?"
            Isabella "GET THE FUCK OUT NOW!!!!!!!!"
            MC "Omg I'm so sorry I didn't know u were in the ro-"
            Isabella "GET OOOOOUT!!!!!!!!"
            "{color=#808080}**You leave the room immediately.**{color=#808080}"
            "{color=#808080}**Isabella love - 5**{color=#808080}"
            $ LilSis_love = LilSis_love - 5
            $ check_and_update_character_stats("LilSis")
            $ Location = "Hallway"
        "Leave":
            MC "{color=#808080}*Let's not risk it today.*{color=#808080}"
            $ Location = "Hallway"
        
