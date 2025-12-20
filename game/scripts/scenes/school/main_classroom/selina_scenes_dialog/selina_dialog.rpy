
label SelinaClassroomScene:
    if SelinaClassroomSceneWatched:
        scene SelinaScene1 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to her...*"
        $ renpy.call("GameLoop")
    scene SelinaScene1 with Dissolve(0.5)
    MC "Hey Selina, how are y-"
    scene SelinaScene2 with Dissolve(0.5)
    Selina "I have a boyfriend, fuck off."
    scene SelinaScene1 with Dissolve(0.5)
    MC "{color=#808080}*Bitch...*"
    "{color=#808080}**Selina love + 2**{color=#808080}"
    $ Selina_love = Selina_love + 2
    $ SelinaClassroomSceneWatched = True
    $ check_and_update_character_stats("Selina")
    $ renpy.call("GameLoop")