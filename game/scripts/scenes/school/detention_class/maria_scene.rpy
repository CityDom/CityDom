init python:
    define_images("DetentionClass_Maria_Scene", "DetentionClass/Maria_Scene", "DetentionClass_Maria_Scene", 100)

label DetentionClass_Maria_Scene:
    if not Watched_detention_Maria_Scene:
        $ Watched_detention_Maria_Scene = True
        scene DetentionClass_Maria_Scene1 with Dissolve(0.5)
        $ MC_whispering = mc_name + " Whispering"
        MC_whispering "Maria!"
        MC_whispering "Pssst, Maria!"
        scene DetentionClass_Maria_Scene2 with Dissolve(0.5)
        Sandra "No talking in detention, [MC]!!"
        scene DetentionClass_Maria_Scene3 with Dissolve(0.5)
        MC "But the detention didn't even start!"
        scene DetentionClass_Maria_Scene4 with Dissolve(0.5)
        pause
        scene DetentionClass_Maria_Scene5 with Dissolve(0.5)
        Sandra "Tsk..."
        scene DetentionClass_Maria_Scene6 with Dissolve(0.5)
        Sandra "{color=#808080}*Whatever.*"
        scene DetentionClass_Maria_Scene7 with Dissolve(0.5)
        MC "{color=#808080}*Oh, wow, I'm surprised she dropped it that easily...*"
        scene DetentionClass_Maria_Scene8 with Dissolve(0.5)
        MC_whispering "Pst! Maria!"
        scene DetentionClass_Maria_Scene9 with Dissolve(0.5)
        MC "{color=#808080}*Alright, she seems to be sleeping.*"
        scene DetentionClass_Maria_Scene10 with Dissolve(0.5)
        MC "{color=#808080}*And Miss Nadal is not paying attention, this is perfect!*"
        scene DetentionClass_Maria_Scene11 with Dissolve(0.5)
        MC "{color=#808080}*Now I just have to make sure she doesn't see me!*"
        scene DetentionClass_Maria_Scene12 with Dissolve(0.5)
        MC "{color=#808080}*Fuck... I'm usually not this nervous...*"
        scene DetentionClass_Maria_Scene13 with Dissolve(0.5)
        MC "{color=#808080}*But they feel so good!*"
        scene DetentionClass_Maria_Scene14 with Dissolve(0.5)
        $ renpy.pause(0.5, hard=True)
        scene DetentionClass_Maria_Scene13 with Dissolve(0.5)
        $ renpy.pause(0.5, hard=True)
        scene DetentionClass_Maria_Scene14 with Dissolve(0.5)
        $ renpy.pause(0.5, hard=True)
        scene DetentionClass_Maria_Scene13 with Dissolve(0.5)
        $ renpy.pause(0.5, hard=True)
        scene DetentionClass_Maria_Scene14 with Dissolve(0.5)
        MC "{color=#808080}*They are the softest thing I've ever touched!*"
        scene DetentionClass_Maria_Scene15 with Dissolve(0.5)
        MC "........."
        MC "{color=#808080}*Well... shit...*"
        scene DetentionClass_Maria_Scene16 with Dissolve(0.5)
        MariaW "Just because I'm not answering you, it doesn't mean I'm asleep, you know that right?"
        scene DetentionClass_Maria_Scene17 with Dissolve(0.5)
        MC_whispering "Uhhh, yeah, of course!"
        scene DetentionClass_Maria_Scene18 with Dissolve(0.5)
        MariaW "Then take that hand off my tits before I cut it!"
        MC_whispering "Yes Ma'am!"
        call stat_reward({"Maria": {"love": -2, "corruption": -2}}, return_to=None)
    else:
        scene DetentionClass_Maria_Scene1 with Dissolve(0.5)
        MC "I already talked to her about that."
        $ renpy.call("GameLoop")