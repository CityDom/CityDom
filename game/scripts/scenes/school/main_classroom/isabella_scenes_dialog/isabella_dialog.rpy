
label IsabellaClassroomScene:
    if IsabellaClassroomSceneWatched:
        scene IsabellaScene1 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to her...*"
        $ renpy.call("GameLoop")
    scene IsabellaScene1 with Dissolve(0.5)
    MC "Hey Isabella!"
    scene IsabellaScene2 with Dissolve(0.5)
    Isabella "Hey [MC], what's up."
    scene IsabellaScene3 with Dissolve(0.5)
    MC "Are we walking home together today?"
    scene IsabellaScene2 with Dissolve(0.5)
    Isabella "Uhh, no, I'm going with Criss."
    scene IsabellaScene3 with Dissolve(0.5)
    MC "Oke, talk to you later then."
    call stat_reward({"Isabella": {"love": 2}}, return_to=None)
    $ IsabellaClassroomSceneWatched = True
    $ renpy.call("GameLoop")