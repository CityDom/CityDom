label LilSisNoon24:

    scene NOON24LILSIS1 with Dissolve(0.5)
    Isabella "Hey [MC], don't you greet your little sister when she gets home?"
    Isabella "You are so rude!"
    scene NOON24LILSIS2 with Dissolve(0.5)
    MC "Always a joy when you're back, isn't it?"
    scene NOON24LILSIS3 with Dissolve(0.5)
    Isabella "And sarcastic as well I see."
    scene NOON24LILSIS4 with Dissolve(0.5)
    MC "Don't forget to take off your shoes."
    scene NOON24LILSIS5 with Dissolve(0.5)
    Isabella "Wow, a direct order? What's next? You'll ask me to take my shirt off?"
    MC "{color=#808080}*Not only that*{/color}"
    MC "I wouldn't mind."
    Isabella "Shut up, pervert."
    scene NOON24LILSIS6 with Dissolve(0.5)
    MC "You know mom gets mad whenever we get inside the house with shoes on."
    Isabella "Yea,  yea, I know."
    scene NOON24LILSIS7 with Dissolve(0.5)
    Isabella "Oh my god, I almost fell."
    Isabella "I hate these shoes so much!"
    scene NOON24LILSIS8 with Dissolve(0.5)
    Isabella "There you go, are you happy now?"
    scene NOON24LILSIS9 with Dissolve(0.5)
    MC "You don't have to get mad at me."
    MC "I'm doing this so mom won't get mad at you! "
    extend "You should thank me."
    scene NOON24LILSIS10 with Dissolve(0.5)
    Isabella "Yeah... you're right."
    scene NOON24LILSIS11 with Dissolve(0.5)
    Isabella "Thank you!"
    MC "{color=#808080}*Should I try out my luck?*{/color}"
    menu:
        "Joke around":
            MC "WAIT!!!"
            scene NOON24LILSIS12 with Dissolve(0.5)
            Isabella "WHAAT?!?!"
            Isabella "What did I do?!"
            MC "You forgot to also take your shirt off!"
            scene NOON24LILSIS13 with Dissolve(0.5)
            Isabella "UGHHH!!!!!"
            Isabella "You seriously have a death wish, don't you?!"
            scene NOON24LILSIS14 with Dissolve(0.5)
            MC "I was just joking! Calm down!"
            scene NOON24LILSIS13 with Dissolve(0.5)
            Isabella "That's not even remotely funny."
            Isabella "You scared the shit out of me!!"
            scene NOON24LILSIS14 with Dissolve(0.5)
            MC "Alright, alright, I'm sorry. Just trying to lighten the mood."
            scene NOON24LILSIS15 with Dissolve(0.5)
            Isabella "Try harder. And preferably without the inappropriate comments."
            MC "Okay, okay, I got it. No more shirt jokes."
            Isabella "Good. Let's keep it that way."
            MC "See you around, right?"
            Isabella "...."
            MC "{color=#808080}*I think she's pissed*{/color}"
            "{color=#808080}**Isabella love - 5**{color=#808080}"
            "{color=#808080}**Isabella obedience + 2**{color=#808080}"
            $ LilSis_love = LilSis_love - 5
            $ LilSis_Obedience = LilSis_Obedience + 2
            $ check_and_update_character_stats("LilSis")
            $ Location = "entrance"
            $ advance_time_or_sleep()
        "Don't":
            scene NOON24LILSIS16 with Dissolve(0.5)
            Isabella "See you around, [MC]."
            MC "Just like that? no kiss? no hug?"
            Isabella "In your dreams, pervert!"
            "{color=#808080}**Isabella love + 2**{color=#808080}"
            $ LilSis_love = LilSis_love + 2
            $ check_and_update_character_stats("LilSis")
            $ Location = "entrance"
            $ advance_time_or_sleep()



