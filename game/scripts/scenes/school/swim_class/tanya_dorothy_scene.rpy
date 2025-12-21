init python:
    define_images("Pool_Tanya_Dorothy_Scene", "SwimClass/Tanya_Dorothy_Scene", "Pool_Tanya_Dorothy_Scene", 100)

label SwimClass_Tanya_Dorothy_Scene:
    if Watched_SwimClass_Tanya_Dorothy_Scene:
        scene Pool_Tanya_Dorothy_Scene1 with Dissolve(0.5)
        MC "{color=#808080}*I already dealt with this...*"
        $ renpy.call("GameLoop")
    else:
        $ Watched_SwimClass_Tanya_Dorothy_Scene = True

        scene Pool_Tanya_Dorothy_Scene1 with Dissolve(0.5)
        Tanya "Come on, Lola, you know you can go faster than that!"
        scene Pool_Tanya_Dorothy_Scene2 with Dissolve(0.5)
        MC "Miss White, do you have a minute? I wanted to ask—"
        scene Pool_Tanya_Dorothy_Scene3 with Dissolve(0.5)
        Tanya "Oh, [MC], perfect timing, come here!"
        scene Pool_Tanya_Dorothy_Scene4 with Dissolve(0.5)
        TanyaW "Listen here, shrimp, I need you to help me with something!"
        $ MC_whispering = mc_name + " Whispering"
        scene Pool_Tanya_Dorothy_Scene5 with Dissolve(0.5)
        MC_whispering "Uhhhh... I kinda have something else to do right now... the class hasn't started yet..."
        scene Pool_Tanya_Dorothy_Scene6 with Dissolve(0.5)
        TanyaW "Not my problem, you have to get Dorothy off my ass!"
        scene Pool_Tanya_Dorothy_Scene7 with Dissolve(0.5)
        Dorothy "Ummmm, Miss White, what are you doing?"
        scene Pool_Tanya_Dorothy_Scene8 with Dissolve(0.5)
        Tanya "I'll be right back, sweetie, I have something to talk to [MC]."
        scene Pool_Tanya_Dorothy_Scene9 with Dissolve(0.5)
        Dorothy "But you can tell me! I can definitely help, I'm sure I can do a better job!"
        scene Pool_Tanya_Dorothy_Scene10 with Dissolve(0.5)
        MC "{color=#808080}*That's kinda rude... but with Tanya's tits pressing against my arm, I'm not gonna move an inch...*"
        scene Pool_Tanya_Dorothy_Scene11 with Dissolve(0.5)
        Dorothy "It's okay, sweetheart, this job is something only [MC] can help me with."
        scene Pool_Tanya_Dorothy_Scene12 with Dissolve(0.5)
        TanyaW "See?! She's creeping me out! I don't even know what she wants; she already has a ten in my class!"
        TanyaW "And it breaks my heart to tell her to leave me alone; you have to help me!"
        scene Pool_Tanya_Dorothy_Scene13 with Dissolve(0.5)
        MC_whispering "And what do you want me to do?! I don't even know her that well to go talk to her!"
        scene Pool_Tanya_Dorothy_Scene14 with Dissolve(0.5)
        TanyaW "Ughhh... have you ever heard of chit-chat? C'mon, anything!"
        scene Pool_Tanya_Dorothy_Scene13 with Dissolve(0.5)
        MC_whispering "I don't know... small talk is not really a strength of mine... what do I get in return?"
        scene Pool_Tanya_Dorothy_Scene14 with Dissolve(0.5)
        TanyaW "You won't get detention for looking at other girls inappropriately. Now stop breaking my balls and go there!"
        scene Pool_Tanya_Dorothy_Scene13 with Dissolve(0.5)
        MC_whispering "Fine..."
        call stat_reward({"Dorothy": {"love": 2}, "Tanya": {"love": 2}})
