label JenniferMorning14:
    $ Jennifer14AM_compliment_given = False
    scene Jennifer_morning14_17
    MC "Hey mom, good morning!"
    scene Jennifer_morning14_16 with Dissolve(0.5)
    Jennifer "Good morning, kiddo!"
    Jennifer "You woke up so early today, did something happen?"
    scene Jennifer_morning14_17 with Dissolve(0.5)
    menu:
        "Spend some time with mom":
            MC "Nope, I just wanted to spend some time with you!"
            MC "Is there anything wrong with that?"
            MC "I feel like we don't get to spend any time together at all."
            scene Jennifer_morning14_18 with Dissolve(0.5)
            Jennifer "There is nothing wrong with that, [MC]."
            Jennifer "It's actually really sweet from you."
            Jennifer "But is also a bit out of character."
            Jennifer "Sooo... what happen? Did you do something bad?"
            scene Jennifer_morning14_19 with Dissolve(0.5)
            MC "Not at all, mom!"
            label morning14Questions:
                scene Jennifer_morning14_19 with Dissolve(0.5)
                menu:
                    "What do you think about us?":
                        MC "I just wanted to ask you, what do you think about us?"
                        scene Jennifer_morning14_20 with Dissolve(0.5)
                        Jennifer "Uhhh... that's kind of a weird question?"
                        Jennifer "What do you mean \"what do I think about us\"?"
                        Jennifer "Like our relationship, or what?"
                        scene Jennifer_morning14_21 with Dissolve(0.5)
                        MC "Yeah, about our relationship."
                        scene Jennifer_morning14_20 with Dissolve(0.5)
                        Jennifer "Uhhh... I don't know... it's good I guess... I hope.."
                        Jennifer "You are my son and I'm your mom. Is there something else to it?"
                        scene Jennifer_morning14_21 with Dissolve(0.5)
                        MC "No, mom, that's all that I wanted to know!"
                        scene Jennifer_morning14_20 with Dissolve(0.5)
                        Jennifer "You kids ask such weird questions these days.."
                        Jennifer "Was that all? or is there anything else you want?"
                        jump morning14Questions
                    "Compliment":
                        if not Jennifer14AM_compliment_given:
                            MC "I just wanted to tell you that you look really good this morning!"
                            scene Jennifer_morning14_20 with Dissolve(0.5)
                            Jennifer "Uhhh.... thank you..."
                            Jennifer "But now I'm sure something happened."
                            Jennifer "So tell me, how bad is it?"
                            scene Jennifer_morning14_21 with Dissolve(0.5)
                            MC "Ohhh, c'mon, can't I just compliment my mom?"
                            MC "You really look great today!"
                            scene Jennifer_morning14_18 with Dissolve(0.5)
                            Jennifer "Awwww, thank you kiddo, that's sweet."
                            Jennifer "But keep the compliments for the girls at school."
                            "{color=#808080}**Mom love + 2**{color=#808080}"
                            $ Jennifer_love = Jennifer_love + 2
                            $ check_and_update_character_stats("Jennifer")
                            $ Jennifer14AM_compliment_given = True
                        else:
                            "{color=#808080}*I've already complimented her.*{/color}"
                        jump morning14Questions
                    "Hug":
                        MC "I just wanted to give you a hug!"
                        scene Jennifer_morning14_18 with Dissolve(0.5)
                        Jennifer "Awwww, that's so sweet of you!"
                        scene Jennifer_morning14_22 with Dissolve(0.5)
                        Jennifer "Come here, kiddo, give mommy a hug!"
                        scene Jennifer_morning14_24 with Dissolve(0.5)
                        MC "I'm so happy I moved back with you, mom."
                        MC "The past month has been really fun!"
                        scene Jennifer_morning14_23 with Dissolve(0.5)
                        Jennifer "Ohhh, [MC], you're gonna make me tear up."
                        Jennifer "I'm so glad to hear that!"
                        scene Jennifer_morning14_25 with Dissolve(0.5)
                        MC "{color=#808080}*Her tits are pressing so hard against my chest*{/color}"
                        MC "{color=#808080}*I'm already getting hard, I have to do something about it.*{/color}"
                        MC "{color=#808080}*But at the same time, I can't waste the opportunity of being this close to her!*{/color}"
                        MC "{color=#808080}*I should leave...*{/color}"
                        menu:
                            "Touch her ass":
                                MC "{color=#808080}*Fuck it, who knows when I will get this chance again.*{/color}"
                                show Jennifer14AMVideos1
                                MC "{color=#808080}*I can't risk to squeeze it...*{/color}"
                                MC "{color=#808080}*I'll just put my hand there, make it look like an accident.*{/color}"
                                scene Jennifer_morning14_26 with Dissolve(0.5)
                                Jennifer "{color=#808080}*Uhhh.. is he-*{/color}"
                                Jennifer "{color=#808080}*Oh my... he is!*{/color}"
                                scene Jennifer_morning14_27 with Dissolve(0.5)
                                Jennifer "What are you doing [MC]?!"
                                MC "{color=#808080}*Fuck... I gotta play dumb.*{/color}"
                                scene Jennifer_morning14_28 with Dissolve(0.5)
                                MC "What is it mom, what happened?"
                                MC "Did I do something wrong?"
                                scene Jennifer_morning14_27 with Dissolve(0.5)
                                Jennifer "You just touched my butt, [MC]!"
                                scene Jennifer_morning14_28 with Dissolve(0.5)
                                MC "Oh my god, mom, I'm so sorry!"
                                MC "I didn't even realize! My head must've slip!"
                                MC "I totally didn't mean to do that!"
                                scene Jennifer_morning14_30 with Dissolve(0.5)
                                Jennifer "Hmmmmm..."
                                scene Jennifer_morning14_29 with Dissolve(0.5)
                                Jennifer "If you say so..."
                                Jennifer "But don't let it happen again!"
                                Jennifer "That's totally inappropriate!!"
                                Jennifer "Especially with me!"
                                Jennifer "Now get out of here, I have to go take a shower."
                                scene Jennifer_morning14_30 with Dissolve(0.5)
                                MC "Okay, mom, again, I'm sorry, I will not let it happen again."
                                MC "See you later then..."
                                scene BlackScreen
                                "{color=#808080}**You leave the room**{/color}"
                                "{color=#808080}**Mom love - 5**{color=#808080}"
                                "{color=#808080}**Mom corruption + 2**{color=#808080}"
                                "{color=#808080}**Mom obedience + 2**{color=#808080}"
                                $ Jennifer_love = Jennifer_love - 5
                                $ Jennifer_Corruption = Jennifer_Corruption + 2
                                $ Jennifer_Obedience = Jennifer_Obedience + 2
                                $ check_and_update_character_stats("Jennifer")
                                $ Location = "hallway"
                                $ advance_time_or_sleep()
                            "Don't":
                                scene Jennifer_morning14_23 with Dissolve(0.5)
                                Jennifer "Okay, kiddo, if that was all you can leave now."
                                Jennifer "I have to go take a shower."
                                Jennifer "But I really appreciate dropping by to hug me, it's sweet."
                                scene Jennifer_morning14_24 with Dissolve(0.5)
                                MC "No worries mom, it's my thank you for being such a wonderful mom!"
                                MC "I'll go now."
                                scene Jennifer_morning14_23 with Dissolve(0.5)
                                Jennifer "Oh, c'mon now, you don't have to be so nice, I told you I'm going to tear up."
                                Jennifer "And you could use a shower as well!"
                                scene Jennifer_morning14_24 with Dissolve(0.5)
                                MC "Ohhh.. okay, I'll go after you."
                                MC "See you around mom!"
                                scene BlackScreen
                                "{color=#808080}**You leave the room**{/color}"
                                "{color=#808080}**Mom love + 2**{color=#808080}"
                                "{color=#808080}**Mom corruption + 2**{color=#808080}"
                                $ Jennifer_love = Jennifer_love + 2
                                $ Jennifer_Corruption = Jennifer_Corruption + 2
                                $ check_and_update_character_stats("Jennifer")
                                $ Location = "Hallway"
                                $ advance_time_or_sleep()
                    "Leave":
                        MC "Ahhh, damn, I remembered I have to do a few things before I leave for school!"
                        MC "See you late mom!"
                        MC "Bye mom, see you around."
                        scene Jennifer_morning14_20 with Dissolve(0.5)
                        Jennifer "So much for spending time together.."
                        Jennifer "Okay, kiddo, I don't want to hear any complaints from your teachers!"
                        scene Jennifer_morning14_21 with Dissolve(0.5)
                        MC "You won't!"
                        MC "See ya!"
                        scene BlackScreen
                        "{color=#808080}**You leave the room**{/color}"
                        $ Location = "hallway"
                        $ advance_time_or_sleep()
        "Leave":
            scene Jennifer_morning14_17 with Dissolve(0.5)
            MC "Nothing..."
            MC "I just wanted to see if you're still sleeping."
            scene Jennifer_morning14_20 with Dissolve(0.5)
            Jennifer "May I ask why?"
            scene Jennifer_morning14_21 with Dissolve(0.5)
            MC "Nothing important, see you around, mom!"
            scene BlackScreen
            "{color=#808080}**You leave the room**{/color}"
            $ Location = "hallway"
            $ renpy.call("GameLoop")