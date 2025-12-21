init python:
    define_images("Pool_Maria_Scene", "SwimClass/Maria_Scene", "Pool_Maria_Scene", 100)

label SwimClass_Maria_Scene:
    if Watched_SwimClass_Maria_Scene:
        scene Pool_Maria_Scene1 with Dissolve(0.5)
        MC "{color=#808080}*I already talked to her about this...*"
        $ renpy.call("GameLoop")
    else:
        $ Watched_SwimClass_Maria_Scene = True
        
        scene Pool_Maria_Scene1 with Dissolve(0.5)
        MC "Why are you sitting here all alone and sad?"
        MC "Don't you want to have fun with your dear classmates?"
        scene Pool_Maria_Scene2 with Dissolve(0.5)
        Maria "Since when are you the one making fun of me? Did the roles reverse without me knowing?"
        scene Pool_Maria_Scene3 with Dissolve(0.5)
        MC "Oh, c'mon, we can't be friends without some back-and-forth banter."
        scene Pool_Maria_Scene4 with Dissolve(0.5)
        Maria "I already told you, we're not friends."
        Maria "We just made a deal... think of it as... I don't know... partners."
        scene Pool_Maria_Scene5 with Dissolve(0.5)
        MC "Well... either way... I don't see anyone else talking to you besides me..."
        scene Pool_Maria_Scene6 with Dissolve(0.5)
        MC "So that's gotta count for something..."
        scene Pool_Maria_Scene7 with Dissolve(0.5)
        Maria "Tsk, cut the crap. What do you want?"
        scene Pool_Maria_Scene8 with Dissolve(0.5)
        MC "Eh, nothing really... I just saw you sitting alone, all bummed out..."
        MC "Which is not out of the ordinary, but usually you're just extremely edgy..."
        scene Pool_Maria_Scene9 with Dissolve(0.5)
        MC "Now you're just... uhhh... sad..."
        scene Pool_Maria_Scene10 with Dissolve(0.5)
        Maria "Could you just get to the point already, Dr. Feel?"
        scene Pool_Maria_Scene11 with Dissolve(0.5)
        MC "Is it about what Selina said back in the locker room?"
        scene Pool_Maria_Scene12 with Dissolve(0.5)
        Maria "Tsk, I already told you it's none of your fucking business!"
        Maria "Just do your part of the deal, and I'll do mine, nothing more, nothing less!"
        scene Pool_Maria_Scene13 with Dissolve(0.5)
        Maria "And stop wasting my time!"
        call stat_reward({"Maria": {"love": 2}})
