init python:
    define_images("BioClass_Lola_Leya_Scene", "BioClass/Lola_Leya", "BioClass_Lola_Leya_Scene", 60)

label BioClass_Lola_Leya_Scene:
    if Watched_BioClass_Lola_Leya_Scene:
        MC "{color=#808080}*I already talked to them...*{color=#808080}"
        $ renpy.call("GameLoop")
    else:
        $ Watched_BioClass_Lola_Leya_Scene = True
        scene BioClass_Lola_Leya_Scene1 with Dissolve(0.5)
        MC "Hey girls, what are you doing?"
        scene BioClass_Lola_Leya_Scene2 with Dissolve(0.5)
        Lola "I'm trying to get Leya to understand the periodic table. Teach' told us to remember most of it for the exam."
        scene BioClass_Lola_Leya_Scene3 with Dissolve(0.5)
        Leya "I mean... this is actually stupid, how are we supposed to remember all this stuff?"
        scene BioClass_Lola_Leya_Scene4 with Dissolve(0.5)
        MC "And I guess it's not going too well, huh?"
        scene BioClass_Lola_Leya_Scene5 with Dissolve(0.5)
        Lola "Uhhh... I don't wanna say she's dumb... She's just... not that gifted academically..."
        scene BioClass_Lola_Leya_Scene6 with Dissolve(0.2)
        $ renpy.pause(0.01, hard=True)
        scene BioClass_Lola_Leya_Scene7 with Dissolve(0.2)
        $ renpy.pause(0.01, hard=True)
        scene BioClass_Lola_Leya_Scene8 with Dissolve(0.2)
        $ renpy.pause(0.01, hard=True)
        scene BioClass_Lola_Leya_Scene9 with Dissolve(0.2)
        Leya "Tsk, I'm right next to you, asshole!"
        scene BioClass_Lola_Leya_Scene10 with Dissolve(0.5)
        Lola "Auuuch, what was that for?!"
        scene BioClass_Lola_Leya_Scene11 with Dissolve(0.5)
        MC "I think it was for calling her dumb as rocks and mentally challenged..."
        scene BioClass_Lola_Leya_Scene12 with Dissolve(0.5)
        MC "To be honest with you, Leya, I wouldn't just stay there and take that, but that's just me though."
        scene BioClass_Lola_Leya_Scene14 with Dissolve(0.5)
        MC "That was really messed up of you to say, Lola!"
        scene BioClass_Lola_Leya_Scene15 with Dissolve(0.5)
        Lola "Whaaaaaat?! But I didn't even say that!!!"
        scene BioClass_Lola_Leya_Scene13 with Dissolve(0.5)
        Leya "Rrrrrrrgh!"
        scene BioClass_Lola_Leya_Scene16 with Dissolve(0.5)
        Lola "Wait, what the fuck?! Leya, I didn't say any of that, you were right next to me, you heard what I said!"
        scene BioClass_Lola_Leya_Scene17 with Dissolve(0.5)
        MC "{color=#808080}*Ah, she's already growling, I don't think there's any stopping her now.*{color=#808080}"
        scene BioClass_Lola_Leya_Scene18 with Dissolve(0.5)
        $ renpy.pause(0.05, hard=True)
        scene BioClass_Lola_Leya_Scene19 with Dissolve(0.5)
        $ renpy.pause(0.05, hard=True)
        scene BioClass_Lola_Leya_Scene18 with Dissolve(0.5)
        $ renpy.pause(0.03, hard=True)
        scene BioClass_Lola_Leya_Scene19 with Dissolve(0.5)
        Leya "Yuh ashool, wyy ar yuh sho meen!!"
        scene BioClass_Lola_Leya_Scene20 with Dissolve(0.5)
        Leya "Tehk thihs!"
        scene BioClass_Lola_Leya_Scene21 with Dissolve(0.5)
        Leya "An thihs!"
        scene BioClass_Lola_Leya_Scene20 with Dissolve(0.5)
        Leya "An thihs!"
        scene BioClass_Lola_Leya_Scene22 with Dissolve(0.5)
        MC "If we ever get in a fight, can I try this strategy as well? Though it doesn't seem that effective..."
        scene BioClass_Lola_Leya_Scene23 with Dissolve(0.5)
        Leya "MMMMFFMFMHHHH!!!"
        scene BioClass_Lola_Leya_Scene24 with Dissolve(0.5)
        Lola "Stop joking, [MC], talk to her! She's not stopping any time soon!"
        scene BioClass_Lola_Leya_Scene25 with Dissolve(0.5)
        MC "Uhhh, I really have to go now... you know?"
        MC "So she's all yours, good luck!"
        scene BioClass_Lola_Leya_Scene26 with Dissolve(0.5)
        Lola "God damn it, [MC]..."
        call stat_reward({"Leya": {"love": 2, "corruption": 2}, "Lola": {"love": 2, "corruption": 2}})
