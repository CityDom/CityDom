init python:
    define_images("Anna_Emma_Scene", "ArtClass/Anna_Emma_Scene", "Anna_Emma_Scene", 100)

label ArtClass_AnnaEmma_Scene:
    if Watched_ArtClass_AnnaEmma_Scene:
        MC "{color=#808080}*I already talked to them...*"
        $ renpy.call("GameLoop")
    else:
        $ Watched_ArtClass_AnnaEmma_Scene = True
        scene Anna_Emma_Scene1 with Dissolve(0.5)
        MC "Hey girls, what's up?"
        scene Anna_Emma_Scene2 with Dissolve(0.5)
        Anna "Check this out, Emma. It's the new guy again."
        scene Anna_Emma_Scene3 with Dissolve(0.5)
        Emma "Yeah, he just can't seem to leave us alone."
        scene Anna_Emma_Scene4 with Dissolve(0.5)
        EmmaAndAnna "What do you want?!"
        scene Anna_Emma_Scene5 with Dissolve(0.5)
        MC "Do you two really have to act like complete assholes all the time?!"
        scene Anna_Emma_Scene6 with Dissolve(0.5)
        Anna "Daaaamn, the new guy's got some balls on him."
        Anna "You better watch your back, loser!"
        scene Anna_Emma_Scene7 with Dissolve(0.5)
        MC "Hah, just try and do something funny. You'll see!"
        scene Anna_Emma_Scene6 with Dissolve(0.5)
        Anna "Can't wait. Let's see who'll have the last laugh!"
        scene BlackScreen with Dissolve(0.5)
        "{color=#808080}**Anna love + 2**{color=#808080}"
        "{color=#808080}**Emma love + 2**{color=#808080}"
        $ Anna_love += 2
        $ Emma_love += 2
        $ check_and_update_character_stats("Anna")
        $ check_and_update_character_stats("Emma")
        $ renpy.call("GameLoop")
