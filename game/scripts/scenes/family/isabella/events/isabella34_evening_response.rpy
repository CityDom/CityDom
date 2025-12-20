label IsabellaEvening34:

    scene Isabella_evening34_1 with Dissolve(0.5)
    MC "{color=#808080}*Isa is here, should I hang out with her?*{color=#808080}"
    menu:
        "Stay":
            MC "Hey sis, what are you doing?"
            scene Isabella_evening34_2 with Dissolve(0.5)
            Isabella "Kyaaaa!!"
            scene Isabella_evening34_3 with Dissolve(0.5)
            Isabella "Oh my god, [MC], you scared me!"
            scene Isabella_evening34_2 with Dissolve(0.5)
            MC "Don't you think you get scared too easily?"
            scene Isabella_evening34_4 with Dissolve(0.5)
            Isabella "Yeah... that might be true..."
            Isabella "But you should stop sneaking around so often!"
            scene Isabella_evening34_5 with Dissolve(0.5)
            Isabella "So, in any case, what do you want?"
            scene Isabella_evening34_6 with Dissolve(0.5)
            MC "Can't I just spend some time with my little sister?"
            MC "You used to want to play with me all the time when you were little!"
            scene Isabella_evening34_5 with Dissolve(0.5)
            Isabella "Yeah, well... I'm not little anymore."
            Isabella "And since when do you just feel like spending time with me?"
            scene Isabella_evening34_6 with Dissolve(0.5)
            MC "What do you mean, sis? I've always wanted to spend time with you."
            scene Isabella_evening34_7 with Dissolve(0.5)
            Isabella "Just tell me what you want already, or leave."
            label choisesmenuisabella34evening:
                scene Isabella_evening34_8 with Dissolve(0.5)
                menu:
                    "How do you feel about us?":
                        scene Isabella_evening34_8 with Dissolve(0.5)
                        MC "I just wanted to ask you how you feel about our relationship."
                        scene Isabella_evening34_7 with Dissolve(0.5)
                        Isabella "Ughhhh... what kind of question is that, you are my big annoying brother."
                        Isabella "And I'm your cute, nice and perfect in all kinds of way little sister, is there something else to it?"
                        jump choisesmenuisabella34evening
                    "Compliment":
                        scene Isabella_evening34_8 with Dissolve(0.5)
                        MC "I just wanted to say that you look really good today."
                        scene Isabella_evening34_10 with Dissolve(0.5)
                        Isabella "Awww that's really sweet [MC]!"
                        Isabella "But that's not something that I want to hear coming from you."
                        scene Isabella_evening34_9 with Dissolve(0.5)
                        MC "Come on, sis, can't you just take the compliment?"
                        scene Isabella_evening34_10 with Dissolve(0.5)
                        Isabella "I'm just fucking with you, thank you for the compliment, I appreciate it."
                        Isabella "Now get out, I have to prepare for school"
                        scene Isabella_evening34_9 with Dissolve(0.5)
                        MC "Ok sis, see you around then."
                        "{color=#808080}**You leave the room**{color=#808080}"
                        "{color=#808080}**Isabella love + 2**{color=#808080}"
                        $ Isabella_love = Isabella_love + 2
                        $ check_and_update_character_stats("Isabella")
                        $ Location = "Hallway"
                        $ advance_time_or_sleep()
                    "Touch":
                        menu:
                            "Hug":
                                MC "I just came in to give you a hug, why do you have to be so mean?"
                                scene Isabella_evening34_11 with Dissolve(0.5)
                                Isabella "Ughhhh... seriously?"
                                scene Isabella_evening34_12 with Dissolve(0.5)
                                MC "Is it too much to ask from my little sister?"
                                scene Isabella_evening34_11 with Dissolve(0.5)
                                Isabella "Okay, just get it over with, I have to pack my bag for tomorrow."
                                scene Isabella_evening34_13 with Dissolve(0.5)
                                MC "{color=#808080}*Her tits are pressing against my chest*{color=#808080}"
                                MC "{color=#808080}*They are so soft and big. {color=#808080}"
                                extend "{color=#808080}I could stay like this forever.*{color=#808080}"
                                MC "{color=#808080}*Should I try out my luck?*{color=#808080}"
                                menu: 
                                    "Grab her ass":
                                        scene Isabella_evening34_15 with Dissolve(0.5)
                                        MC "{color=#808080}*Fuck it, it's worth whatever happens next.*{color=#808080}"
                                        scene Isabella_evening34_14 with Dissolve(0.5)
                                        Isabella "Ummmm.... Can you let me go now, it's getting awkward..."
                                        scene Isabella_evening34_18 with Dissolve(0.5)
                                        Isabella "{color=#808080}*Ughhhh, what the fuck... {color=#808080}"
                                        extend "{color=#808080}is he grabbing my ass?*{color=#808080}"
                                        scene Isabella_evening34_17 with Dissolve(0.5)
                                        Isabella "WHAT THE FUCK ARE YOU DOING??!?!?!?"
                                        scene Isabella_evening34_19 with Dissolve(0.5)
                                        MC "Oh my god, Isa, I'm so sorry, my hand slipped."
                                        scene Isabella_evening34_16 with Dissolve(0.5)
                                        Isabella "Your hand always slips, right?!"
                                        Isabella "Get the fuck out right now or I will scream for mom!"
                                        "{color=#808080}**You quickly leave the room**{color=#808080}"
                                        "{color=#808080}**Isabella corruption + 2**{color=#808080}"
                                        "{color=#808080}**Isabella love - 5**{color=#808080}"
                                        $ Isabella_love = Isabella_love - 5
                                        $ Isabella_Corruption = Isabella_Corruption + 2
                                        $ check_and_update_character_stats("Isabella")
                                        $ Location = "Hallway"
                                        $ advance_time_or_sleep()
                                    "Just hug her":
                                        Isabella "......."
                                        scene Isabella_evening34_14 with Dissolve(0.5)
                                        Isabella "Ummm... can you let me go now? You smell!"
                                        scene Isabella_evening34_23 with Dissolve(0.5)
                                        MC "No way I smell, I shower every chance I get."
                                        scene Isabella_evening34_21 with Dissolve(0.5)
                                        Isabella "Yeah, I'm just fucking with you. "
                                        extend "You are not the worst thing I've ever smelled, I guess."
                                        scene Isabella_evening34_22 with Dissolve(0.5)
                                        MC "Wow, what a compliment... I guess..."
                                        scene Isabella_evening34_20 with Dissolve(0.5)
                                        Isabella "Okay, now get out, I have to get ready for tomorrow."
                                        "{color=#808080}**You leave the room**{color=#808080}"
                                        "{color=#808080}**Isabella love + 2**{color=#808080}"
                                        "{color=#808080}**Isabella obedience + 2**{color=#808080}"
                                        $ Isabella_love = Isabella_love + 2
                                        $ Isabella_Obedience = Isabella_Obedience + 2
                                        $ check_and_update_character_stats("Isabella")
                                        $ Location = "Hallway"
                                        $ advance_time_or_sleep()
        "Leave":
            MC "{color=#808080}*Maybe some other time.*{color=#808080}"
            "{color=#808080}**You leave the room.**{color=#808080}"
            $ Location = "Isabella room"
            $ renpy.call("GameLoop")
