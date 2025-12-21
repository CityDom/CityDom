init python:
    define_images("Isa_Criss_Helena_Scene", "BioClass/Isa_Criss_Helena", "Isa_Criss_Helena_Scene", 60)

label BioClass_IsaCrissHelena_Scene:
    if Watched_BioClass_IsaCrissHelena_Scene:
        MC "{color=#808080}*I already talked to them...*{color=#808080}"
        $ renpy.call("GameLoop")
    else:
        $ Watched_BioClass_IsaCrissHelena_Scene = True
        scene Isa_Criss_Helena_Scene1 with Dissolve(0.5)
        Criss "Come on, Isa! Stop touching it, the teacher is going to yell at us!"
        scene Isa_Criss_Helena_Scene2 with Dissolve(0.5)
        Isabella "Calm down, Criss, she won't know. And Helena is touching it too, why aren't you yelling at her as well?"
        scene Isa_Criss_Helena_Scene3 with Dissolve(0.5)
        Helena "Huh? But I'm not even touching it!"
        Helena "I'm just... uhhh... admiring it closely!"
        scene Isa_Criss_Helena_Scene4 with Dissolve(0.5)
        MC "Do you have any idea how much this thing costs, Isa?"
        scene Isa_Criss_Helena_Scene5 with Dissolve(0.5)
        Isabella "Nope, why don't you tell me, smart guy!"
        scene Isa_Criss_Helena_Scene6 with Dissolve(0.5)
        MC "I don't know, but I can tell you it's waaaay above what we can pay."
        scene Isa_Criss_Helena_Scene7 with Dissolve(0.5)
        Isabella "Ugh, here you go again, ruining my fun."
        Isabella "Why don't you scold Helena, huh? She's doing the same thing!"
        scene Isa_Criss_Helena_Scene8 with Dissolve(0.5)
        Helena "I told you I'm not touching it! Stop being so unfair!"
        scene Isa_Criss_Helena_Scene9 with Dissolve(0.5)
        Helena "This is what touching looks like, do you see the difference?"
        scene Isa_Criss_Helena_Scene10 with Dissolve(0.5)
        MC "{color=#808080}*Uhhh... this turned unexpectedly pleasant all of a sudden...*{color=#808080}"
        scene Isa_Criss_Helena_Scene11 with Dissolve(0.5)
        Criss "{color=#808080}*Uhhhhh... she's not going to react well to this.*{color=#808080}"
        scene Isa_Criss_Helena_Scene12 with Dissolve(0.5)
        Criss "{color=#808080}*Oh god, there she goes...*{color=#808080}"
        scene Isa_Criss_Helena_Scene13 with Dissolve(0.5)
        Isabella "Keep your hands to yourself, moss head."
        scene Isa_Criss_Helena_Scene14 with Dissolve(0.5)
        Helena "{color=#808080}*Hehe, I struck a chord here.*{color=#808080}"
        scene Isa_Criss_Helena_Scene15 with Dissolve(0.5)
        Helena "C'mon, Isa, you know I'm just playing, why are you getting so riled up?"
        scene Isa_Criss_Helena_Scene16 with Dissolve(0.5)
        Isabella "Uhhh, haha, I'm not getting riled up, I knew you were just playing, haha!"
        scene Isa_Criss_Helena_Scene17 with Dissolve(0.5)
        Criss "{color=#808080}*You were about to jump her...*{color=#808080}"
        scene Isa_Criss_Helena_Scene18 with Dissolve(0.5)
        Isabella "But that's enough playing around, knock it off."
        scene Isa_Criss_Helena_Scene19 with Dissolve(0.5)
        Helena "But you heard him, we are not allowed to touch the skeleton, and we are in biology, how else am I supposed to learn?"
        scene Isa_Criss_Helena_Scene20 with Dissolve(0.5)
        MC "{color=#808080}*Do I have to say something? Do I shut up?*{color=#808080}"
        scene Isa_Criss_Helena_Scene21 with Dissolve(0.5)
        Criss "Ummm... girls?"
        scene Isa_Criss_Helena_Scene22 with Dissolve(0.5)
        Isabella "Stay out of it, Criss!"
        scene Isa_Criss_Helena_Scene23 with Dissolve(0.5)
        MC "{color=#808080}*The answer is to shut the fuck up, okay, got it!*{color=#808080}"
        scene Isa_Criss_Helena_Scene24 with Dissolve(0.5)
        Helena "Okay, girl, sheesh..."
        scene Isa_Criss_Helena_Scene25 with Dissolve(0.5)
        Helena "I told you, I'm just messing around."
        scene Isa_Criss_Helena_Scene26 with Dissolve(0.5)
        Helena "Anyway, do you wanna play with the skeleton more? I think I know how to detach the ribs!"
        scene Isa_Criss_Helena_Scene27 with Dissolve(0.5)
        Isabella "Wait, really?! Haha, yeah, let's do it!"
        scene Isa_Criss_Helena_Scene28 with Dissolve(0.5)
        MC "I told you, Isa, you shouldn't play with the sk—"
        scene Isa_Criss_Helena_Scene29 with Dissolve(0.5)
        IsaAndHelena "Oh, shut up already!"
        scene Isa_Criss_Helena_Scene30 with Dissolve(0.5)
        Criss "{color=#808080}*Ughhh... [MC], how did you make things worse than they already were?*{color=#808080}"
        call stat_reward({"Criss": {"love": 2}, "Helena": {"love": 2}, "Isabella": {"love": 2}}, dissolve_time=1)
