init python:
    define_images("ArtClass_Maria_Scene", "ArtClass/Maria_Scene", "ArtClass_Maria_Scene", 100)

label ArtClass_Maria_Scene:
    if Watched_ArtClass_Maria_Scene:
        MC "{color=#808080}*I already talked to her...*{color=#808080}"
        $ renpy.call("GameLoop")
    else:
        $ Watched_ArtClass_Maria_Scene = True
        scene ArtClass_Maria_Scene1 with Dissolve(0.5)
        MC "So... ummm... why aren't there any chairs in this class?"
        scene ArtClass_Maria_Scene2 with Dissolve(0.5)
        Maria "Because Miss Petal tries to be different and switch things up, I guess..."
        Maria "And to truly put your heart into the thing that you're painting, you have to stand up straight or some shit like that."
        Maria "I don't know, it's just a pain in the ass if you ask me."
        scene ArtClass_Maria_Scene3 with Dissolve(0.5)
        MC "Yeah... fifty minutes of standing up straight sounds pretty stupid."
        scene ArtClass_Maria_Scene4 with Dissolve(0.5)
        "................"
        scene ArtClass_Maria_Scene3 with Dissolve(0.5)
        MC "Aaaaand... uhhh... anything else?"
        MC "What are you watching? Is that a game?"
        scene ArtClass_Maria_Scene5 with Dissolve(0.5)
        Maria "Yeah... I was checking if any updates came up..."
        scene ArtClass_Maria_Scene6 with Dissolve(0.5)
        Maria "Anyway, what do you want? Don't you have anyone else to talk to?"
        scene ArtClass_Maria_Scene7 with Dissolve(0.5)
        MC "Did you forget we're sitting next to each other? Why do you have to be such a bitch? Do you get a kick out of it or something?"
        scene ArtClass_Maria_Scene8 with Dissolve(0.5)
        Maria "Hmm... I never really thought about it..."
        Maria "I guess I do a little..."
        scene ArtClass_Maria_Scene7 with Dissolve(0.5)
        MC "Yeah, not surprising at all... in any case, I wanted to ask you what exactly we'll be doing in this class."
        scene ArtClass_Maria_Scene8 with Dissolve(0.5)
        Maria "Just wait and you'll see. Miss Petal really tries her hardest to stand out as a teacher..."
        call stat_reward({"Maria": {"love": 2}})
