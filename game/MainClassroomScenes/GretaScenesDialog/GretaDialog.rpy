
label GretaClassroomScene:
    if GretaClassroomSceneWatched:
        scene GretaScene1 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to her...*"
        $ renpy.call("GameLoop")
    scene GretaScene1 with Dissolve(0.5)
    MC "Hey, Greta, what's up!"
    "......"
    MC "Ummm.... Greta?"
    scene GretaScene3 with Dissolve(0.5)
    Greta "What do you want?! Leave me alone, I have to concentrate!"
    scene GretaScene2 with Dissolve(0.5)
    Greta "Oh, [MC], I didn't realize it was you, sorry but I don't have time right now."
    Greta "I have to revise the lesson before the class starts!"
    scene GretaScene4 with Dissolve(0.5)
    MC "Oh, okay, good luck with that!"
    scene GretaScene5 with Dissolve(0.5)
    Greta "Thank you, [MC]!"
    "{color=#808080}**Greta love + 2**{color=#808080}"
    $ Greta_love = Greta_love + 2
    $ GretaClassroomSceneWatched = True
    $ check_and_update_character_stats("Greta")
    $ renpy.call("GameLoop")