label MovieNightLVL1:

    scene MovieScene28 with Dissolve(0.5)
    "{color=#808080}**You walk into the living room**{/color}"
    MC "{color=#808080}*Oh, the girls are watching a movie, should I join them?*{/color}"
    menu:
        "Join them":
            scene MovieScene26 with Dissolve(0.5)
            MC "Hey, what are y'all doing?"
            Jennifer "Oh hey kiddo, we are deciding on what movie to watch."
            MC "Can I join?"
            Jennifer "Sure, come here."
            scene MovieScene30 with Dissolve(0.5)
            Jennifer "So... ummm... what movie do you kids want to watch?"
            scene MovieScene32 with Dissolve(0.5)
            MC "Can I choose?"
            scene MovieScene30 with Dissolve(0.5)
            Jennifer "Sure, We can never decide anyway."
            MC "{color=#808080}*What should I choose?*{/color}"

            label MovieChoise_menu:
                scene MovieScene30 with Dissolve(0.5)
                menu:
                    "Action":
                        call stat_reward({"Isabella": {"love": 2}, "Jennifer": {"love": 2}}, return_to=None)
                        scene MovieScene31 with Dissolve(0.5)
                        MC "We could watch an action movie."
                        scene MovieScene30 with Dissolve(0.5)
                        Jennifer "Oke, an action movie it is!"
                        scene MovieScene33 with Dissolve(0.5)
                        Claire "C'mon mom, are we really gonna let him choose the movie? I bet it's gonna be shit!"
                        scene MovieScene34 with Dissolve(0.5)
                        Jennifer "Watch your mouth Claire, I said we are letting [MC] choose for this night."
                        Claire "Tsk... Fine... I'll try not to fall asleep."
                        scene BlackScreen with Dissolve(0.5)
                        "40 minutes later..."
                        scene MovieScene24 with Dissolve(0.5)
                        MC "{color=#808080}*On who should I make a move on?*{/color}"
                        menu:
                            "Jennifer":
                                scene MovieScene23 with Dissolve(0.5)
                                MC "{color=#808080}*I'll just take it slow...*{/color}"
                                scene MovieScene22 with Dissolve(0.5)
                                Jennifer "Take your hand off kiddo."
                                MC "Yep, oke.."
                                scene MovieScene24 with Dissolve(0.5)
                                MC "{color=#808080}*I expected as much...*{/color}"
                                scene BlackScreen with Dissolve(0.5)
                                "{color=#808080}**You watch the rest of the movie and leave**{/color}"
                                $ Location = "Entrance"
                                $ advance_time_or_sleep()
                            "Isabella":
                                scene MovieScene10 with Dissolve(0.5)
                                MC "{color=#808080}*I hope she doesn't make a scene out of this*{/color}"
                                scene MovieScene7 with Dissolve(0.5)
                                Isabella "Don't even try [MC]."
                                scene MovieScene24 with Dissolve(0.5)
                                MC "{color=#808080}*Eh... I tried*{/color}"
                                scene BlackScreen with Dissolve(0.5)
                                "{color=#808080}**You watch the rest of the movie and leave**{/color}"
                                $ Location = "Entrance"
                                $ advance_time_or_sleep()
                                # scene MovieScene9 with Dissolve(0.5)
                                # MC "{color=#808080}*Maybe she didn't reali-*{/color}"
                                # scene MovieScene7 with Dissolve(0.5)
                                # Isabella "Huh!"
                                # scene MovieScene6 with Dissolve(0.5)
                                # Isabella "Ummm....."
                                # scene MovieScene4 with Dissolve(0.5)
                                # Isabella "Could you..."
                                # scene MovieScene3 with Dissolve(0.5)
                                # Isabella "Take your hand off me?"
                                # scene MovieScene24 with Dissolve(0.5)
                                # MC "{color=#808080}*Eh... I tried*{/color}"
                            "Claire":
                                scene MovieScene2 with Dissolve(0.5)
                                MC "Psst!"
                                MC "Pssssst!"
                                scene MovieScene1 with Dissolve(0.5)
                                Claire "I'm trying to watch this boring movie, don't talk to me, loser."
                                scene MovieScene24 with Dissolve(0.5)
                                MC "{color=#808080}*Ehh.... I don't know what I expected.*{/color}"
                                scene BlackScreen with Dissolve(0.5)
                                "{color=#808080}**You watch the rest of the movie and leave**{/color}"
                                $ Location = "Entrance"
                                $ advance_time_or_sleep()
                            "Don't":
                                MC "{color=#808080}*Let's just watch the movie...*{/color}"
                                scene BlackScreen with Dissolve(0.5)
                                "{color=#808080}**You watch the rest of the movie and leave**{/color}"
                                $ Location = "Entrance"
                                $ advance_time_or_sleep()
                    "Romance":
                        call stat_reward({"Isabella": {"love": 2}, "Jennifer": {"love": 2}}, return_to=None)
                        scene MovieScene31 with Dissolve(0.5)
                        MC "We could watch a romance movie"
                        scene MovieScene30 with Dissolve(0.5)
                        Jennifer "Oke, a romance movie it is!"
                        scene MovieScene33 with Dissolve(0.5)
                        Claire "C'mon mom, are we really gonna let him choose the movie? I bet it's gonna be shit!"
                        scene MovieScene34 with Dissolve(0.5)
                        Jennifer "Watch your mouth Claire, I said we are letting [MC] choose for this night."
                        Claire "Tsk... Fine... I'll try not to fall asleep."
                        scene BlackScreen with Dissolve(0.5)
                        "40 minutes later..."
                        scene MovieScene35 with Dissolve(0.5)
                        MC "{color=#808080}*On who should I make a move on?*{/color}"
                        menu:
                            "Jennifer":
                                Jennifer "Oh, this is so beautiful... and so sad at the same time."
                                MC "{color=#808080}*Maybe I could console her...*{/color}"
                                scene MovieScene36 with Dissolve(0.5)
                                MC " Mom, are you okay?"
                                scene MovieScene37 with Dissolve(0.5)
                                Jennifer "Yeah kiddo, I'm okay. Love stories always tear me up."
                                Jennifer "They remind me of my younger days."
                                scene MovieScene38 with Dissolve(0.5)
                                MC "C'mon mom, what are you talking about, you look better than that actress."
                                scene MovieScene39 with Dissolve(0.5)
                                Jennifer "Awww, that's cute [MC], now let me watch the movie."
                                MC "{color=#808080}*Tsk...*{/color}"
                                scene BlackScreen with Dissolve(0.5)
                                "{color=#808080}**You watch the rest of the movie and leave**{/color}"
                                $ Location = "Entrance"
                                $ advance_time_or_sleep()
                            "Isabella":
                                scene MovieScene40 with Dissolve(0.5)
                                MC "{color=#808080}*Huh? is she actually tearing up at this shitty movie?*{/color}"
                                scene MovieScene41 with Dissolve(0.5)
                                MC "Are you crying?"
                                MC "I didn't know you were so emotional sis."
                                scene MovieScene42 with Dissolve(0.5)
                                Isabella "You know romance movies are my weak point."
                                Isabella "How could you not get sad at this, they loved eachother so much, just for something like this to happen."
                                Isabella "Don't you have any compassion?"
                                scene MovieScene43 with Dissolve(0.5)
                                MC "Of course I do sis, it's just that movies don't really get to me like that."
                                scene MovieScene44 with Dissolve(0.5)
                                Isabella "Ughhh... I swear it feels like I'm talking to a brick wall sometimes!"
                                Isabella "Let me watch the movie."
                                scene BlackScreen with Dissolve(0.5)
                                "{color=#808080}**You watch the rest of the movie and leave**{/color}"
                                $ Location = "Entrance"
                                $ advance_time_or_sleep()
                            "Claire":
                                scene MovieScene45 with Dissolve(0.5)
                                MC "Psst..."
                                MC "Pssssssst..."
                                scene MovieScene46 with Dissolve(0.5)
                                Claire "I'm trying to watch this cringe crap, leave me alone!"
                                MC "...."
                                scene MovieScene35 with Dissolve(0.5)
                                MC "{color=#808080}*I expected as much*{/color}"
                                scene BlackScreen with Dissolve(0.5)
                                "{color=#808080}**You watch the rest of the movie and leave**{/color}"
                                $ Location = "Entrance"
                                $ advance_time_or_sleep()
                            "Don't":
                                MC "{color=#808080}*Let's just watch the movie...*{/color}"
                                scene BlackScreen with Dissolve(0.5)
                                "{color=#808080}**You watch the rest of the movie and leave**{/color}"
                                $ Location = "Entrance"
                                $ advance_time_or_sleep()
                    "Horror":
                        call stat_reward({"Isabella": {"love": -2}, "Jennifer": {"love": -2}}, return_to=None)
                        scene MovieScene31 with Dissolve(0.5)
                        MC "We could maybe watch a horror movie"
                        scene MovieScene30 with Dissolve(0.5)
                        Jennifer "Ughh... I get scared really easily... but I guess we could watch that."
                        scene MovieScene33 with Dissolve(0.5)
                        Claire "C'mon mom, are we really gonna let him choose the movie? I bet it's gonna be shit!"
                        scene MovieScene34 with Dissolve(0.5)
                        Jennifer "Watch your mouth Claire, I said we are letting [MC] choose for this night."
                        Claire "Tsk... Fine... I'll try not to fall asleep."
                        scene BlackScreen with Dissolve(0.5)
                        "40 minutes later..."
                        scene MovieScene47 with Dissolve(0.5)
                        MC "{color=#808080}*Damn... this movie really is shit*{/color}"
                        MC "{color=#808080}*It's getting really boring, should I try something?*{/color}"
                        menu:
                            "Jennifer":
                                scene MovieScene48 with Dissolve(0.5)
                                MC "{color=#808080}*She didn't lie when she said she gets scared easily...*{/color}"
                                MC "{color=#808080}*I bet she's going to jump if I move an inch*{/color}"
                                scene MovieScene49 with Dissolve(0.5)
                                MC "It's just a movie mom, no reason to be scared"
                                scene MovieScene50 with Dissolve(0.5)
                                Jennifer "AAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!!!!"
                                scene MovieScene51 with Dissolve(0.5)
                                Isabella "KYAAAAAAA!!!!!!"
                                MC "{color=#808080}*oh my god.....what have I caused..*{/color}"
                                scene MovieScene52 with Dissolve(0.5)
                                Claire "You finally did something kinda funny, dumbass."
                                scene MovieScene53 with Dissolve(0.5)
                                Jennifer "OMG [MC] YOU SCARED THE SOUL OUT OF ME!!"
                                MC "I'm sorry mom I just wanted to-"
                                Jennifer "Don't EVER do that again! Do you understand?!!?!?"
                                MC "But I just-"
                                Jennifer "Let me watch the movie and stay put!"
                                MC "{color=#808080}*Damn...*{/color}"
                                scene BlackScreen with Dissolve(0.5)
                                "{color=#808080}**You watch the rest of the movie and leave**{/color}"
                                $ Location = "Entrance"
                                $ advance_time_or_sleep()
                            "Isabella":
                                scene MovieScene54 with Dissolve(0.5)
                                MC "{color=#808080}*It might be funny to try and scare her.*{/color}"
                                scene MovieScene55 with Dissolve(0.5)
                                MC "Boo!"
                                Isabella "KYAAAAAAA!!!!!!!!!"
                                scene MovieScene56 with Dissolve(0.5)
                                Jennifer "AAAAAAAAAAAAAA!!!!!"
                                Isabella "AAAAAAAA!!!!!"
                                Claire "Hehe, I was just thinking about doing that."
                                scene MovieScene57 with Dissolve(0.5)
                                Isabella "YOU ASSHOLE!!!"
                                Isabella "IT'S NOT FUNNY!!!"
                                MC "It was pretty funny!!"
                                Isabella "You are such a jerk!"
                                Isabella "Let me watch the movie or I'm leaving!"
                                MC "Oke geez..."
                                scene BlackScreen with Dissolve(0.5)
                                "{color=#808080}**You watch the rest of the movie and leave**{/color}"
                                $ Location = "Entrance"
                                $ advance_time_or_sleep()
                            "Claire":
                                scene MovieScene59 with Dissolve(0.5)
                                MC "{color=#808080}*Hmmm... Is she actually enjoying this piece of shit?*{/color}"
                                MC "{color=#808080}*Seeing that the whole movie is about a woman torturing men... I see why she would like it.*{/color}"
                                scene MovieScene58 with Dissolve(0.5)
                                MC "Hey Claire, how are you liking the movie?"
                                scene MovieScene60 with Dissolve(0.5)
                                Claire "It's not complete dogshit, I might be able to stay awake."
                                Claire "Now stop talking and let me watch the movie!"
                                scene MovieScene58 with Dissolve(0.5)
                                MC "I'm glad you like the movie I suggested!"
                                scene MovieScene60 with Dissolve(0.5)
                                Claire "Yeah whatever, now shut up!"
                                MC "okay, geez..."
                                scene BlackScreen with Dissolve(0.5)
                                "{color=#808080}**You watch the rest of the movie and leave**{/color}"
                                $ Location = "Entrance"
                                $ advance_time_or_sleep()
                    "Erotic":
                        MC "{color=#808080}*I don't think it's a good ideea to even suggest that*{/color}"
                        jump MovieChoise_menu
        "Leave":
            $ Location = "Entrance"
            $ renpy.call("GameLoop")