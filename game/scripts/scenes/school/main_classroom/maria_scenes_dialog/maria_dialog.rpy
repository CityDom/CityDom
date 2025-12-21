
label MariaClassroomScene:
    if MariaClassroomSceneWatched:
        scene MariaScene1 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to her...*"
        $ renpy.call("GameLoop")        
    scene MariaScene1 with Dissolve(0.5)
    MC "Ummmm, Maria?"
    "........."
    MC "Mariaaaaaa!!"
    scene MariaScene2 with Dissolve(0.5)
    Maria "Is the school burning?"
    scene MariaScene3 with Dissolve(0.5)
    MC "No?"
    scene MariaScene4 with Dissolve(0.5)
    Maria "Then let me sleep."
    scene MariaScene1 with Dissolve(0.5)
    MC "...."
    call stat_reward({"Maria": {"love": 2}}, show_black=False, return_to=None)
    $ MariaClassroomSceneWatched = True
    $ renpy.call("GameLoop")