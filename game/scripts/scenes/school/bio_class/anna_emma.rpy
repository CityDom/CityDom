init python:
    define_images("BioClass_Anna_Emma_Scene", "BioClass/Anna_Emma", "BioClass_Anna_Emma_Scene", 60)

label BioClass_Anna_Emma_Scene:
    if Watched_BioClass_Anna_Emma_Scene:
        MC "{color=#808080}*I already talked to them...*{color=#808080}"
        $ renpy.call("GameLoop")
    else:
        $ Watched_BioClass_Anna_Emma_Scene = True
        scene BioClass_Anna_Emma_Scene1 with Dissolve(0.5)
        Anna "Yo, Emma, the new guy is passing by."
        Anna "Wanna have some fun?"
        scene BioClass_Anna_Emma_Scene2 with Dissolve(0.5)
        Emma "Hah, of course!"
        scene BioClass_Anna_Emma_Scene3 with Dissolve(0.5)
        MC "Huh..."
        scene BioClass_Anna_Emma_Scene4 with Dissolve(0.5)
        Emma "Hey, new guy! Come here for a second!"
        scene BioClass_Anna_Emma_Scene5 with Dissolve(0.5)
        MC "Ugh... you two again, what do you want?"
        scene BioClass_Anna_Emma_Scene6 with Dissolve(0.5)
        Anna "Awww, come on, don't be so mean!"
        Anna "We just want to get to know our new classmate a little better."
        scene BioClass_Anna_Emma_Scene7 with Dissolve(0.5)
        MC "Yeah, sure..."
        MC "Just tell me what you want already..."
        scene BioClass_Anna_Emma_Scene8 with Dissolve(0.5)
        Emma "We will, we will, just take a seat first. We don't bite."
        scene BioClass_Anna_Emma_Scene9 with Dissolve(0.5)
        Emma "We just wanna talk a little, don't be scared."
        scene BioClass_Anna_Emma_Scene10 with Dissolve(0.5)
        MC "Ughhh... fine..."
        scene BioClass_Anna_Emma_Scene11 with Dissolve(0.5)
        MC "Just get it over with already..."
        scene BioClass_Anna_Emma_Scene12 with Dissolve(0.5)
        Anna "{color=#808080}*Heh, got your ass!*{color=#808080}"
        scene BioClass_Anna_Emma_Scene13 with Dissolve(0.5)
        Emma "{color=#808080}*Haha, loser!*{color=#808080}"
        scene BioClass_Anna_Emma_Scene14 with Dissolve(0.5)
        EmmaAndAnna "Hahahahahaha!!!"
        scene BioClass_Anna_Emma_Scene15 with Dissolve(0.5)
        MC "Fuck... that actually hurt..."
        scene BioClass_Anna_Emma_Scene16 with Dissolve(0.5)
        EmmaAndAnna "Hahahaha, you actually fell for it!"
        scene BioClass_Anna_Emma_Scene17 with Dissolve(0.5)
        Anna "You should've seen your face, hahahaha!!"
        scene BioClass_Anna_Emma_Scene18 with Dissolve(0.5)
        Emma "You are such a loser!!"
        call stat_reward({"Anna": {"love": 2}, "Emma": {"love": 2}})
