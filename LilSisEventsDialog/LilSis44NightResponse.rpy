label LilSisNight44:

    scene NIGHT44LILSIS1 with Dissolve(0.5)
    MC "{color=#808080}*Isabella is on her phone, should I spend some time with her before she goes to sleep?*{/color}"
    menu:
        "Stay":
            scene NIGHT44LILSIS2 with Dissolve(0.5)
            MC "Hey sis, are you not sleepy yet?"
            scene NIGHT44LILSIS3 with Dissolve(0.5)
            Isabella "A little bit, I'm just checking out my socials."
            Isabella "I'll got to sleep shortly."
            scene NIGHT44LILSIS2 with Dissolve(0.5)
            MC "Is there something bothering you sis? "
            extend "You seem a little off."
            scene NIGHT44LILSIS4 with Dissolve(0.5)
            Isabella "Eh..."
            Isabella "Nothing important, I'm ok."
            scene NIGHT44LILSIS5 with Dissolve(0.5)
            MC "If it's making you sad it means important Isa."
            scene NIGHT44LILSIS4 with Dissolve(0.5)
            Isabella "For real, it's nothing important [MC], I'm fine."
            menu:
                "Insist":
                    # if (LilSis_Obedience >= 20 and LilSis_love >= 20):
                    #     scene NIGHT44LILSIS6 with Dissolve(0.5)
                    #     MC "I'm your big brother Isa. "
                    #     extend "You can tell me everything!"
                    #     scene NIGHT44LILSIS7 with Dissolve(0.5)
                    #     Isabella "I know... but there is nothing you can help with anyway."
                    #     scene NIGHT44LILSIS9 with Dissolve(0.5)
                    #     MC "Ok Isa, if you don't want to tell me then I'll leave you to it. "
                    #     extend "I thought you trusted me more than that..."
                    #     scene NIGHT44LILSIS10 with Dissolve(0.5)
                    #     Isabella "Ughhhhh!"
                    #     scene NIGHT44LILSIS11 with Dissolve(0.5)
                    #     Isabella "Okay, I will tell you, but take it serious or I'm never talking to you again!"
                    #     scene NIGHT44LILSIS12 with Dissolve(0.5)
                    #     MC "Of course sis, I promise! You can tell me everything."
                    #     scene NIGHT44LILSIS11 with Dissolve(0.5)
                    #     Isabella "I know... it's just hard. Sometimes, I feel like I don't measure up."
                    #     scene NIGHT44LILSIS12 with Dissolve(0.5)
                    #     MC "Why would you say that sis? In what way?"
                    #     scene NIGHT44LILSIS14 with Dissolve(0.5)
                    #     Isabella "I don't know, lately I've been so unconfortable with my body, I feel like I always look awful!"
                    #     scene NIGHT44LILSIS13 with Dissolve(0.5)
                    #     MC "Come on Isa... have you looked in a mirror latly? You look amazing! how could you say that?"
                    #     scene NIGHT44LILSIS14 with Dissolve(0.5)
                    #     Isabella "No I didn't... Each time I catch a glimpse of myself in the mirror I feel like crying. "
                    #     extend "Now I feel anxious to go outside or or even show my face at school."
                    #     scene NIGHT44LILSIS13 with Dissolve(0.5)
                    #     MC "I don't know where you got that ideea from sis, you are one of the best looking girl I know."
                    #     scene NIGHT44LILSIS14 with Dissolve(0.5) 
                    #     Isabella "Yeah.. because you don't know any... "
                    #     extend "All these girls that I follow on social media look completly amazing! "
                    #     extend "I feel like a fat pig compared to them!"
                    #     scene NIGHT44LILSIS15 with Dissolve(0.5)
                    #     Isabella "And I'm trying so hard to lose weight. I don't know what to do anymore."
                    #     Isabella "Every day I feel sick from not eating and I'm still not losing any weight."
                    #     Isabella "{color=#808080}**...sniff...sniff...**{/color}"
                    #     scene NIGHT44LILSIS15 with Dissolve(0.5)
                    #     Isabella "I don't know what to do anymore...."
                    #     Isabella "I feel like everything is going awful!"
                    #     scene NIGHT44LILSIS16 with Dissolve(0.5)
                    #     MC "I'm so sorry you feel like that Isa, I had no ideea. "
                    #     extend "Thank you for telling me."
                    #     scene NIGHT44LILSIS17 with Dissolve(0.5)
                    #     MC "But let me tell you, you have nothing to worry about."
                    #     MC "You are the best looking girl I know, even better then most of the models you see on social media."
                    #     scene NIGHT44LILSIS18 with Dissolve(0.5)
                    #     Isabella "{color=#808080}**...sniff...sniff...**{/color}"
                    #     Isabella "I know you are saying that just to make me feel better [MC], but I know it's not true."
                    #     Isabella "You don't even believe yourself."
                    #     scene NIGHT44LILSIS20 with Dissolve(0.5)
                    #     MC "Isabella! listen to me!"
                    #     MC "I've been watching these bitches on social media since I first had internet."
                    #     MC "Those are just pictures, with the right angles and lighting you would look ten times better than them!"
                    #     scene NIGHT44LILSIS19 with Dissolve(0.5)
                    #     Isabella "Wh.. what do you mean?"
                    #     scene NIGHT44LILSIS20 with Dissolve(0.5)
                    #     MC "I can take pictures of you in which you would look a hundred times better then them!"
                    #     menu:
                    #         "Take photos":
                    #             MC "Let me show you, stand up."
                    #             scene NIGHT44LILSIS21 with Dissolve(0.5)
                    #             Isabella "Thank you [MC], but I'm not in the mood for taking photos. "
                    #             extend "I look awful."
                    #             scene NIGHT44LILSIS22 with Dissolve(0.5)
                    #             MC "Ok sis, I hope you feel a little better."
                    #             MC "Stop doubting yourself, be more prideful with how you look."
                    #             MC "You have an amazing body."
                    #             scene NIGHT44LILSIS23 with Dissolve(0.5)
                    #             Isabella "Ok bro, I'm your little sister, I don't need to hear that from you."
                    #             Isabella "I feel a little better now, you can leave."
                    #             extend "I wanna go to sleep."
                    #             scene NIGHT44LILSIS24 with Dissolve(0.5)
                    #             MC "Ok Isa, have a good sleep!"
                    #             scene NIGHT44LILSIS23 with Dissolve(0.5)
                    #             Isabella "Thank you bro, good night!"
                    #             scene BlackScreen with Dissolve(0.5)
                    #             "{color=#808080}**You leave the room.**{/color}"
                    #             $ LilSis_Corruption = LilSis_Corruption - 2
                    #             $ LilSis_Obedience = LilSis_Obedience - 2 
                    #             $ LilSis_love = LilSis_love - 2
                    #             $ Location = "Hallway"
                    #             $ advance_time_or_sleep()
                    #         "Leave":
                    #             MC "But for now I'll let you sleep. Just know that you look way better than those bitches."
                    #             scene NIGHT44LILSIS26 with Dissolve(0.5)
                    #             Isabella "......"
                    #             scene NIGHT44LILSIS27 with Dissolve(0.5)
                    #             Isabella "Wait! [MC]..."
                    #             scene NIGHT44LILSIS28 with Dissolve(0.5)
                    #             MC "Is there something el-"
                    #             scene NIGHT44LILSIS30 with Dissolve(0.5)
                    #             "........................."
                    #             scene NIGHT44LILSIS29 with Dissolve(0.5)
                    #             Isabella "Thank you "
                    #             MC "{color=#808080}*I can only think about her tits pressing on my chest.*{/color}"
                    #             MC "{color=#808080}*If she feels me getting hard now I'm gonna be in so much trouble*{/color}"
                    #             MC "{color=#808080}*I gotta leave*{/color}"
                    #             scene NIGHT44LILSIS34 with Dissolve(0.5)
                    #             MC "No problem sis, thank you for trusting me enough to talk to me about your problems."
                    #             MC "I'll let you sleep now, try to think about what I told you"
                    #             scene NIGHT44LILSIS33 with Dissolve(0.5)
                    #             Isabella "Yea, I will think about it."
                    #             MC "Ok sis, have a good night."
                    #             Isabella "Good night."
                    #             scene BlackScreen with Dissolve(0.5)
                    #             "{color=#808080}**You leave the room.**{/color}"
                    #             $ LilSis_love = LilSis_love + 2
                    #             $ LilSis_Obedience = LilSis_Obedience + 2
                    #             $ LilSis_Corruption = LilSis_Corruption + 2
                    #             $ Location = "Hallway"
                    #             $ advance_time_or_sleep()
                                
                    # else:
                    scene NIGHT44LILSIS6 with Dissolve(0.5)
                    MC "I'm your big brother Isa. "
                    extend "You can tell me everything!"
                    scene NIGHT44LILSIS7 with Dissolve(0.5)
                    Isabella "It's late [MC], thank you for caring, but I'm not really in the mood to talk right now."
                    scene NIGHT44LILSIS6 with Dissolve(0.5)
                    MC "Ok Isa, if there's ever a problem tell me."
                    scene NIGHT44LILSIS7 with Dissolve(0.5) 
                    Isabella "Yea, yeah..."
                    scene BlackScreen with Dissolve(0.5)
                    "{color=#808080}**Isabella love + 2**{color=#808080}"
                    "{color=#808080}**Isabella obedience + 2**{color=#808080}"
                    "{color=#808080}**You leave the room.**{/color}"
                    $ LilSis_love = LilSis_love + 2
                    $ LilSis_Obedience = LilSis_Obedience + 2
                    $ check_and_update_character_stats("LilSis")
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
                "Leave":
                    scene NIGHT44LILSIS6 with Dissolve(0.5)
                    MC "Okay, sis I won't bother you anymore, just know that you can tell me any problem you have."
                    Isabella "I know, I know."
                    scene BlackScreen with Dissolve(0.5)
                    "{color=#808080}**Isabella love + 2**{color=#808080}"
                    $ LilSis_love = LilSis_love + 2
                    $ check_and_update_character_stats("LilSis")
                    "{color=#808080}**You leave the room.**{/color}"
                    $ Location = "Hallway"
                    $ advance_time_or_sleep()
        "Leave":
            MC "{color=#808080}*Maybe she would like to be alone.*{/color}"
            "{color=#808080}**You leave the room.**{/color}"
            $ Location = "Hallway"
            $ renpy.call("GameLoop")
        