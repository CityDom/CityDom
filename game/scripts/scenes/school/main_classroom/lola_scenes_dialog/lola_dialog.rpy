
label LolaClassroomScene:
    if LolaClassroomSceneWatched:
        scene LolaScene6 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to her...*"
        $ renpy.call("GameLoop")
    scene LolaScene6 with Dissolve(0.5)
    MC "Hey, Lola!"
    scene LolaScene1 with Dissolve(0.5)
    Lola "Oh, hey [MC]!"
    scene LolaScene2 with Dissolve(0.5)
    Lola "It's Selina messing with you again?"
    scene LolaScene3 with Dissolve(0.5)
    Selina "Tsk.."
    scene LolaScene4 with Dissolve(0.5)
    MC "Uhh, no, everything is fine."
    MC "I heard that you are in the volleyball team, and I wanted to ask you if you have any matches coming up."
    MC "I like the sport and I heard you are the best in the team, I would love to watch you play sometimes."
    scene LolaScene5 with Dissolve(0.5)
    Lola "Haha, really, I'm not sure if I'm the best in the team, but I do try my best."
    Lola "Sadly, we don't have any matches coming up, but I'll let you know if one comes up."
    scene LolaScene4 with Dissolve(0.5)
    MC "Okay, thanks!"
    call stat_reward({"Lola": {"love": 2}}, return_to=None)
    $ LolaClassroomSceneWatched = True
    $ renpy.call("GameLoop")