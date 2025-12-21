
label DorothyClassroomScene:
    if DorothyClassroomSceneWatched:
        scene DorothyScene1 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to her...*"
        $ renpy.call("GameLoop")

    scene DorothyScene1 with Dissolve(0.5)
    MC "Hey, Dorothy, how are you doing?"
    Dorothy "Hey, [MC], you have to pay the class fund, and don't be late or the teacher will be mad at me, not you."
    Dorothy "Also, stop leaving trash at your desk."
    Dorothy "And you have 2 strikes in my notebook for harassing girls, one more and I'm telling Miss Thompson!"
    MC "So... uhhh... I guess you're doing fine?"
    scene DorothyScene2 with Dissolve(0.5)
    Dorothy "Oh, yeah, I'm doing okay, thank you for asking!"
    Dorothy "I have to finish this report for Miss Thompson, but we can talk later!"
    call stat_reward({"Dorothy": {"love": 2}}, show_black=False, return_to=None)
    $ DorothyClassroomSceneWatched = True
    $ renpy.call("GameLoop")