label LilsisAfterNoon44:
    scene AFTERNOON44LILSIS1 with Dissolve(0.5)
    MC "{color=#808080}*Oh, Isabella is still awake, should I go talk to her?*{/color}"
    menu: 
        "Talk to Isabella":
            MC "Hey sis, what are you doing?"
            scene AFTERNOON44LILSIS2 with Dissolve(0.5)
            Isabella "Oh hey bro."
            Isabella "I'm trying to install this stupid game."
            Isabella "I've been trying for like an hour, I can't get this thing to work!"
            scene AFTERNOON44LILSIS4 with Dissolve(0.5)
            MC "Try not to get 20 viruses again."
            MC "And then come to me crying that somebody hacked your computer"
            Isabella "Come on, why are you so mean, I only did that once or twice."
            MC "Yea, more like 10 or 20 times."
            scene AFTERNOON44LILSIS3 with Dissolve(0.5)
            Isabella "Well, you know, if you'd actually help me from time to time that wouldn't be a problem."
            scene AFTERNOON44LILSIS5 with Dissolve(0.5)
            MC "....."
            MC "I don't know sis... I wanted to go to sleep, maybe tomorrow..."
            scene AFTERNOON44LILSIS7 with Dissolve(0.5)
            Isabella "Please?"
            scene AFTERNOON44LILSIS6 with Dissolve(0.5)
            MC "....."
            scene AFTERNOON44LILSIS7 with Dissolve(0.5)
            Isabella "Pleaaaase?"
            scene AFTERNOON44LILSIS6 with Dissolve(0.5)
            MC "Just wait until tomorrow sis, I'm waking up early."
            scene AFTERNOON44LILSIS7 with Dissolve(0.5)
            Isabella "Pleaaaaaaaaaaaseeee!!!"
            Isabella "PLEASE PLEASE PLEASE PLEASE PLEASE PLEASE!!!!"
            scene AFTERNOON44LILSIS6 with Dissolve(0.5)
            MC "I don't know sis, you have to learn to ask more nicely."
            MC "Saying please over and over ain't gonna cut it"
            scene AFTERNOON44LILSIS7 with Dissolve(0.5)
            Isabella "Oh come on, what do you want me to do?"
            menu:
                "Be understanding":
                    scene AFTERNOON44LILSIS6 with Dissolve(0.5)
                    MC "Eh.."
                    MC "I guess a pretty please would sufice for now."
                    scene AFTERNOON44LILSIS7 with Dissolve(0.5)
                    Isabella "Pretty pelaaaase??"
                    scene AFTERNOON44LILSIS6 with Dissolve(0.5)
                    MC "Okay, move over, let me see."
                    scene AFTERNOON44LILSIS8 with Dissolve(0.5)
                    Isabella "Thank youuu!!!"
                    scene AFTERNOON44LILSIS9 with Dissolve(0.5)
                    MC "Okay, so what game do you want to download?"
                    jump getGame
                "Ask her to beg":
                    scene AFTERNOON44LILSIS6 with Dissolve(0.5)
                    MC "You have to learn to beg if you really want something."
                    scene AFTERNOON44LILSIS3 with Dissolve(0.5)
                    Isabella "Are you for real?"
                    Isabella "What are you, a kid?"
                    scene AFTERNOON44LILSIS5 with Dissolve(0.5)
                    MC "There is nothing wrong in begging for something Isa."
                    MC "Trust your big brother."
                    scene AFTERNOON44LILSIS6 with Dissolve(0.5)
                    Isabella "Ummm... sure... if you say so."
                    scene AFTERNOON44LILSIS25 with Dissolve(0.5)
                    Isabella "Will you help me? pleaaaaase!"
                    menu:
                        "That's enough":
                            MC "Okay, I will help you."
                            scene AFTERNOON44LILSIS26 with Dissolve(0.5)
                            Isabella "Really? It was that easy?"
                            scene AFTERNOON44LILSIS25 with Dissolve(0.5)
                            MC "Yea, if you beg for it correctly, you get what you want!"
                            scene AFTERNOON44LILSIS26 with Dissolve(0.5)
                            Isabella "I didn't know that, thank you for teaching me!"
                            scene AFTERNOON44LILSIS25 with Dissolve(0.5)
                            MC "No problem sis, now show me what game do you want."
                            "{color=#808080}**Isabella love + 2**{color=#808080}"
                            "{color=#808080}**Isabella obedience + 2**{color=#808080}"
                            "{color=#808080}**Isabella corruption + 2**{color=#808080}"
                            $ LilSis_love = LilSis_love + 2
                            $ LilSis_Obedience = LilSis_Obedience + 2
                            $ LilSis_Corruption = LilSis_Corruption + 2
                            $ check_and_update_character_stats("LilSis")
                            jump getGame
                        "Ask for more":
                            MC "Hmmm..."
                            MC "I'm afraid that is still not enough..."
                            MC "You have to get on your knees."
                            scene AFTERNOON44LILSIS28 with Dissolve(0.5)
                            Isabella "That's too far [MC]! "
                            extend "I'm not getting on my knees for you. "
                            extend "Even the thought of that makes me sick."
                            scene AFTERNOON44LILSIS27 with Dissolve(0.5)
                            MC "You don't have to think of it like that sis. "
                            extend "It's something completely normal."
                            MC "There is nothing sexual about it. "
                            extend "You do that when you really want something."
                            scene AFTERNOON44LILSIS28 with Dissolve(0.5)
                            Isabella "Yea, no thank you, it doesn't matter how much I want it!"
                            Isabella "Mom told me to not embarrass myself in front of nobody. "
                            extend "So no, I'm not doing that."
                            scene AFTERNOON44LILSIS27 with Dissolve(0.5)
                            MC "That's not true, Isa, there is nothing embarrassing about it!"
                            Isabella "For me it is! "
                            extend "So you can leave now. "
                            extend "Thank you for nothing!"
                            "{color=#808080}**You leave the room, Isabella is mad at you.**{/color}"
                            "{color=#808080}**Isabella love - 5**{color=#808080}"
                            "{color=#808080}**Isabella obedience - 2**{color=#808080}"
                            "{color=#808080}**Isabella corruption + 2**{color=#808080}"
                            $ LilSis_love = LilSis_love - 5
                            $ LilSis_Obedience = LilSis_Obedience - 2
                            $ LilSis_Corruption = LilSis_Corruption + 2
                            $ check_and_update_character_stats("LilSis")
                            $ Location = "Hallway"
                            $ advance_time_or_sleep()
        "Leave":
            MC "{color=#808080}*Maybe not right now*{/color}"
            "{color=#808080}**You leave the room.**{/color}"
            $ Location = "Hallway"
            $ renpy.call("GameLoop")
            return

label getGame:
    scene AFTERNOON44LILSIS10 with Dissolve(0.5)
    Isabella "It's called 'Battle of gods'..."
    Isabella "Have you heard of it?"
    scene AFTERNOON44LILSIS9 with Dissolve(0.5)
    MC "Nope..."
    MC "But let me check..."
    scene AFTERNOON44LILSIS11 with Dissolve(0.5)
    "...."
    ".........."
    "................."
    scene AFTERNOON44LILSIS9 with Dissolve(0.5)
    MC "Um... Isabella?"
    scene AFTERNOON44LILSIS13 with Dissolve(0.5)
    Isabella "yea?"
    scene AFTERNOON44LILSIS14 with Dissolve(0.5)
    MC "This game costs 60 dollars..."
    MC "Are you sure you want to get this game?"
    scene AFTERNOON44LILSIS13 with Dissolve(0.5)
    Isabella "60 dollars... fuuuck..."
    Isabella "Can't you just get it for free?"
    scene AFTERNOON44LILSIS14 with Dissolve(0.5)
    MC "I mean... I can pirate it..."
    MC "But it's going to take a lot of time to find a good website to pirate it from."
    MC "And as I told you before, I don't got that much time right now, no matter how much you beg for it."
    scene AFTERNOON44LILSIS12 with Dissolve(0.5)
    MC "{color=#808080}*I think I can take advantage of this situation*{/color}"
    scene AFTERNOON44LILSIS13 with Dissolve(0.5)
    Isabella "Come on, I'll do anything!"
    MC "{color=#808080}*Perfect, now what should I make her do?*{/color}"
    menu:
        "Just help her":
            scene AFTERNOON44LILSIS12 with Dissolve(0.5)
            MC "Maybe you can just return the favor some other time..."
            scene AFTERNOON44LILSIS15 with Dissolve(0.5)
            Isabella "Yaaaaay, sure, thank you!"
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**After 30 minutes you finish installing the game and leave.**{/color}"
            "{color=#808080}**Isabella love + 2**{color=#808080}"
            $ LilSis_love = LilSis_love + 2
            $ check_and_update_character_stats("LilSis")
            $ Location = "Hallway"
            $ advance_time_or_sleep()
            # TODO sa adaug scene cu MC ul in care sa o puna sa ii multumeasca si sa o invete cum, sa scoata limba etc
        "Show me your tits":
            scene AFTERNOON44LILSIS16 with Dissolve(0.5)
            MC "You will do 'Anything'?"
            scene AFTERNOON44LILSIS17 with Dissolve(0.5)
            Isabella "Yea, come on just tell me, what do you want?"
            Isabella "I will do the dishes when is your turn."
            scene AFTERNOON44LILSIS16 with Dissolve(0.5)
            MC "I'm afraid that is not going to cut it this time."
            MC "You are going to have to do some more."
            scene AFTERNOON44LILSIS17 with Dissolve(0.5)
            Isabella "You want me to clean your room?"
            Isabella "Come on, it's going to take me a whole day."
            scene AFTERNOON44LILSIS16 with Dissolve(0.5)
            MC "It's okay, you don't have to clean my room."
            MC "It's actually a lot easier than that. "
            extend "And it will only take a couple of seconds."
            scene AFTERNOON44LILSIS19 with Dissolve(0.5)
            Isabella "Really? What is it?"
            scene AFTERNOON44LILSIS20 with Dissolve(0.5)
            MC "You just have to lift up your shirt?"
            scene AFTERNOON44LILSIS21 with Dissolve(0.5)
            Isabella "You are not funny [MC], now tell me what you want."
            scene AFTERNOON44LILSIS22 with Dissolve(0.5)
            MC "I just told you what I want."
            scene AFTERNOON44LILSIS23 with Dissolve(0.5)
            Isabella "I'm not going to do that [MC]!!"
            Isabella "How could you ask me that?!?! "
            extend "I'm your sister!"
            scene AFTERNOON44LILSIS24 with Dissolve(0.5)
            MC "Come on sis, I used to see them all the time back in the day."
            MC "What would be the difference now?"
            scene AFTERNOON44LILSIS23 with Dissolve(0.5)
            Isabella "There is a big difference! "
            extend "I have breasts now. "
            extend "Mom said to not be naked around you now that I'm grown!"
            scene AFTERNOON44LILSIS24 with Dissolve(0.5)
            MC "There shouldn't be anything wrong or weird in doing that."
            MC "You are my little sister, you don't have to be shy around me."
            scene AFTERNOON44LILSIS23 with Dissolve(0.5)
            Isabella "Absolutely not [MC], I will get the game myself if this is what you want!"
            scene AFTERNOON44LILSIS24 with Dissolve(0.5)
            MC "Okay, then, good luck getting that game."
            MC "Goodnight!"
            scene AFTERNOON44LILSIS23 with Dissolve(0.5)
            Isabella "Yea, thanks for nothing, get out!"
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**You leave the room, Isabella is mad at you.**{/color}"
            "{color=#808080}**Isabella love - 5**{color=#808080}"
            "{color=#808080}**Isabella obedience + 2**{color=#808080}"
            $ LilSis_love = LilSis_love - 5
            $ LilSis_Obedience = LilSis_Obedience + 2
            $ check_and_update_character_stats("LilSis")
            $ Location = "Hallway"
            $ advance_time_or_sleep()