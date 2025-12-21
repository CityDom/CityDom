label IsabellaNoon24:

    scene Isabella_noon24_1 with Dissolve(0.5)
    Isabella "Hey [MC], don't you greet your little sister when she gets home?"
    Isabella "You are so rude!"
    scene Isabella_noon24_2 with Dissolve(0.5)
    MC "Always a joy when you're back, isn't it?"
    scene Isabella_noon24_3 with Dissolve(0.5)
    Isabella "And sarcastic as well I see."
    scene Isabella_noon24_4 with Dissolve(0.5)
    MC "Don't forget to take off your shoes."
    scene Isabella_noon24_5 with Dissolve(0.5)
    Isabella "Wow, a direct order? What's next? You'll ask me to take my shirt off?"
    MC "{color=#808080}*Not only that*{/color}"
    MC "I wouldn't mind."
    Isabella "Shut up, pervert."
    scene Isabella_noon24_6 with Dissolve(0.5)
    MC "You know mom gets mad whenever we get inside the house with shoes on."
    Isabella "Yea,  yea, I know."
    scene Isabella_noon24_7 with Dissolve(0.5)
    Isabella "Oh my god, I almost fell."
    Isabella "I hate these shoes so much!"
    scene Isabella_noon24_8 with Dissolve(0.5)
    Isabella "There you go, are you happy now?"
    scene Isabella_noon24_9 with Dissolve(0.5)
    MC "You don't have to get mad at me."
    MC "I'm doing this so mom won't get mad at you! "
    extend "You should thank me."
    scene Isabella_noon24_10 with Dissolve(0.5)
    Isabella "Yeah... you're right."
    scene Isabella_noon24_11 with Dissolve(0.5)
    Isabella "Thank you!"
    MC "{color=#808080}*Should I try out my luck?*{/color}"
    menu:
        "Joke around":
            MC "WAIT!!!"
            scene Isabella_noon24_12 with Dissolve(0.5)
            Isabella "WHAAT?!?!"
            Isabella "What did I do?!"
            MC "You forgot to also take your shirt off!"
            scene Isabella_noon24_13 with Dissolve(0.5)
            Isabella "UGHHH!!!!!"
            Isabella "You seriously have a death wish, don't you?!"
            scene Isabella_noon24_14 with Dissolve(0.5)
            MC "I was just joking! Calm down!"
            scene Isabella_noon24_13 with Dissolve(0.5)
            Isabella "That's not even remotely funny."
            Isabella "You scared the shit out of me!!"
            scene Isabella_noon24_14 with Dissolve(0.5)
            MC "Alright, alright, I'm sorry. Just trying to lighten the mood."
            scene Isabella_noon24_15 with Dissolve(0.5)
            Isabella "Try harder. And preferably without the inappropriate comments."
            MC "Okay, okay, I got it. No more shirt jokes."
            Isabella "Good. Let's keep it that way."
            MC "See you around, right?"
            Isabella "...."
            MC "{color=#808080}*I think she's pissed*{/color}"
            call stat_reward({"Isabella": {"love": -5, "obedience": 2}}, show_black=False, return_to=None)
            $ Location = "entrance"
            $ advance_time_or_sleep()
        "Don't":
            scene Isabella_noon24_16 with Dissolve(0.5)
            Isabella "See you around, [MC]."
            MC "Just like that? no kiss? no hug?"
            Isabella "In your dreams, pervert!"
            call stat_reward({"Isabella": {"love": 2}}, show_black=False, return_to=None)
            $ Location = "entrance"
            $ advance_time_or_sleep()



