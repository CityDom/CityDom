init python:
    define_images("GymClass_Tanya", "GymClass/GymClass_Tanya", "GymClass_Tanya", 74)

label GymClass_Tanya:
    scene GymClass_Tanya1 with Dissolve(0.5)
    Tanya "Hey, shrimp! What's up? What do you want?"
    scene GymClass_Tanya2 with Dissolve(0.5)
    MC "Hey, Tanya. Nothing much, just waiting for class to start."
    scene GymClass_Tanya3 with Dissolve(0.5)
    Tanya "Drop the Tanya! I'm Miss White in here!"
    Tanya "Now tell me, what do you want? You don't usually talk to me."
    jump TanyaGymMenu

label TanyaGymMenu:
    scene GymClass_Tanya4 with Dissolve(0.5)
    menu:
        "What do you think about me?":
            if not Watched_GymClass_Tanya_WDYTAM:
                $ Watched_GymClass_Tanya_WDYTAM = True
                MC "I was just curious, what do you think about me?"
                scene GymClass_Tanya5 with Dissolve(0.5)
                Tanya "Haha, since when do you care what other people think?!"
                Tanya "It's not a healthy thing!"
                Tanya "But, you are my annoying and perverted little cousin!"
                Tanya "You've grown quite a bit, but you have a long way to go if you want to stop me from giving you noogies!"
                scene GymClass_Tanya5 with Dissolve(0.5)
                Tanya "Is that all you wanted to know?"
                scene GymClass_Tanya4 with Dissolve(0.5)
            else:
                MC "{color=#808080}*I already talked to her about that.*{/color}"
            jump TanyaGymMenu
        
        "Compliment":
            if not Watched_GymClass_Tanya_Compliment:
                $ Watched_GymClass_Tanya_Compliment = True
                MC "I wanted to tell you that you look good in that tracksuit."
                MC "You can barely keep up the tomboy appearance anymore!"
                scene GymClass_Tanya7 with Dissolve(0.5)
                Tanya "I'm still your teacher in here, Shrimp!"
                Tanya "The other girls might think you're trying to flatter me for a better grade!"
                scene GymClass_Tanya8 with Dissolve(0.5)
                MC "But is it working?"
                scene GymClass_Tanya9 with Dissolve(0.5)
                Tanya "Haha, miles away from working!"
                Tanya "Now tell me what you really want. You're never nice just to be nice!"
                call stat_reward({"Tanya": {"love": 2}}, show_black=False, return_to=None)
            else:
                MC "{color=#808080}*I already talked to her about that.*{/color}"
            jump TanyaGymMenu
        
        "Pervert compliment":
            if not Watched_GymClass_Tanya_PervertCompliment:
                $ Watched_GymClass_Tanya_PervertCompliment = True
                MC "Do you really have to wear that tracksuit?"
                MC "It's a real waste, you're way too hot for that!"
                scene GymClass_Tanya10 with Dissolve(0.5)
                Tanya "I am your teacher, shrimp! Even if I wasn't, you don't talk like that to your cousin!"
                Tanya "It shows that you lived with that jerk. I hope Jennifer taught you better."
                Tanya "I hope you're not talking to the other teachers like that!"
                Tanya "Now get lost before I smack you!"
                call stat_reward({"Tanya": {"love": -2, "corruption": 2}}, show_black=False, return_to=None)
            else:
                MC "{color=#808080}*I already talked to her about that.*{/color}"
            jump TanyaGymMenu
        
        "Insult":
            if not Watched_GymClass_Tanya_Insult:
                $ Watched_GymClass_Tanya_Insult = True
                MC "It's really annoying when you keep yelling. You should stop."
                MC "It just makes you look like the annoying teacher type."
                scene GymClass_Tanya11 with Dissolve(0.5)
                Tanya "You better get lost before I smack you in front of the class!"
                call stat_reward({"Tanya": {"love": -2, "corruption": -2}}, return_to=None)
            else:
                MC "{color=#808080}*I already talked to her about that.*{/color}"
            jump TanyaGymMenu
        
        "Leave":
            MC "Actually, I have to do something before class starts."
            MC "I don't want to be late and make Miss White angry!"
            scene GymClass_Tanya5 with Dissolve(0.5)
            Tanya "Yeah, you better not!"
            $ renpy.call("GameLoop")
