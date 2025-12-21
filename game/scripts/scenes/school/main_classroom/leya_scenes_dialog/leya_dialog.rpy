
label LeyaClassroomScene:
    if LeyaClassroomSceneWatched:
        scene LeyaScene1 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to her...*"
        $ renpy.call("GameLoop")        
    scene LeyaScene1 with Dissolve(0.5)
    MC "Hey Leya, how are you?"
    scene LeyaScene2 with Dissolve(0.5)
    Leya "Oh, the new guy, I'm good, what's up?"
    scene LeyaScene3 with Dissolve(0.5)
    MC "I was thinking about joining the gymnastic club, is there anyone I should talk to or-"
    scene LeyaScene4 with Dissolve(0.5)
    Leya "Uhhhh, I don't think the teacher accepts men in the class... sorry..."
    scene LeyaScene5 with Dissolve(0.5)
    MC "Oh, it's okay, no need to feel sorry for it."
    call stat_reward({"Leya": {"love": 2}}, show_black=False, return_to=None)
    $ LeyaClassroomSceneWatched = True
    $ renpy.call("GameLoop")
    #! Maybe you could teach me -- future idea