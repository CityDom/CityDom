init python:
    define_images("Pool_Selina_Greta_Scene", "SwimClass/Selina_Greta_Scene", "Pool_Selina_Greta_Scene", 100)

label SwimClass_Selina_Greta_Scene:
    if Watched_SwimClass_Selina_Greta_Scene:
        scene Pool_Selina_Greta_Scene1 with Dissolve(0.5)
        MC "{color=#808080}*I already dealt with her...*"
        $ renpy.call("GameLoop")
    else:
        $ Watched_SwimClass_Selina_Greta_Scene = True

        scene Pool_Selina_Greta_Scene1 with Dissolve(0.5)
        MC "Hey, Greta, what's up? Why aren't you coming in the water?"
        scene Pool_Selina_Greta_Scene2 with Dissolve(0.5)
        Greta "Oh, hey, [MC]!"
        Greta "Sure, I'll join you in a second!"
        scene Pool_Selina_Greta_Scene3 with Dissolve(0.5)
        Selina "Uhhh, excuse me!"
        scene Pool_Selina_Greta_Scene4 with Dissolve(0.5)
        Selina "Who allowed you to speak to my footstand?"
        scene Pool_Selina_Greta_Scene5 with Dissolve(0.5)
        MC "She's not your footstand, Selina!"
        MC "Nor do I need your permission to talk to her!"
        scene Pool_Selina_Greta_Scene6 with Dissolve(0.5)
        Selina "Oh, my bad, I misunderstood you. You're jealous of her!"
        Selina "You just wanted to take her place!"
        scene Pool_Selina_Greta_Scene7 with Dissolve(0.5)
        Selina "Well... maybe if you ask nicely, I'll allow it."
        scene Pool_Selina_Greta_Scene8 with Dissolve(0.5)
        Selina "And if you kiss my feet first, show me you really want it."
        scene Pool_Selina_Greta_Scene9 with Dissolve(0.5)
        MC "Tsk, go fuck yourself, Selina!"
        scene Pool_Selina_Greta_Scene10 with Dissolve(0.5)
        Selina "Hahahaha, I got the broke boy mad, he's fuming!! Hahahahaha!!"
        scene Pool_Selina_Greta_Scene11 with Dissolve(0.5)
        MC "Tsk...."
        call stat_reward({"Greta": {"love": 2}, "Selina": {"love": 2}})
