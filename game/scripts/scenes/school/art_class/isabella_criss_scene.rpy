init python:
    define_images("Isabella_Criss_Scene", "ArtClass/Isabella_Criss_Scene", "Isabella_Criss_Scene", 100)

label ArtClass_IsabellaCriss_Scene:
    if Watched_ArtClass_IsabellaCriss_Scene:
        MC "{color=#808080}*I already talked to them...*{color=#808080}"
        $ renpy.call("GameLoop")
    else:
        $ Watched_ArtClass_IsabellaCriss_Scene = True
        scene Isabella_Criss_Scene1 with Dissolve(0.5)
        Isabella "Yeah, it's pretty annoying. I can't even walk around the house half-naked anymore."
        scene Isabella_Criss_Scene2 with Dissolve(0.5)
        MC "And why exactly can't you do that anymore?"
        scene Isabella_Criss_Scene3 with Dissolve(0.5)
        Isabella "God damn it, [MC]!"
        Isabella "You scared the shit out of me!"
        scene Isabella_Criss_Scene4 with Dissolve(0.5)
        MC "It's not my fault you get scared so easily."
        MC "So what were you saying? Why can't you walk around half-naked anymore?"
        scene Isabella_Criss_Scene5 with Dissolve(0.5)
        Isabella "Because your ass is creeping around the hallway like a damn ghost."
        scene Isabella_Criss_Scene6 with Dissolve(0.5)
        MC "Can you believe that, Criss?"
        MC "Her dear, loving brother finally comes home, and all she does is complain about me."
        scene Isabella_Criss_Scene7 with Dissolve(0.5)
        Criss "Well... sometimes she talks nicely about you."
        scene Isabella_Criss_Scene8 with Dissolve(0.5)
        MC "Haha, really? Like what?"
        scene Isabella_Criss_Scene9 with Dissolve(0.5)
        Criss "Ummmm... She told me that one time, when you were helping her on the computer, she wanted to—"
        scene Isabella_Criss_Scene10 with Dissolve(0.5)
        Isabella "AAAAAAAAA!!! LALALALALALALALA!!!!!!"
        Isabella "Shut up, Criss!!!!"
        scene Isabella_Criss_Scene11 with Dissolve(0.5)
        MC "Huh? Why? What's wrong?"
        scene Isabella_Criss_Scene12 with Dissolve(0.5)
        Isabella "Nothing, nothing! You know Criss, sometimes she's in her own world."
        scene Isabella_Criss_Scene13 with Dissolve(0.5)
        Criss "But you told me that yesterday, you wanted to see his—"
        scene Isabella_Criss_Scene14 with Dissolve(0.5)
        Isabella "LALALALALALALALALALALALALALALA!!!!"
        scene Isabella_Criss_Scene15 with Dissolve(0.5)
        Isabella "CRISS!!! SHUT THE FUCK UP!!"
        scene Isabella_Criss_Scene16 with Dissolve(0.5)
        Scarlet "ISABELLA!!! WATCH YOUR LANGUAGE!!"
        scene Isabella_Criss_Scene17 with Dissolve(0.5)
        Isabella "I'm sorry, Miss Petal!"
        Isabella "It won't happen again!"
        scene Isabella_Criss_Scene18 with Dissolve(0.5)
        Scarlet "Good! And [MC], go to your seat!"
        "..................."
        scene Isabella_Criss_Scene19 with Dissolve(0.5)
        Scarlet "I'm talking to you, [MC]!!!"
        scene Isabella_Criss_Scene20 with Dissolve(0.5)
        Isabella "Don't make her angry, [MC]! Just go to your seat, don't ignore her!"
        scene Isabella_Criss_Scene21 with Dissolve(0.5)
        Isabella "{color=#808080}*Is he ignoring me as well?*{color=#808080}"
        scene Isabella_Criss_Scene22 with Dissolve(0.5)
        Isabella "{color=#808080}*Oh, right, I'm stupid.*{color=#808080}"
        scene Isabella_Criss_Scene23 with Dissolve(0.5)
        Scarlet "[MC_upper], TO YOUR SEAT, NOW!"
        scene Isabella_Criss_Scene24 with Dissolve(0.5)
        MC "Alright, Miss Petal, I'll go right now!"
        scene Isabella_Criss_Scene25 with Dissolve(0.5)
        MC "{color=#808080}*Geez, why is she so angry? She could've asked nicely...*{color=#808080}"
        scene BlackScreen with Dissolve(0.5)
        "{color=#808080}**Criss love + 2**{color=#808080}"
        "{color=#808080}**Isabella love + 2**{color=#808080}"
        $ Criss_love += 2
        $ Isabella_love += 2
        $ check_and_update_character_stats("Isabella")
        $ check_and_update_character_stats("Criss")
        $ renpy.call("GameLoop")
