init python:
    define_images("ArtClass_SelinaGreta_Scene", "ArtClass/Selina_Greta_Scene", "ArtClass_SelinaGreta_Scene", 100)

label ArtClass_SelinaGreta_Scene:
    if Watched_ArtClass_SelinaGreta_Scene:
        MC "{color=#808080}*I already talked to them...*{color=#808080}"
        $ renpy.call("GameLoop")
    else:
        $ Watched_ArtClass_SelinaGreta_Scene = True
        scene ArtClass_SelinaGreta_Scene1 with Dissolve(0.5)
        MC "Hey girls! Ready for class?"
        scene ArtClass_SelinaGreta_Scene2 with Dissolve(0.5)
        Greta "Hey, [MC]! Yeah, I'm actually pretty hyped for this one. This semester, we will learn to make figure drawings!"
        Greta "And that would b—"
        scene ArtClass_SelinaGreta_Scene3 with Dissolve(0.5)
        Selina "Greta!"
        scene ArtClass_SelinaGreta_Scene4 with Dissolve(0.5)
        Greta "Y-yes, Selina, what happened?"
        scene ArtClass_SelinaGreta_Scene5 with Dissolve(0.5)
        Selina "Can you tell this loser to get lost already?!"
        scene ArtClass_SelinaGreta_Scene6 with Dissolve(0.5)
        Selina "I mean... maybe it's the stench..."
        scene ArtClass_SelinaGreta_Scene7 with Dissolve(0.5)
        Selina "Yeah! I think that's it."
        Selina "I can't stand you being anywhere near me."
        Selina "So get lost already; you have no business standing next to me!"
        scene ArtClass_SelinaGreta_Scene8 with Dissolve(0.5)
        Greta "Bye-bye, [MC]!"
        call stat_reward({"Greta": {"love": 2}, "Selina": {"love": 2}})
