init python:
    define_images("Selina_Greta_Scene", "BioClass/Selina_Greta", "Selina_Greta_Scene", 60)

label BioClass_Selina_Greta_Scene:
    if Watched_BioClass_Selina_Greta_Scene:
        MC "{color=#808080}*I already talked to them...*{color=#808080}"
        $ renpy.call("GameLoop")
    else:
        $ Watched_BioClass_Selina_Greta_Scene = True
        scene Selina_Greta_Scene1 with Dissolve(0.5)
        Selina "Yeah, but it's whatever, I'll just buy them both, who gives a fu—"
        MC "Hey Greta! What's up, do you mind if I borrow your homework for a minute?"
        scene Selina_Greta_Scene2 with Dissolve(0.5)
        Greta "Oh, hey, [MC], sure, no problem!"
        scene Selina_Greta_Scene3 with Dissolve(0.5)
        Selina "Um, excuse me?! I was talking here! How dare you interrupt me like that?!"
        scene Selina_Greta_Scene4 with Dissolve(0.5)
        MC "Oh, Selina, hey, I didn't see you there. Anyway..."
        scene Selina_Greta_Scene5 with Dissolve(0.5)
        MC "Thank you, Greta, I'll give it back before the class starts!"
        scene Selina_Greta_Scene6 with Dissolve(0.5)
        Selina "Tsk..."
        Selina "{color=#808080}*How dare he...*{color=#808080}"
        scene Selina_Greta_Scene7 with Dissolve(0.5)
        Selina "Don't ignore me, asshole!"
        scene Selina_Greta_Scene8 with Dissolve(0.5)
        MC "...."
        scene Selina_Greta_Scene9 with Dissolve(0.5)
        MC "Umm, any reason for why you hit me?"
        scene Selina_Greta_Scene10 with Dissolve(0.5)
        Selina "Hah, I don't need a reason to hit losers like you!"
        Selina "You should feel lucky I even touched you."
        Selina "Now let go of my foot, I don't want any poor to rub off on me. How dare you touch it in the first place?!"
        scene Selina_Greta_Scene11 with Dissolve(0.5)
        MC "......"
        scene Selina_Greta_Scene12 with Dissolve(0.5)
        MC "You know... I think you should start to learn to read the room."
        MC "I don't think you are in the position to have a big mouth."
        scene Selina_Greta_Scene13 with Dissolve(0.5)
        Selina "KYAAAAAA, WHAT ARE YOU DOING?!"
        scene Selina_Greta_Scene14 with Dissolve(0.5)
        MC "Hmmm, you are pretty flexible... more than I expected at least..."
        scene Selina_Greta_Scene15 with Dissolve(0.5)
        Selina "{color=#808080}*UGHHH, how is he so strong, I can't move my foot at all!*{color=#808080}"
        scene Selina_Greta_Scene16 with Dissolve(0.5)
        Selina "Let go of my foot, asshole! NOW!"
        scene Selina_Greta_Scene17 with Dissolve(0.5)
        MC "Hmmm... I don't think that's the way you ask for something, didn't you pay attention in manners class?"
        scene Selina_Greta_Scene18 with Dissolve(0.5)
        MC "Let's try again."
        scene Selina_Greta_Scene19 with Dissolve(0.5)
        Selina "KYAAAAA, OKAY, OKAY, LET ME GO, PLEASE!!"
        scene Selina_Greta_Scene20 with Dissolve(0.5)
        MC "Oh, so it's possible to be nice from time to time."
        scene Selina_Greta_Scene21 with Dissolve(0.5)
        MC "It wasn't so hard, was it?"
        scene Selina_Greta_Scene22 with Dissolve(0.5)
        MC "The class is about to start so I don't think I need the homework anymore, thank you anyway, Greta."
        scene Selina_Greta_Scene23 with Dissolve(0.5)
        Greta "O-okay, no problem..."
        scene Selina_Greta_Scene24 with Dissolve(0.5)
        Selina "Don't you think you can just walk off like that, asshole!!!"
        Selina "You are fucked, you hear me?! FUCKED!!!"
        scene Selina_Greta_Scene25 with Dissolve(0.5)
        MC "Yeah, yeah, whatever you say, Selina."
        call stat_reward({"Greta": {"love": 2, "corruption": 2, "obedience": 2}, "Selina": {"love": 2, "corruption": 2, "obedience": 2}})
