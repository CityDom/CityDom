
label SophieClassroomScene:
    if SophieClassroomSceneWatched:
        scene SophieScene1 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to her...*"
        $ renpy.call("GameLoop")        
    scene SophieScene1 with Dissolve(0.5)
    MC "Hey, Sophie!"
    scene SophieScene2 with Dissolve(0.5)
    Sophie "Oh, hey...."
    scene SophieScene3 with Dissolve(0.5)
    Sophie "Uhhhhh.... ummmm... uhhhhh"
    MC "[MC].."
    scene SophieScene4 with Dissolve(0.5)
    Sophie "Yea! Right! [MC]!"
    Sophie "The new guy! You want me to show you around the school?"
    Sophie "Need help with something? I'll see what I can do!"
    Sophie "I don't want to seem pushy or something."
    Sophie "I'm just always glad to help a new collogue."
    Sophie "It must be so hard for you in here, being new to everything."
    scene SophieScene5 with Dissolve(0.5)
    MC "Oh, thank you, that's great, I was actually wondering if you could help me wi-"
    scene SophieScene6 with Dissolve(0.5)
    Sophie "Uhhh... I can't really help you with that right now... sorry..."
    scene SophieScene5 with Dissolve(0.5)
    MC "But I didn't even tell you wh-"
    scene SophieScene7 with Dissolve(0.5)
    Sophie "Yea, I get it, I understand, I'm so sorry for you!"
    Sophie "But I really can't right now, you must hate me for it, I understand."
    Sophie "Please don't be mad at me!"
    scene SophieScene8 with Dissolve(0.5)
    MC "Uhhh.. no, it's alright, it wasn't that big of a deal anywa-"
    scene SophieScene9 with Dissolve(0.5)
    Sophie "Ahhh, I'm so relieved to hear that, talk to you later then."
    scene SophieScene10 with Dissolve(0.5)
    MC "{color=#808080}*Damn... a simple fuck off would've been better...*"
    call stat_reward({"Sophie": {"love": 2}}, show_black=False, return_to=None)
    $ SophieClassroomSceneWatched = True
    $ renpy.call("GameLoop")