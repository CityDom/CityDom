label JenniferEvening44:
    scene Jennifer_evening44_0
    MC "Oh, mom is cooking dinner."
    menu:
        "Talk":
            scene Jennifer_evening44_1 with Dissolve(0.5)
            MC "Hey mom, how are you?"
            scene Jennifer_evening44_14 with Dissolve(0.5)
            Jennifer "Sorry, I can't talk right now, I need to focus."
            scene Jennifer_evening44_1 with Dissolve(0.5)
            MC "Can I help you?"
            scene Jennifer_evening44_14 with Dissolve(0.5)
            Jennifer "You are sweet kiddo, but I don't think you can help me here."
            Jennifer "I'm cooking something more complicated and you would just get in the way."
            scene Jennifer_evening44_1 with Dissolve(0.5)
            MC "{color=#808080}*... you could've said that more nicely..*{/color}"
            MC "Okay mom, can't wait to see what you're cooking!"
            scene Jennifer_evening44_14 with Dissolve(0.5)
            Jennifer "It will be done soon, go sit at the table."
            $ Location = "livingroom"
        "Hug":
            scene Jennifer_evening44_15 with Dissolve(0.5)
            MC "Aaaand.."
            scene Jennifer_evening44_16 with Dissolve(0.5)
            MC "Surpriseee!!!"
            Jennifer "AAAAAAAAAAAAA"
            scene Jennifer_evening44_17 with Dissolve(0.5)
            Jennifer "Oh my goodness, [MC], you really startled me there!"
            Jennifer "Don't ever do that again!"
            scene Jennifer_evening44_18 with Dissolve(0.5)
            MC "Ok, mom, I'm sorry, I'll never hug you again. I understand..."
            scene Jennifer_evening44_17 with Dissolve(0.5)
            Jennifer "Oh, c'mon, [MC], you know I didn't mean it like that."
            Jennifer "I really appreciate you hugging me."
            scene Jennifer_evening44_19 with Dissolve(0.5)
            Jennifer "So tell me, What do you want?"
            scene Jennifer_evening44_20 with Dissolve(0.5)
            MC "You keep saying that I wan't something from you!"
            MC "Can't I love my mom just because?"
            scene Jennifer_evening44_21 with Dissolve(0.5)
            Jennifer "So you just got really lovey dovey all of the sudden, huh?"
            scene Jennifer_evening44_20 with Dissolve(0.5)
            MC "Well... being away all this time does that to you."
            scene Jennifer_evening44_21 with Dissolve(0.5)
            Jennifer "I guess you're right..."
            Jennifer "And I love you too, kiddo."
            Jennifer "But are you going to be clinging on me all night?"
            Jennifer "I really have to get dinner ready."
            scene Jennifer_evening44_20 with Dissolve(0.5)
            MC "Just a little bit more!"
            scene Jennifer_evening44_22 with Dissolve(0.5)
            Jennifer "Okay, but don't cry when some hot oil jumps on your hands"
            scene Jennifer_evening44_23 with Dissolve(0.5)
            MC "{color=#808080}*Her ass is pressing right onto my dick...*{/color}"
            MC "{color=#808080}*Is almost like she's doing it on purpose!*{/color}"
            MC "{color=#808080}*But I'm getting really hard, and if she finds out I'm dead!*{/color}"
            MC "{color=#808080}*Maybe I should leave...*{/color}"
            MC "{color=#808080}*But It feels so good... and I don't know if I'll ever get into a position like that with her...*{/color}"
            menu:
                "Grab her boobs":
                    MC "{color=#808080}*I'll just loosely lay my hand on her tit, maybe she won't feel it...*{/color}"
                    MC "{color=#808080}*I'm so nervous...*{/color}"
                    scene Jennifer_evening44_24 with Dissolve(0.5)
                    MC "{color=#808080}*Oh my god, I did it!*{/color}"
                    MC "{color=#808080}*I can't really feel it through these clothes tough...*{/color}"
                    scene Jennifer_evening44_25 with Dissolve(0.5)
                    Jennifer "{color=#808080}*Hmmm... something feels a bit weird..*{/color}"
                    Jennifer "{color=#808080}*My boob feels a bit itchy...*{/color}"
                    Jennifer "{color=#808080}*Wait... is he-*{/color}"
                    scene Jennifer_evening44_26 with Dissolve(0.5)
                    Jennifer "{color=#808080}*Oh my... he is!{/color}"
                    scene Jennifer_evening44_27 with Dissolve(0.5)
                    Jennifer "[MC_upper], WHAT DO YOU THINK YOU'RE DOING?!"
                    scene Jennifer_evening44_28 with Dissolve(0.5)
                    MC "{color=#808080}*Fuck... she caught me...*"
                    MC "What happened mom? Did I do something?"
                    scene Jennifer_evening44_27 with Dissolve(0.5)
                    Jennifer "You just grabbed my boob [MC], that's not normal!"
                    Jennifer "How could you do that?!!?"
                    scene Jennifer_evening44_28 with Dissolve(0.5)
                    MC "Oh my god, mom, I'm so sorry if that's what it looked like."
                    MC "I was trying to leave and when I pulled my hand back I must've accidentally touched you!"
                    MC "I'm sorry if it made you feed uncomfortable, I didn't mean to!"
                    scene Jennifer_evening44_27 with Dissolve(0.5)
                    Jennifer "You have to be more careful [MC]!"
                    Jennifer "These are not okay mistakes to do!"
                    Jennifer "I'm trying to finish the dinner, please leave!"
                    scene Jennifer_evening44_28 with Dissolve(0.5)
                    MC "Oh my god, mom, I'm so sorry if that's what it looked like."
                    scene Jennifer_evening44_14 with Dissolve(0.5)
                    Jennifer "......."
                    MC "{color=#808080}*She doesn't even wanna speak to me anymore...*{/color}"
                    MC "{color=#808080}*I messed up pretty bad...*{/color}"
                    scene BlackScreen
                    "{color=#808080}**You leave the room.**{/color}"
                    call stat_reward({"Jennifer": {"love": -5, "corruption": 2, "obedience": -5}}, show_black=False, return_to=None)
                    $ Location = "Entrance"
                    $ advance_time_or_sleep()
                "Leave":
                    MC "Okay mom, I'll leave you to it. It already smells amazing!"
                    scene Jennifer_evening44_22 with Dissolve(0.5)
                    Jennifer "Awww thanks kiddo, you are so sweet."
                    Jennifer "Go sit at the table, the food it's almost done."
                    scene BlackScreen
                    "{color=#808080}**You leave the room.**{/color}"
                    call stat_reward({"Jennifer": {"love": 2}}, show_black=False, return_to=None)
                    $ Location = "Entrance"
                    $ advance_time_or_sleep()
        "Leave":
            MC "{color=#808080}*Better not disturb her now, she seems focused..*{/color}"
            $ Location = "livingroom"
            $ renpy.call("GameLoop")
