label MomMorning14:
    $ Mom14AM_compliment_given = False
    scene MOM17
    MC "Hey mom, good morning!"
    scene MOM16 with Dissolve(0.5)
    McMom "Good morning, kiddo!"
    McMom "You woke up so early today, did something happen?"
    scene MOM17 with Dissolve(0.5)
    menu:
        "Spend some time with mom":
            MC "Nope, I just wanted to spend some time with you!"
            MC "Is there anything wrong with that?"
            MC "I feel like we don't get to spend any time together at all."
            scene MOM18 with Dissolve(0.5)
            McMom "There is nothing wrong with that, [MC]."
            McMom "It's actually really sweet from you."
            McMom "But is also a bit out of character."
            McMom "Sooo... what happen? Did you do something bad?"
            scene MOM19 with Dissolve(0.5)
            MC "Not at all, mom!"
            label morning14Questions:
                scene MOM19 with Dissolve(0.5)
                menu:
                    "What do you think about us?":
                        MC "I just wanted to ask you, what do you think about us?"
                        scene MOM20 with Dissolve(0.5)
                        McMom "Uhhh... that's kind of a weird question?"
                        McMom "What do you mean \"what do I think about us\"?"
                        McMom "Like our relationship, or what?"
                        scene MOM21 with Dissolve(0.5)
                        MC "Yeah, about our relationship."
                        scene MOM20 with Dissolve(0.5)
                        McMom "Uhhh... I don't know... it's good I guess... I hope.."
                        McMom "You are my son and I'm your mom. Is there something else to it?"
                        scene MOM21 with Dissolve(0.5)
                        MC "No, mom, that's all that I wanted to know!"
                        scene MOM20 with Dissolve(0.5)
                        McMom "You kids ask such weird questions these days.."
                        McMom "Was that all? or is there anything else you want?"
                        jump morning14Questions
                    "Compliment":
                        if not Mom14AM_compliment_given:
                            MC "I just wanted to tell you that you look really good this morning!"
                            scene MOM20 with Dissolve(0.5)
                            McMom "Uhhh.... thank you..."
                            McMom "But now I'm sure something happened."
                            McMom "So tell me, how bad is it?"
                            scene MOM21 with Dissolve(0.5)
                            MC "Ohhh, c'mon, can't I just compliment my mom?"
                            MC "You really look great today!"
                            scene MOM18 with Dissolve(0.5)
                            McMom "Awwww, thank you kiddo, that's sweet."
                            McMom "But keep the compliments for the girls at school."
                            "{color=#808080}**Mom love + 2**{color=#808080}"
                            $ Mom_love = Mom_love + 2
                            $ check_and_update_character_stats("Mom")
                            $ Mom14AM_compliment_given = True
                        else:
                            "{color=#808080}*I've already complimented her.*{/color}"
                        jump morning14Questions
                    "Hug":
                        MC "I just wanted to give you a hug!"
                        scene MOM18 with Dissolve(0.5)
                        McMom "Awwww, that's so sweet of you!"
                        scene MOM22 with Dissolve(0.5)
                        McMom "Come here, kiddo, give mommy a hug!"
                        scene MOM24 with Dissolve(0.5)
                        MC "I'm so happy I moved back with you, mom."
                        MC "The past month has been really fun!"
                        scene MOM23 with Dissolve(0.5)
                        McMom "Ohhh, [MC], you're gonna make me tear up."
                        McMom "I'm so glad to hear that!"
                        scene MOM25 with Dissolve(0.5)
                        MC "{color=#808080}*Her tits are pressing so hard against my chest*{/color}"
                        MC "{color=#808080}*I'm already getting hard, I have to do something about it.*{/color}"
                        MC "{color=#808080}*But at the same time, I can't waste the opportunity of being this close to her!*{/color}"
                        MC "{color=#808080}*I should leave...*{/color}"
                        menu:
                            "Touch her ass":
                                MC "{color=#808080}*Fuck it, who knows when I will get this chance again.*{/color}"
                                show Mom14AMVideos1
                                MC "{color=#808080}*I can't risk to squeeze it...*{/color}"
                                MC "{color=#808080}*I'll just put my hand there, make it look like an accident.*{/color}"
                                scene MOM26 with Dissolve(0.5)
                                McMom "{color=#808080}*Uhhh.. is he-*{/color}"
                                McMom "{color=#808080}*Oh my... he is!*{/color}"
                                scene MOM27 with Dissolve(0.5)
                                McMom "What are you doing [MC]?!"
                                MC "{color=#808080}*Fuck... I gotta play dumb.*{/color}"
                                scene MOM28 with Dissolve(0.5)
                                MC "What is it mom, what happened?"
                                MC "Did I do something wrong?"
                                scene MOM27 with Dissolve(0.5)
                                McMom "You just touched my butt, [MC]!"
                                scene MOM28 with Dissolve(0.5)
                                MC "Oh my god, mom, I'm so sorry!"
                                MC "I didn't even realize! My head must've slip!"
                                MC "I totally didn't mean to do that!"
                                scene MOM30 with Dissolve(0.5)
                                McMom "Hmmmmm..."
                                scene MOM29 with Dissolve(0.5)
                                McMom "If you say so..."
                                McMom "But don't let it happen again!"
                                McMom "That's totally inappropriate!!"
                                McMom "Especially with me!"
                                McMom "Now get out of here, I have to go take a shower."
                                scene MOM30 with Dissolve(0.5)
                                MC "Okay, mom, again, I'm sorry, I will not let it happen again."
                                MC "See you later then..."
                                scene BlackScreen
                                "{color=#808080}**You leave the room**{/color}"
                                "{color=#808080}**Mom love - 5**{color=#808080}"
                                "{color=#808080}**Mom corruption + 2**{color=#808080}"
                                "{color=#808080}**Mom obedience + 2**{color=#808080}"
                                $ Mom_love = Mom_love - 5
                                $ Mom_Corruption = Mom_Corruption + 2
                                $ Mom_Obedience = Mom_Obedience + 2
                                $ check_and_update_character_stats("Mom")
                                $ Location = "hallway"
                                $ advance_time_or_sleep()
                            "Don't":
                                scene MOM23 with Dissolve(0.5)
                                McMom "Okay, kiddo, if that was all you can leave now."
                                McMom "I have to go take a shower."
                                McMom "But I really appreciate dropping by to hug me, it's sweet."
                                scene MOM24 with Dissolve(0.5)
                                MC "No worries mom, it's my thank you for being such a wonderful mom!"
                                MC "I'll go now."
                                scene MOM23 with Dissolve(0.5)
                                McMom "Oh, c'mon now, you don't have to be so nice, I told you I'm going to tear up."
                                McMom "And you could use a shower as well!"
                                scene MOM24 with Dissolve(0.5)
                                MC "Ohhh.. okay, I'll go after you."
                                MC "See you around mom!"
                                scene BlackScreen
                                "{color=#808080}**You leave the room**{/color}"
                                "{color=#808080}**Mom love + 2**{color=#808080}"
                                "{color=#808080}**Mom corruption + 2**{color=#808080}"
                                $ Mom_love = Mom_love + 2
                                $ Mom_Corruption = Mom_Corruption + 2
                                $ check_and_update_character_stats("Mom")
                                $ Location = "Hallway"
                                $ advance_time_or_sleep()
                    "Leave":
                        MC "Ahhh, damn, I remembered I have to do a few things before I leave for school!"
                        MC "See you late mom!"
                        MC "Bye mom, see you around."
                        scene MOM20 with Dissolve(0.5)
                        McMom "So much for spending time together.."
                        McMom "Okay, kiddo, I don't want to hear any complaints from your teachers!"
                        scene MOM21 with Dissolve(0.5)
                        MC "You won't!"
                        MC "See ya!"
                        scene BlackScreen
                        "{color=#808080}**You leave the room**{/color}"
                        $ Location = "hallway"
                        $ advance_time_or_sleep()
        "Leave":
            scene MOM17 with Dissolve(0.5)
            MC "Nothing..."
            MC "I just wanted to see if you're still sleeping."
            scene MOM20 with Dissolve(0.5)
            McMom "May I ask why?"
            scene MOM21 with Dissolve(0.5)
            MC "Nothing important, see you around, mom!"
            scene BlackScreen
            "{color=#808080}**You leave the room**{/color}"
            $ Location = "hallway"
            $ renpy.call("GameLoop")