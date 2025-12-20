init python:
    define_images("Sophie_Alis_Scene", "ArtClass/Sophie_Alis_Scene", "Sophie_Alis_Scene", 100)

label ArtClass_SophieAlis_Scene:
    if Watched_ArtClass_SophieAlis_Scene:
        MC "{color=#808080}*I already talked to them...*{color=#808080}"
        $ renpy.call("GameLoop")
    else:
        $ Watched_ArtClass_SophieAlis_Scene = True
        scene Sophie_Alis_Scene1 with Dissolve(0.5)
        MC "Hey Sophie, hey Alis!"
        scene Sophie_Alis_Scene2 with Dissolve(0.5)
        Sophie "Oh hey... ummm..."
        scene Sophie_Alis_Scene3 with Dissolve(0.5)
        Sophie "Uhhhhhhhhh...."
        Sophie "Ummmmmmm...."
        scene Sophie_Alis_Scene4 with Dissolve(0.5)
        Alis "It's [MC]... His name is [MC]."
        Alis "It's [MC]...."
        scene Sophie_Alis_Scene5 with Dissolve(0.5)
        Sophie "OH! Yeah, that's right! [MC]!"
        Sophie "How could I forget!"
        scene Sophie_Alis_Scene6 with Dissolve(0.5)
        Alis "Ughhhh...."
        scene Sophie_Alis_Scene7 with Dissolve(0.5)
        Alis "Anyway... is there anything you need, [MC]?"
        scene Sophie_Alis_Scene8 with Dissolve(0.5)
        MC "Uhhhh, nothing... just walking by, getting ready for class!"
        scene Sophie_Alis_Scene9 with Dissolve(0.5)
        Alis "Okay then... see you around!"
        scene Sophie_Alis_Scene10 with Dissolve(0.5)
        MC "{color=#808080}*\"Just walking by?!\" How the fuck did I fumble like that?!*{color=#808080}"
        scene Sophie_Alis_Scene11 with Dissolve(0.5)
        MC "{color=#808080}*Maybe Mhyrorin is right, I'm just a virgin...*{color=#808080}"
        scene BlackScreen with Dissolve(0.5)
        "{color=#808080}**Sophie love + 2**{color=#808080}"
        "{color=#808080}**Alis love + 2**{color=#808080}"
        $ Sophie_love += 2
        $ Alis_love += 2
        $ check_and_update_character_stats("Sophie")
        $ check_and_update_character_stats("Alis")
        $ renpy.call("GameLoop")
