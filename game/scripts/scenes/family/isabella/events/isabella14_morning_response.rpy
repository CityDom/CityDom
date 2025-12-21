label IsabellaMorning14:

    MC "Hey Isabella, good morning!!"
    scene Isabella_morning14_18 with Dissolve(0.5)
    Isabella "Hey [MC], Good morning!"
    Isabella "You usually don't wake up this early, what's up?"
    MC "Well, I thought...."
    scene Isabella_morning14_2 with Dissolve(0.5)
    Isabella "Don't stay there, come here!"
    scene Isabella_morning14_3 with Dissolve(0.5)
    Isabella "So... what's up?"
    scene Isabella_morning14_4 with Dissolve(0.5)
    MC "Nothing, I just wanted to see my little sister in the morning"
    scene Isabella_morning14_5 with Dissolve(0.5)
    Isabella "You are soooooo sweet [MC]"
    Isabella "Since you are here, I wanted to ask you..."
    scene Isabella_morning14_6 with Dissolve(0.5)
    MC "{color=#808080}*Isabella was always so touchy*{/color}"
    scene Isabella_morning14_7 with Dissolve(0.5)
    MC "{color=#808080}*Not that I mind, she got our mother tits*{/color}"
    Isabella "Ummm [MC], is not nice to look at your little sister tits you know?"
    scene Isabella_morning14_8 with Dissolve(0.5)
    MC "Sorry Isabella, you are so beautiful, sometimes my eyes just wonder away."
    Isabella "It's ok [MC], I heard boys your age are obsessed with tits."
    scene Isabella_morning14_7 with Dissolve(0.5)
    Isabella "But you are my brother, it's not ok to stare at my tits all the time........"
    MC "........................."
    Isabella "'playeeeeeeeeeeeer'"
    scene Isabella_morning14_9 with Dissolve(0.5)
    Isabella "....."
    Isabella "That's really not nice [MC] I wanted to tell you something that's been bothering me..."
    MC "Sorry Isabella, I'm listening, you have my full attention!"
    scene Isabella_morning14_10 with Dissolve(0.5)
    Isabella "Mhmmmmmmmm....."
    Isabella "Okay, but if I catch you again you are out!!"
    MC "Yes ma'am !!!"
    scene Isabella_morning14_8 with Dissolve(0.5)
    Isabella "Okay, so I wanted to tell you that lately I was a bit struggling at school."
    Isabella "And I wanted to ask you if you could help me."
    MC "Of course I will help you sis"
    menu:
        "Touch her tits":
            scene Isabella_morning14_12 with Dissolve(0.5)
            MC "{color=#808080}*I mean.. she's touching me in the same place...*{/color}"
            MC "{color=#808080}*And I'll take any chance I get to get close to touching those tits.*{/color}"
            MC "{color=#808080}*Since she's so touchy maybe she won't mind it.*{/color}"
            MC "I will do my best to make you the best student"
            MC "{color=#808080}*And the slutiest student too*{/color}"
            scene Isabella_morning14_13 with Dissolve(0.5)
            Isabella "Thanks a lot [MC] but uhhhhh...."
            scene Isabella_morning14_14 with Dissolve(0.5)
            Isabella "Can you please move you hand..."
            Isabella "You almost groped my full tit just now."
            scene Isabella_morning14_15 with Dissolve(0.5)
            MC "Oh my god, Isabella, I'm so sorry, I didn't realize"
            MC "You are so close and I think my hand slipped"
            scene Isabella_morning14_10 with Dissolve(0.5)
            Isabella "Mhmmmmmm...."
            Isabella "Whatever you say [MC]"
            Isabella "Now please go, I gotta go take a bath."
            MC "Sure sis, byeee!"
            Isabella "See you around [MC]!"
            call stat_reward({"Isabella": {"love": -5}}, return_to=None)
            $ Location = "Hallway"
            $ advance_time_or_sleep()
            # if (Isabella_love >= 20):
            #     scene Isabella_morning14_12 with Dissolve(0.5)
            #     MC "{color=#808080}*Looks like she's got used to it...*{/color}"
            #     MC "But... Even with my help you didn't manage to get your notes up?"
            #     Isabella "I did.. but I feel like I'm always distraced, and school get harder and harder"
            #     menu:
            #         "Go further":
            #             MC "{color=#808080}*Time to push my luck even further!*{/color}"
            #             scene Isabella_morning14_16 with Dissolve(0.5)
            #             MC "Then I will help you more and more Isabella, I promised you that you are going to be the best student and so you will be!!"
            #             if (Isabella_love < 40):
            #                 Isabella "Thanks a lot [MC] but.... uhhh..."
            #                 scene Isabella_morning14_17 with Dissolve(0.5)
            #                 Isabella "You are pushing your luck a bit too much don't you think?"
            #                 scene Isabella_morning14_15 with Dissolve(0.5)
            #                 Isabella "Thanks a lot for your help [MC], but I'm not comfortable with that."
            #                 MC "Sorry Sis, my hand must've sleep and...."
            #                 Isabella "Yeah yeah, it always slips I get it..."
            #                 Isabella "Now please leave, I gotta take a bath."
            #                 MC "Ok sis, byeee!!"
            #                 Isabella "Bye bye [MC]!!"
            #                 $ advance_time_or_sleep()
            #                 $ Isabella_love = Isabella_love - 5
            #                 $ Location = "Hallway"
            #             elif (Isabella_love >= 40):
            #                 Isabella "Thanks a lot [MC]!!!"
            #                 MC "{color=#808080}*Now she's not reacting even to that?*{/color}"
            #                 MC "{color=#808080}*This lesons we've been doing are working amazing!!*{/color}"
            #                 Isabella "Now let go of my boob and go pervert."
            #                 Isabella "I gotta take a bath!!"
            #                 MC "Okay, sis"
            #                 MC "Byee"
            #                 Isabella "See you around big bro!"
            #                 $ Isabella_love = Isabella_love + 2
            #                 $ Isabella_Corruption = Isabella_Corruption + 2
            #                 $ advance_time_or_sleep()
            #                 $ Location = "Hallway"
            #         "Leave":
            #             MC "Don't worry sis, I'll make sure to teach you even more!!"
            #             Isabella "Thanks a lot [MC]!!"
            #             Isabella "Now can you please leave?"
            #             Isabella "I gotta go take a bath."
            #             $ advance_time_or_sleep()
            #             $ Isabella_love = Isabella_love + 2
            #             $ Location = "Hallway"
        "Leave":
            Isabella "Thanks a lot [MC]!!"
            Isabella "Now can you please leave?"
            Isabella "I gotta go take a bath."
            call stat_reward({"Isabella": {"love": 2}}, return_to=None)
            $ Location = "Hallway"
            $ advance_time_or_sleep()





