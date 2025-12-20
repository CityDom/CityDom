init python:
    define_images("Lola_Team_Scene", "GymClass/Lola_Team_Scene", "Lola_Team_Scene", 74)

label Lola_Team_Scene:
    if not Watched_GymClass_Lola_Team_Scene:
        $ Watched_GymClass_Lola_Team_Scene = True
        scene Lola_Team_Scene1 with Dissolve(0.5)
        MC "Hey girls, are you ready for the game?"
        scene Lola_Team_Scene2 with Dissolve(0.5)
        Selina "Get away, loser! This is not your team!"
        Selina "We don't need you hearing our plans!"
        scene Lola_Team_Scene3 with Dissolve(0.5)
        Lola "Calm down, Selina, it's not like we have some master plan."
        Lola "And it's just some friendly game anyway."
        scene Lola_Team_Scene4 with Dissolve(0.5)
        Selina "Hmph!"
        scene Lola_Team_Scene5 with Dissolve(0.5)
        Lola "It's okay, [MC], the only secret plan you're going to hear is 'give the ball to Lola.'"
        scene Lola_Team_Scene6 with Dissolve(0.5)
        MC "Hah, sounds like a pretty good plan!"
        scene Lola_Team_Scene7 with Dissolve(0.5)
        Lola "Yeah, it usually works, so we stick with it."
        Lola "But who knows, now that you're here, maybe it won't be so easy."
        scene Lola_Team_Scene8 with Dissolve(0.5)
        MC "Hah, I think you overestimate me."
        scene Lola_Team_Scene9 with Dissolve(0.5)
        Lola "Maybe... but last time we played, you surprised me!"
        Lola "So it might be an interesting match!"
        scene Lola_Team_Scene10 with Dissolve(0.5)
        Selina "Ughhhh, do we really have to sit here and listen to these two suck each other off?"
        scene Lola_Team_Scene11 with Dissolve(0.5)
        Selina "Oh, weaw, you're so good, I can't wait to play with you!"
        scene Lola_Team_Scene12 with Dissolve(0.5)
        Selina "Like, get a room already."
        scene Lola_Team_Scene13 with Dissolve(0.5)
        MC "Is it really that disgusting for you to see two people having a genuine conversation?"
        MC "You're a really sad person, Selina..."
        scene Lola_Team_Scene14 with Dissolve(0.5)
        Selina "UGHHHH!!"
        scene Lola_Team_Scene15 with Dissolve(0.5)
        Selina "You know what's sad?! Being a poor loser whose mommy has to drive you to school or take the bus!"
        Selina "Or having to sit next to the class weirdo because no one else likes you!"
        scene Lola_Team_Scene16 with Dissolve(0.5)
        MC "Damn, I must've hit a soft spot for you to go on such a rant."
        MC "I'll leave it at that then; I don't wanna get expelled for some dumbass reason."
        scene Lola_Team_Scene17 with Dissolve(0.5)
        Selina "Yeah, that's right! You better walk away!"
        scene BlackScreen with Dissolve(0.5)
        "{color=#808080}**Lola love + 2**{/color}"
        $ Lola_love += 2
        $ check_and_update_character_stats("Lola")
    else:
        MC "{color=#808080}*I've already talked to them about this.*{/color}"
    $ renpy.call("GameLoop")