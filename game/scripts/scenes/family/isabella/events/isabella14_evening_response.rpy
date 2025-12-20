label IsabellaEvening14:

    scene Isabella_noon14_6 with Dissolve(0.5)
    menu:
        "Knock":
            Isabella "Who is it?"
            MC "It's me!"
            Isabella "What do you want?!"
            MC "Can't a loving brother spend time with his little sister?"
            Isabella "Cut the crap [MC], just tell me what you want!"
            MC "I just told you!"
            Isabella "Yea, right, I'm getting changed, come later if you want!"       
            $ Location = "Hallway"   
        "Peek":
            scene Isabella_evening14_1 with Dissolve(0.5)
            "{color=#808080}**You open the door quietly and peek through the door crack**{color=#808080}"
            MC "{color=#808080}*Nice, I got here just in time.*{color=#808080}"
            MC "{color=#808080}*She just started changing.*{color=#808080}"
            MC "{color=#808080}*I just have to be quiet!*{color=#808080}"
            scene Isabella_evening14_2 with Dissolve(0.5)
            MC "{color=#808080}*I can't get enough of seeing her ass.*{color=#808080}"
            scene Isabella_evening14_3 with Dissolve(0.5)
            MC "{color=#808080}*Even if she is my little sister, she is so fucking hot.*{color=#808080}"
            MC "{color=#808080}*Her tits are soo round and firm.*{color=#808080}"
            scene Isabella_evening14_4 with Dissolve(0.5)
            MC "{color=#808080}*Maybe I can see them*{color=#808080}"
            MC "{color=#808080}*But if I make a sound I'm fucked!*{color=#808080}"
            scene Isabella_evening14_5 with Dissolve(0.5)
            MC "{color=#808080}*Maybe I should leave before she catches me*{color=#808080}"
            menu:
                "Stay":
                    scene Isabella_evening14_6 with Dissolve(0.5)
                    MC "{color=#808080}*Fuck it, I'm staying.*{color=#808080}"
                    MC "{color=#808080}*I'd give anything to see those tits under all those clothes*{color=#808080}"
                    scene Isabella_evening14_7 with Dissolve(0.5)
                    MC "{color=#808080}*Fuck yea!! I knew it!*{color=#808080}"
                    MC "{color=#808080}*If only I could have a closer look*{color=#808080}"
                    scene Isabella_evening14_8 with Dissolve(0.5)
                    MC "{color=#808080}*Her tits are perfect, and her pink nipples are so small!*{color=#808080}"
                    MC "{color=#808080}*She should take out her panties now*{color=#808080}"
                    MC "{color=#808080}*Please god, don't let her notice me!*{color=#808080}"
                    scene Isabella_evening14_9 with Dissolve(0.5)
                    MC "{color=#808080}*Her ass is perfect, she definitely gets it from mom.*{color=#808080}"
                    "{color=#808080}**As you lean in to get a better lookay, the floor squeaks**{color=#808080}"
                    scene Isabella_evening14_10 with Dissolve(0.5)
                    Isabella "{color=#808080}*What the fuck was that....{color=#808080}"
                    extend "{color=#808080}It came from the door...*{color=#808080}"
                    scene Isabella_evening14_11 with Dissolve(0.5)
                    Isabella "{color=#808080}*I'm pretty sure I locked it*{color=#808080}"
                    Isabella "{color=#808080}*Don't tell me [MC] is peeking through the do-*{color=#808080}"
                    scene Isabella_evening14_12 with Dissolve(0.5)
                    Isabella "KYAAAAAAAAAAAAAAA!!!!!!"
                    Isabella "GET OUT NOW!!!!!!!"
                    MC "Oh my god, Isabella I'm so sorry I was just trying to-"
                    scene Isabella_evening14_13 with Dissolve(0.5)
                    Isabella "GET THE FUCK OUT NOW!!!!!!!"
                    "{color=#808080}**You quickly get out of the room**{color=#808080}"
                    MC "{color=#808080}*I hope she's not too mad*{color=#808080}"
                    MC "{color=#808080}*Isabella love -5*{color=#808080}"
                    $ Isabella_love = Isabella_love - 5
                    $ check_and_update_character_stats("Isabella")
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
                "Leave":
                    scene Isabella_evening14_6 with Dissolve(0.5)
                    MC "{color=#808080}*Fuck... I wanna see her naked so badly...*{color=#808080}"
                    MC "{color=#808080}*But it's better not to risk it.*{color=#808080}"
                    "{color=#808080}**You slowly step out of the room and close the door silently**{color=#808080}"
                    "{color=#808080}**Isabella corruption + 2**{color=#808080}"
                    $ Isabella_Corruption = Isabella_Corruption + 2
                    $ check_and_update_character_stats("Isabella")
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
        "Open":
            "{color=#808080}**You storm into the room without a care in the world**{color=#808080}"
            scene Isabella_evening14_12 with Dissolve(0.5)
            Isabella "KYAAAAAAAAAAA!!!!"
            Isabella "WHAT THE FUCK ARE YOU DOING!!"
            Isabella "GET THE FUCK OUT NOW!!!!"
            MC "Oh my god, I'm so sorry I didn't know you were changing, I thought you-"
            scene Isabella_evening14_13 with Dissolve(0.5)
            Isabella "I SAID GET THE FUCK OUT NOW PERVERT!!!!!!!!!!"
            "{color=#808080}**Isabella love - 5**{color=#808080}"
            $ Isabella_love = Isabella_love - 5
            $ check_and_update_character_stats("Isabella")
            $ Location = "Hallway"
        "Leave":
            MC "{color=#808080}*Better not to risk it.*{color=#808080}"
            $ Location = "Hallway"
            $ renpy.call("GameLoop")
