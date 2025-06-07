
label HelenaClassroomScene:
    if HelenaClassroomSceneWatched:
        scene HelenaScene1 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to her...*"
        $ renpy.call("GameLoop")
    scene HelenaScene1 with Dissolve(0.5)
    MC "Hey, Helena, what's up!"
    scene HelenaScene2 with Dissolve(0.5)
    Helena "Hey, [MC], nothing much, just trying to get Sophie to understand a few things."
    scene HelenaScene3 with Dissolve(0.5)
    Sophie "Ummm, we were talking here!"
    scene HelenaScene4 with Dissolve(0.5)
    Alis "Just let them speak Sophie, you are not going to learn 12 years of math in 10 minutes."
    scene HelenaScene5 with Dissolve(0.5)
    Sophie "Hmph!"
    scene HelenaScene6 with Dissolve(0.5)
    Helena "Haha, don't mind Sophie, she is just a little possessive."
    scene HelenaScene7 with Dissolve(0.5)
    Sophie "I'm not possessive at all! What are you talking abo-"
    scene HelenaScene8 with Dissolve(0.5)
    Alis "Sophie!!!"
    Sophie "Hmph!"
    scene HelenaScene9 with Dissolve(0.5)
    Helena "Anyway, how about you?"
    scene HelenaScene10 with Dissolve(0.5)
    MC "I'm fine, I just wanted to ask you if-"
    scene HelenaScene11 with Dissolve(0.5)
    Helena "Uhhh, sorry to interrupt you, but I really have to get Sophie to understand the most simple math before the class starts."
    Helena "But we can talk after the class!"
    scene HelenaScene12 with Dissolve(0.5)
    MC "It's okay, we can talk later."
    "{color=#808080}**Helena love + 2**{color=#808080}"
    $ Helena_love = Helena_love + 2
    $ HelenaClassroomSceneWatched = True
    $ check_and_update_character_stats("Helena")
    $ renpy.call("GameLoop")