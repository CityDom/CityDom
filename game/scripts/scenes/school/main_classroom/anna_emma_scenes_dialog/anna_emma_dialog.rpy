
label AnnaEmmaClassroomScene:
    if AnnaEmmaClassroomSceneWatched:
        scene AnnaEmmaScene1 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to them.*"
        $ renpy.call("GameLoop")
    scene AnnaEmmaScene1 with Dissolve(0.5)
    MC "Hey girls!"
    scene AnnaEmmaScene2 with Dissolve(0.5)
    Emma "Uhhhh... is he talking to us?"
    scene AnnaEmmaScene3 with Dissolve(0.5)
    Anna "Ummmm... I think.. I'm not sure..."
    scene AnnaEmmaScene4 with Dissolve(0.5)
    Emma "What do you want?"
    scene AnnaEmmaScene5 with Dissolve(0.5)
    MC "I-"
    scene AnnaEmmaScene4 with Dissolve(0.5)
    Emma "We don't care."
    scene AnnaEmmaScene6 with Dissolve(0.5)
    Anna "Yeah, we don't care."
    Anna "Get lost!"
    scene AnnaEmmaScene4 with Dissolve(0.5)
    Emma "Yeah, get lost!"
    scene AnnaEmmaScene1 with Dissolve(0.5)
    MC "{color=#808080}*Tsk, They are meaner than I thought.*"
    call stat_reward({"Anna": {"love": 2}, "Emma": {"love": 2}}, show_black=False, return_to=None)
    $ AnnaEmmaClassroomSceneWatched = True
    $ renpy.call("GameLoop")