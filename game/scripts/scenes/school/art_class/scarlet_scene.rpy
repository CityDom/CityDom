init python:
    define_images("ArtClass_Scarlet_Scene", "ArtClass/ArtClass_Scarlet_Scene", "ArtClass_Scarlet_Scene", 100)

label ArtClass_Scarlet_Scene:
    scene ArtClass_Scarlet_Scene2 with Dissolve(0.5)
    MC "Ummmm... Miss Petal?"
    scene ArtClass_Scarlet_Scene1 with Dissolve(0.5)
    Scarlet "Yes, [MC], what's the matter? Everything alright?"
    scene ArtClass_Scarlet_Scene3 with Dissolve(0.5)
    menu:
        "Talk":
            jump scarletTalk_menu
        "Leave":
            scene ArtClass_Scarlet_Scene2 with Dissolve(0.5)
            MC "Uhhh, nothing, I just wanted to ask what we'll be doing in class today."
            scene ArtClass_Scarlet_Scene1 with Dissolve(0.5)
            Scarlet "Wait for the class to start and you'll see."
            $ renpy.call("GameLoop")

label scarletTalk_menu:
    scene ArtClass_Scarlet_Scene3
    menu:
        "What do you think about me?":
            if not Watched_ArtClass_WDYTScarlet_Scene:
                $ Watched_ArtClass_WDYTScarlet_Scene = True
                MC "I wanted to ask you, what do you think about me?"
                scene ArtClass_Scarlet_Scene4 with Dissolve(0.5)
                Scarlet "You seem to be doing alright, [MC]. You have an inclination for art."
                Scarlet "But you should focus on the things that I'm telling you to do."
                scene ArtClass_Scarlet_Scene3 with Dissolve(0.5)
                MC "I meant what you think of me, in general."
                scene ArtClass_Scarlet_Scene5 with Dissolve(0.5)
                Scarlet "Uhhh... Just don't cause the rest of the class any problems, and you should be alright."
                Scarlet "And stop asking weird questions."
                jump scarletTalk_menu
            else:
                MC "{color=#808080}*I already talked to her about that...*"
                jump scarletTalk_menu

        "Compliment":
            if not Watched_ArtClass_ComplimentScarlet_Scene:
                $ Watched_ArtClass_ComplimentScarlet_Scene = True
                MC "I just wanted to let you know that your hair looks amazing, Miss Petal."
                scene ArtClass_Scarlet_Scene6 with Dissolve(0.5)
                Scarlet "Aww, thank you, [MC]. That's sweet."
                Scarlet "It's all over the place lately, and I can't seem to find a style for it."
                scene ArtClass_Scarlet_Scene7 with Dissolve(0.5)
                MC "You already have a style for it, Miss Petal!"
                MC "The messy look totally fits you!"
                scene ArtClass_Scarlet_Scene8 with Dissolve(0.5)
                Scarlet "Thank you, [MC]. I knew you had a good eye!"
                Scarlet "Now go back to your seat. Class is about to start."
                call stat_reward({"Scarlet": {"love": 2}})
            else:
                MC "{color=#808080}*I already talked to her about that...*"
                jump scarletTalk_menu

        "Pervert compliment":
            if not Watched_ArtClass_PervertComplimentScarlet_Scene:
                $ Watched_ArtClass_PervertComplimentScarlet_Scene = True
                MC "This robe isn't really complimenting your figure, Miss Petal."
                scene ArtClass_Scarlet_Scene9 with Dissolve(0.5)
                MC "And even so, all of your good parts are still sticking out."
                MC "You are truly blessed in that regard, Miss Petal!"
                scene ArtClass_Scarlet_Scene10 with Dissolve(0.5)
                Scarlet "This is no way to talk to a teacher, young man!"
                Scarlet "Now go back to your seat before I get mad!"
                scene ArtClass_Scarlet_Scene11 with Dissolve(0.5)
                MC "But Miss Petal, I didn't mean it in a bad way! I-"
                scene ArtClass_Scarlet_Scene12 with Dissolve(0.5)
                Scarlet "I DON'T CARE HOW YOU MEANT IT, [MC_upper]!"
                Scarlet "GO BACK TO YOUR PLACE RIGHT NOW!!!!"
                scene BlackScreen with Dissolve(0.5)
                MC "{color=#808080}*Geez... She really flies off the handle pretty quick...*{color=#808080}"
                call stat_reward({"Scarlet": {"love": -2, "corruption": 2}}, show_black=False)
            else:
                MC "{color=#808080}*I already talked to her about that...*"
                jump scarletTalk_menu

        "Insult":
            if not Watched_ArtClass_InsultScarlet_Scene:
                $ Watched_ArtClass_InsultScarlet_Scene = True
                scene ArtClass_Scarlet_Scene13 with Dissolve(0.5)
                MC "I just wanted to tell you that you should work on your attitude, Miss Petal."
                MC "This whole bipolar thing you’ve got going on is not really working for me."
                MC "So try to be better, alright?"
                scene ArtClass_Scarlet_Scene13 with Dissolve(0.5)
                Scarlet "UNDER NO CIRCUMSTANCE ARE YOU ALLOWED TO TALK LIKE THIS TO A TEACHER, [MC_upper]!!!"
                Scarlet "I DON'T CARE WHAT YOU THINK ABOUT MY ATTITUDE!!"
                Scarlet "NOW GO BACK TO YOUR SEAT RIGHT NOW!!"
                call stat_reward({"Scarlet": {"love": -2, "corruption": -2}})
            else:
                MC "{color=#808080}*I already talked to her about that...*"
                jump scarletTalk_menu

        "Leave":
            MC "I have to go, Miss Petal. Sorry for bothering you."
            scene BlackScreen with Dissolve(0.5)
            $ renpy.call("GameLoop")
