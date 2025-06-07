init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)

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
        scene BlackScreen with Dissolve(0.5)
        "{color=#808080}**Maria love + 2**{color=#808080}"
        $ Maria_love += 2
        $ check_and_update_character_stats("Maria")
        $ renpy.call("GameLoop")
