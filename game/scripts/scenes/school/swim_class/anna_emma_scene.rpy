init python:
    define_images("Pool_Anna_Emma_Scene", "SwimClass/Anna_Emma_Scene", "Pool_Anna_Emma_Scene", 100)

label SwimClass_AnnaEmma_Scene:
    if Watched_SwimClass_AnnaEmma_Scene:
        MC "{color=#808080}*I already talked to them...*{color=#808080}"
        $ renpy.call("GameLoop")
    else:
        $ Watched_SwimClass_AnnaEmma_Scene = True
        
        if Maria_Report_AnnaAndEmma:
            scene Pool_Anna_Emma_Scene1 with Dissolve(0.5)
            Anna "Watch out, Emma, the new guy is passing!"
            scene Pool_Anna_Emma_Scene2 with Dissolve(0.5)
            MC "I hope you're not going to do another one of your pranks!"
            scene Pool_Anna_Emma_Scene3 with Dissolve(0.5)
            Emma "And if we do? What are you going to do about it?"
            scene Pool_Anna_Emma_Scene4 with Dissolve(0.5)
            MC "Then I'll just make sure to get my payback."
            MC "Or maybe I'll just be one step ahead of you."
            scene Pool_Anna_Emma_Scene5 with Dissolve(0.5)
            Emma "Just try us! You'll see what happens!"
            scene Pool_Anna_Emma_Scene6 with Dissolve(0.5)
            MC "Okay then, you asked for it!"
            scene Pool_Anna_Emma_Scene7 with Dissolve(0.5)
            Emma "KYAAAAAAAAAAA!!!"
            scene Pool_Anna_Emma_Scene8 with Dissolve(0.5)
            MC "Damn brats."
            scene Pool_Anna_Emma_Scene9 with Dissolve(0.5)
            MC "Trying your luck with me like I don't have the biggest pain of a little sister. You two are nothing compared to her!"
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**Anna love + 2**{color=#808080}"
            "{color=#808080}**Emma love + 2**{color=#808080}"
            $ Anna_love += 2 
            $ Emma_love += 2
            $ check_and_update_character_stats("Anna")
            $ check_and_update_character_stats("Emma")
            $ renpy.call("GameLoop")
        else:
            scene Pool_Anna_Emma_Scene1 with Dissolve(0.5)
            Anna "Look, it's the new guy!"
            Anna "Keep moving loser!"
            $ renpy.call("GameLoop")
