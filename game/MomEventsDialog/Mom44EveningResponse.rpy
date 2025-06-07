label MomEvening44:

    menu:
        "Talk":
            scene EVENINGS44MOM1 with Dissolve(0.5)
            MC "Hey mom, how are you?"
            scene EVENINGS44MOM14 with Dissolve(0.5)
            McMom "Sorry, I can't talk right now, I need to focus."
            scene EVENINGS44MOM1 with Dissolve(0.5)
            MC "Can I help you?"
            scene EVENINGS44MOM14 with Dissolve(0.5)
            McMom "You are sweet kiddo, but I don't think you can help me here."
            McMom "I'm cooking something more complicated and you would just get in the way."
            scene EVENINGS44MOM1 with Dissolve(0.5)
            MC "{color=#808080}*... you could've said that more nicely..*{/color}"
            MC "Okay mom, can't wait to see what you're cooking!"
            scene EVENINGS44MOM14 with Dissolve(0.5)
            McMom "It will be done soon, go sit at the table."
            $ Location = "livingroom"
        "Hug":
            scene EVENINGS44MOM15 with Dissolve(0.5)
            MC "Aaaand.."
            scene EVENINGS44MOM16 with Dissolve(0.5)
            MC "Surpriseee!!!"
            McMom "AAAAAAAAAAAAA"
            scene EVENINGS44MOM17 with Dissolve(0.5)
            McMom "Oh my goodness, [MC], you really startled me there!"
            McMom "Don't ever do that again!"
            scene EVENINGS44MOM18 with Dissolve(0.5)
            MC "Ok, mom, I'm sorry, I'll never hug you again. I understand..."
            scene EVENINGS44MOM17 with Dissolve(0.5)
            McMom "Oh, c'mon, [MC], you know I didn't mean it like that."
            McMom "I really appreciate you hugging me."
            scene EVENINGS44MOM19 with Dissolve(0.5)
            McMom "So tell me, What do you want?"
            scene EVENINGS44MOM20 with Dissolve(0.5)
            MC "You keep saying that I wan't something from you!"
            MC "Can't I love my mom just because?"
            scene EVENINGS44MOM21 with Dissolve(0.5)
            McMom "So you just got really lovey dovey all of the sudden, huh?"
            scene EVENINGS44MOM20 with Dissolve(0.5)
            MC "Well... being away all this time does that to you."
            scene EVENINGS44MOM21 with Dissolve(0.5)
            McMom "I guess you're right..."
            McMom "And I love you too, kiddo."
            McMom "But are you going to be clinging on me all night?"
            McMom "I really have to get dinner ready."
            scene EVENINGS44MOM20 with Dissolve(0.5)
            MC "Just a little bit more!"
            scene EVENINGS44MOM22 with Dissolve(0.5)
            McMom "Okay, but don't cry when some hot oil jumps on your hands"
            scene EVENINGS44MOM23 with Dissolve(0.5)
            MC "{color=#808080}*Her ass is pressing right onto my dick...*{/color}"
            MC "{color=#808080}*Is almost like she's doing it on purpose!*{/color}"
            MC "{color=#808080}*But I'm getting really hard, and if she finds out I'm dead!*{/color}"
            MC "{color=#808080}*Maybe I should leave...*{/color}"
            MC "{color=#808080}*But It feels so good... and I don't know if I'll ever get into a position like that with her...*{/color}"
            menu:
                "Grab her boobs":
                    MC "{color=#808080}*I'll just loosely lay my hand on her tit, maybe she won't feel it...*{/color}"
                    MC "{color=#808080}*I'm so nervous...*{/color}"
                    scene EVENINGS44MOM24 with Dissolve(0.5)
                    MC "{color=#808080}*Oh my god, I did it!*{/color}"
                    MC "{color=#808080}*I can't really feel it through these clothes tough...*{/color}"
                    scene EVENINGS44MOM25 with Dissolve(0.5)
                    McMom "{color=#808080}*Hmmm... something feels a bit weird..*{/color}"
                    McMom "{color=#808080}*My boob feels a bit itchy...*{/color}"
                    McMom "{color=#808080}*Wait... is he-*{/color}"
                    scene EVENINGS44MOM26 with Dissolve(0.5)
                    McMom "{color=#808080}*Oh my... he is!{/color}"
                    scene EVENINGS44MOM27 with Dissolve(0.5)
                    McMom "[MC_upper], WHAT DO YOU THINK YOU'RE DOING?!"
                    scene EVENINGS44MOM28 with Dissolve(0.5)
                    MC "{color=#808080}*Fuck... she caught me...*"
                    MC "What happened mom? Did I do something?"
                    scene EVENINGS44MOM27 with Dissolve(0.5)
                    McMom "You just grabbed my boob [MC], that's not normal!"
                    McMom "How could you do that?!!?"
                    scene EVENINGS44MOM28 with Dissolve(0.5)
                    MC "Oh my god, mom, I'm so sorry if that's what it looked like."
                    MC "I was trying to leave and when I pulled my hand back I must've accidentally touched you!"
                    MC "I'm sorry if it made you feed uncomfortable, I didn't mean to!"
                    scene EVENINGS44MOM27 with Dissolve(0.5)
                    McMom "You have to be more careful [MC]!"
                    McMom "These are not okay mistakes to do!"
                    McMom "I'm trying to finish the dinner, please leave!"
                    scene EVENINGS44MOM28 with Dissolve(0.5)
                    MC "Oh my god, mom, I'm so sorry if that's what it looked like."
                    scene EVENINGS44MOM14 with Dissolve(0.5)
                    McMom "......."
                    MC "{color=#808080}*She doesn't even wanna speak to me anymore...*{/color}"
                    MC "{color=#808080}*I messed up pretty bad...*{/color}"
                    scene BlackScreen
                    "{color=#808080}**You leave the room.**{/color}"
                    "{color=#808080}**Mom love - 5**{color=#808080}"
                    "{color=#808080}**Mom obedience - 5**{color=#808080}"
                    "{color=#808080}**Mom corruption + 2**{color=#808080}"
                    $ Mom_love = Mom_love - 5
                    $ Mom_Obedience = Mom_Obedience - 5
                    $ Mom_Corruption = Mom_Corruption + 2
                    $ check_and_update_character_stats("Mom")
                    $ Location = "Entrance"
                    $ advance_time_or_sleep()
                "Leave":
                    MC "Okay mom, I'll leave you to it. It already smells amazing!"
                    scene EVENINGS44MOM22 with Dissolve(0.5)
                    McMom "Awww thanks kiddo, you are so sweet."
                    McMom "Go sit at the table, the food it's almost done."
                    scene BlackScreen
                    "{color=#808080}**You leave the room.**{/color}"
                    "{color=#808080}**Mom love + 2**{color=#808080}"
                    $ Mom_love = Mom_love + 2
                    $ check_and_update_character_stats("Mom")
                    $ Location = "Entrance"
                    $ advance_time_or_sleep()
        "Leave":
            MC "{color=#808080}*Better not disturb her now, she seems focused..*{/color}"
            $ Location = "livingroom"
