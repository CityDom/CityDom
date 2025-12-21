
label CrissClassroomScene:
    if CrissClassroomSceneWatched:
        scene CrissScene1 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to her...*"
        $ renpy.call("GameLoop")

    scene CrissScene1 with Dissolve(0.5)
    MC "Ummmm, Criss?"
    scene CrissScene2 with Dissolve(0.5)
    Criss "Uhhh, yeah?"
    scene CrissScene3 with Dissolve(0.5)
    MC "Are you coming to our house this weekend?"
    scene CrissScene2 with Dissolve(0.5)
    Criss "Ummmm..."
    scene CrissScene4 with Dissolve(0.5)
    Isabella "Why do you care?!"
    scene CrissScene5 with Dissolve(0.5)
    MC "So I could not get scare jumped when I get out of my room naked on a radom saturday."
    MC "And why are you even getting involved in this conversation? I was talking to Criss!"
    scene CrissScene6 with Dissolve(0.5)
    Criss "Heyyy, don't get in a fight over this."
    Criss "Yeah, I will most likely come over, is there a problem?"
    scene CrissScene7 with Dissolve(0.5)
    MC "Okay, that's all I wanted to know."
    call stat_reward({"Criss": {"love": 2}}, show_black=False, return_to=None)
    $ CrissClassroomSceneWatched = True
    $ renpy.call("GameLoop")