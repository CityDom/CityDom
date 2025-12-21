
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
    call stat_reward({"Selina": {"love": 2}}, show_black=False, return_to=None)
    $ SelinaClassroomSceneWatched = True
    $ renpy.call("GameLoop")