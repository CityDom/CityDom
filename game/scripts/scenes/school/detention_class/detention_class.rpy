init python:
    define_images("DetentionClass_Scene", "DetentionClass/DetentionClass", "DetentionClass_Scene", 100)
    renpy.image("Detention_BalanceTraining1_1", Movie(play="images/DetentionClass/DetentionClass/Detention_BalanceTraining1_1.webm", loop=True, group="pov_group"))
    renpy.image("Detention_BalanceTraining2_1", Movie(play="images/DetentionClass/DetentionClass/Detention_BalanceTraining2_1.webm", loop=True, group="pov_group"))
    renpy.image("Detention_BalanceTraining2_2", Movie(play="images/DetentionClass/DetentionClass/Detention_BalanceTraining2_2.webm", loop=True, group="pov_group"))
    renpy.image("Detention_BalanceTraining2_3", Movie(play="images/DetentionClass/DetentionClass/Detention_BalanceTraining2_3.webm", loop=True, group="pov_group"))

label DetentionClass_Scene:
    scene DetentionClass_Scene1 with Dissolve(0.5)
    "{color=#808080}**RING RING RING**{/color}"
    scene DetentionClass_Scene2 with Dissolve(0.5)
    Sandra "Alright, break is over!"
    scene DetentionClass_Scene3 with Dissolve(0.5)
    Sandra "Stop talking!"
    scene DetentionClass_Scene4 with Dissolve(0.5)
    Sandra "And no sleeping!!"
    scene DetentionClass_Scene5 with Dissolve(0.5)
    Maria "I'm sorry, my head is hurting a little..."
    scene DetentionClass_Scene6 with Dissolve(0.5)
    Sandra "Sometimes my head hurts as well, but you don't see me sleeping!"
    scene DetentionClass_Scene7 with Dissolve(0.5)
    Maria "{color=#808080}*Tsk... annoying bitch...*{/color}"
    scene DetentionClass_Scene8 with Dissolve(0.5)
    Sandra "Also, no phones and no homework."
    scene DetentionClass_Scene9 with Dissolve(0.5)
    MC "Can we at least—"
    scene DetentionClass_Scene10 with Dissolve(0.5)
    Sandra "I said no talking, can't you follow simple instructions?"
    Sandra "Are you that dumb?"
    scene DetentionClass_Scene11 with Dissolve(0.5)
    MC "......"
    scene DetentionClass_Scene10 with Dissolve(0.5)
    Sandra "I asked you a question, didn't you learn that it's polite to answer?"
    scene DetentionClass_Scene12 with Dissolve(0.5)
    MC "Yes, Miss Nadal, I am du—"
    scene DetentionClass_Scene13 with Dissolve(0.5)
    Sandra "Of course you are, it was a rhetorical question, but I don't think you know what that is either..."
    scene DetentionClass_Scene14 with Dissolve(0.5)
    MC "{color=#808080}*Jesus Christ, does this bitch have a humiliation fetish, or does she really hate me that much?!*{/color}"
    Maria "{color=#808080}*This is going to be hell...*{/color}"
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}**20 minutes later...**{/color}"
    scene DetentionClass_Scene15 with Dissolve(0.5)
    "...................."
    scene DetentionClass_Scene16 with Dissolve(0.5)
    Sandra "Alright, I have to leave for a few minutes..."
    scene DetentionClass_Scene17 with Dissolve(0.5)
    Sandra "You two better not make a sound!"
    scene DetentionClass_Scene18 with Dissolve(0.5)
    Maria "Ughhh, she finally left, how can she just sit doing nothing for this long?!"
    scene DetentionClass_Scene19 with Dissolve(0.5)
    Maria "How are you holding up?"
    scene DetentionClass_Scene20 with Dissolve(0.5)
    "................"
    scene DetentionClass_Scene21 with Dissolve(0.5)
    Maria "Uhhh, [MC]?"
    scene DetentionClass_Scene22 with Dissolve(0.5)
    MC "Listen up, Maria, I got it! I have a plan!"
    MC "When she comes back in, you get a hold of her and I blow her back out!"
    scene DetentionClass_Scene23 with Dissolve(0.5)
    Maria "{color=#808080}*Oh no, he's gone completely insane!*{/color}"
    scene DetentionClass_Scene24 with Dissolve(0.5)
    Maria "Ummm, [MC], listen, I don't think that's a great idea..."
    Maria "I mean yeah, pinning her down and fucking her sounds good and all."
    scene DetentionClass_Scene25 with Dissolve(0.5)
    Maria "But prison kinda sucks... I don't think it's all that fun..."
    scene DetentionClass_Scene26 with Dissolve(0.5)
    MC "Then I might have an even better idea..."
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}**5 minutes later...**{/color}"
    scene DetentionClass_Scene27 with Dissolve(0.5)
    Sandra "{color=#808080}*Ugh, why was I assigned to watch over them in detention.*{/color}"
    scene DetentionClass_Scene28 with Dissolve(0.5)
    Sandra "{color=#808080}*I guess they know I'm the only one capable of teaching these kids some respect.*{/color}"
    scene DetentionClass_Scene29 with Dissolve(0.5)
    Maria "AHHH, [MC], stop doing it so hard!"
    Maria "It hurts, I can barely feel my legs anymore!"
    MC "Stop crying, you know you can take more!"
    scene DetentionClass_Scene30 with Dissolve(0.5)
    Sandra "{color=#808080}*What the...*{/color}"
    scene DetentionClass_Scene31 with Dissolve(0.5)
    Sandra "WHAT ARE YOU TWO DOING IN HERE?!!?!"
    show Detention_BalanceTraining1_1 with Dissolve(0.5)
    Sandra "Huh...."
    $ ShouldSeeSwitchSceneButton = True
    $ play_video_sequence(["Detention_BalanceTraining2_1", "Detention_BalanceTraining2_2", "Detention_BalanceTraining2_3", "Detention_BalanceTraining1_1"]) 
    Maria "Ahhh...."
    scene DetentionClass_Scene32 with Dissolve(0.5)
    $ ShouldSeeSwitchSceneButton = False
    Sandra "YOU TWO STOP RIGHT NOW!!!"
    scene DetentionClass_Scene33 with Dissolve(0.5)
    Sandra "Take your hand off of her right now!!"
    scene DetentionClass_Scene34 with Dissolve(0.5)
    Maria "No, Miss Nadal, I can explain!"
    Maria "I asked him to do this!"
    scene DetentionClass_Scene35 with Dissolve(0.5)
    Sandra "Then you better have a damn good reason for all of this!!"
    scene DetentionClass_Scene36 with Dissolve(0.5)
    Sandra "Go on, explain yourselves!"
    scene DetentionClass_Scene37 with Dissolve(0.5)
    Maria "I asked [MC] to help me with some stretching exercises..."
    Maria "Lately, from all the sitting, my legs started to hurt..."
    Maria "And I even started to perform poorly in PE..."
    scene DetentionClass_Scene38 with Dissolve(0.5)
    MC "We know we are not supposed to do this in detention..."
    MC "But we thought that, since we are in detention to begin with, it means we have a lot of catching up to do!"
    MC "And we should use this time to better ourselves!"
    scene DetentionClass_Scene39 with Dissolve(0.5)
    Sandra "Ehh, I guess that's a good enough reason..."
    scene DetentionClass_Scene40 with Dissolve(0.5)
    Sandra "But if you kids want to do this while I'm watching over you, you can't just break your legs and call that stretching!"
    Sandra "I guess Tanya isn't teaching you anything in PE. I will show you how to do it correctly!"
    scene DetentionClass_Scene41 with Dissolve(0.5)
    pause
    scene DetentionClass_Scene42 with Dissolve(0.5)
    Maria "But, Miss Nadal, I'm really scared of getting hurt doing it, and [MC] is no help."
    Maria "I think I'd better see a professional..."
    scene DetentionClass_Scene43 with Dissolve(0.5)
    Sandra "Haha, that's a nice way of saying you don't trust me."
    Sandra "You kids must not know who I am."
    scene DetentionClass_Scene44 with Dissolve(0.5)
    Sandra "I am the one who the professionals call to, sweetie."
    scene DetentionClass_Scene45 with Dissolve(0.5)
    Maria "{color=#808080}*Damn, she's acting different, I don't know what it is but we hit a soft spot or something.*{/color}"
    Maria "{color=#808080}*I mean, she's still arrogant and prideful as always, but now... I think she's happy!*{/color}"
    Maria "{color=#808080}*I can't believe [MC]'s plan is working!*{/color}"
    Maria "{color=#808080}*And she's so cute and little with that attitude of hers... God she's so hot...*{/color}"
    scene DetentionClass_Scene46 with Dissolve(0.5)
    MC "{color=#808080}*Ummm, well, that worked out better than I expected...*{/color}"
    MC "{color=#808080}*I think we managed to find the humanity in her...*{/color}"
    scene DetentionClass_Scene47 with Dissolve(0.5)
    MC "Did you use to do sports, Miss Nadal?"
    scene DetentionClass_Scene48 with Dissolve(0.5)
    Sandra "Didn't I tell you no talking in detention? Are you forgetting that fast?"
    scene DetentionClass_Scene49 with Dissolve(0.5)
    MC "{color=#808080}*Never mind, I guess...*{/color}"
    scene DetentionClass_Scene50 with Dissolve(0.5)
    Sandra "Okay, so what you were trying to do before is no easy move for beginners."
    Sandra "So it's way too advanced to be used for stretching."
    scene DetentionClass_Scene52 with Dissolve(0.5)
    Maria "Could you still show us how it's done? I always wanted to be able to do that."
    scene DetentionClass_Scene53 with Dissolve(0.5)
    MC "You can't ask that of her, Maria, Miss Nadal is a teacher now!"
    scene DetentionClass_Scene54 with Dissolve(0.5)
    Maria "Yeah, I guess you're right..."
    scene DetentionClass_Scene55 with Dissolve(0.5)
    Sandra "You kids really need to stop assuming things about me..."
    Sandra "I'm surprised you two are that clueless, I suppose rumors about me got around more..."
    scene DetentionClass_Scene56 with Dissolve(0.5)
    Sandra "I'll only repeat myself one more time."
    scene DetentionClass_Scene57 with Dissolve(0.5)
    Sandra "I am the best at this!"
    scene DetentionClass_Scene58 with Dissolve(0.5)
    Sandra "So basically, what you were trying to do earlier is this..."
    Sandra "But, again, this is no way to stretch for a beginner!"
    scene DetentionClass_Scene59 with Dissolve(0.5)
    MC "I saw Leya doing that once in PE."
    MC "But she went way higher than that!"
    scene DetentionClass_Scene60 with Dissolve(0.5)
    Sandra "You mean like this?"
    scene DetentionClass_Scene61 with Dissolve(0.5)
    MC "Y-yes... I think that is even better than Leya..."
    scene DetentionClass_Scene62 with Dissolve(0.5)
    Sandra "Huh? Better? I have to have a talk with her then..."
    $ MC_LS = mc_name + " lip syncing"
    scene DetentionClass_Scene63 with Dissolve(0.5)
    MC_LS "Now!"
    scene DetentionClass_Scene64 with Dissolve(0.5)
    Sandra "In any case, now you see why this exercise is way too hard for you to do."
    scene DetentionClass_Scene65 with Dissolve(0.5)
    Sandra "Huh? Where did you go, Maria?"
    scene DetentionClass_Scene66 with Dissolve(0.5)
    Sandra "Igh!"
    scene DetentionClass_Scene67 with Dissolve(0.5)
    Maria "Doesn't it hurt?"
    scene DetentionClass_Scene68 with Dissolve(0.5)
    Sandra "Uhhh, no, not really..."
    scene DetentionClass_Scene66 with Dissolve(0.5)
    Sandra "Igh!"
    scene DetentionClass_Scene69 with Dissolve(0.5)
    MC "Are you sure? It looks really painful!"
    scene DetentionClass_Scene70 with Dissolve(0.5)
    Sandra "I told you it doesn't!"
    scene DetentionClass_Scene71 with Dissolve(0.5)
    Sandra "Ugh!"
    scene DetentionClass_Scene72 with Dissolve(0.5)
    Maria "I didn't even know the body could bend like that!"
    scene DetentionClass_Scene73 with Dissolve(0.5)
    Sandra "MARIA! CAREFUL WITH YOUR HANDS!"
    scene DetentionClass_Scene74 with Dissolve(0.5)
    Maria "Oh, I'm sorry, Miss Nadal, I got a bit lost!"
    scene DetentionClass_Scene75 with Dissolve(0.5)
    Sandra "Alright, both of you, you've seen enough!"
    scene DetentionClass_Scene76 with Dissolve(0.5)
    Sandra "What the hell are you two doing, touching me like that?!"
    scene DetentionClass_Scene77 with Dissolve(0.5)
    Sandra "Don't you ev—"
    scene DetentionClass_Scene78 with Dissolve(0.5)
    "{color=#808080}**RING RING RING**{/color}"
    Sandra "Tsk!"
    scene DetentionClass_Scene79 with Dissolve(0.5)
    MC "Oh, it seems that detention ended!"
    MC "We are kinda in a hurry!"
    scene DetentionClass_Scene80 with Dissolve(0.5)
    MC "Let's go, Maria!"
    scene DetentionClass_Scene81 with Dissolve(0.5)
    MC "Sorry, Miss Nadal, see you in manners class!"
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}**Sandra Love - 2**{/color}"
    "{color=#808080}**Sandra Corruption + 2**{/color}"
    "{color=#808080}**Sandra Obedience + 2**{/color}"
    $ Sandra_love = Sandra_love - 2
    $ Sandra_Corruption = Sandra_Corruption + 2
    $ Sandra_Obedience = Sandra_Obedience + 2
    $ check_and_update_character_stats("Sandra")
    $ Location = "artclassfront"
    $ advance_time_or_sleep()

        # "Drop Pen":
        # "Strength Test":
        # "Posture Correction":