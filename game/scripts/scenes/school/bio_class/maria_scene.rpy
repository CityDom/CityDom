init python:
    define_images("BioClass_Maria_Scene", "BioClass/Maria", "BioClass_Maria_Scene", 60)

label BioClass_Maria_Scene:
    if Watched_BioClass_Maria_Scene:
        MC "{color=#808080}*I already talked to her...*{color=#808080}"
        $ renpy.call("GameLoop")
    else:
        $ Watched_BioClass_Maria_Scene = True
        scene BioClass_Maria_Scene1 with Dissolve(0.5)
        MC "Huh? How come you're not sleeping?"
        MC "Did you meet your quota for today?"
        scene BioClass_Maria_Scene2 with Dissolve(0.5)
        Maria "I'm not in the mood right now, [MC]..."
        scene BioClass_Maria_Scene3 with Dissolve(0.5)
        MC "Oh, I get it, you just woke up and you're grumpy."
        MC "I feel you, it happens to me as well."
        scene BioClass_Maria_Scene1 with Dissolve(0.5)
        ".............."
        scene BioClass_Maria_Scene4 with Dissolve(0.5)
        MC "Uhhh, okay then, I will leave you to it..."
        call stat_reward({"Maria": {"love": 2}})
