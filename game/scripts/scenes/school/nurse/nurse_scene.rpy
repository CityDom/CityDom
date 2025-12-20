init python:
    define_images("Nurse_Scene", "NurseRoom", "Nurse_Scene", 100)

label NurseScene:
    scene Nurse_Scene1 with Dissolve(0.5)
    Luna "Hey, [MC], what brings you here today? Everything alright?"
    jump LunaMenu

label LunaMenu:
    scene Nurse_Scene9 with Dissolve(0.5)
    menu:
        "What do you think about me?":
            if Watched_Nurse_WDYTAM:
                MC "{color=#808080}*I already asked her about that...*{color=#808080}"
                jump LunaMenu
            else:
                $ Watched_Nurse_WDYTAM = True
                MC "Yeah, I just wanted to ask you, what do you think about me?"
                scene Nurse_Scene3 with Dissolve(0.5)
                Luna "Uhhh, that's a bit of an odd question..."
                Luna "And you shouldn't come to the nurse's office for these types of questions."
                scene Nurse_Scene4 with Dissolve(0.5)
                Luna "But since we're already here..."
                scene Nurse_Scene5 with Dissolve(0.5)
                Luna "I think you are a nice—"
                scene Nurse_Scene6 with Dissolve(0.5)
                Luna "and very—"
                scene Nurse_Scene7 with Dissolve(0.5)
                Luna "healthy—"
                scene Nurse_Scene6 with Dissolve(0.5)
                Luna "young man."
                scene Nurse_Scene8 with Dissolve(0.5)
                Luna "Is that all you came here for?"
                jump LunaMenu
        "Compliment":
            if Watched_Nurse_Compliment:
                MC "{color=#808080}*I already complimented her...*{color=#808080}"
                jump LunaMenu
            else:
                $ Watched_Nurse_Compliment = True
                MC "Well... I wanted to tell you that..."
                scene Nurse_Scene10 with Dissolve(0.5)
                MC "I just wanted to tell you that you've really helped me with my biology grades."
                MC "The physical learning actually helped me out a lot!"
                scene Nurse_Scene11 with Dissolve(0.5)
                Luna "Whaaaa, reallyyy?!"
                Luna "Ahhhh, I'm so glad!"
                scene Nurse_Scene12 with Dissolve(0.5)
                Luna "After Miss Greene had her..."
                scene Nurse_Scene13 with Dissolve(0.5)
                Luna "Uhhhh... Accident..."
                scene Nurse_Scene12 with Dissolve(0.5)
                Luna "I was really nervous about teaching the class since I don't have much experience in that!"
                scene Nurse_Scene14 with Dissolve(0.5)
                Luna "So it actually means a lot! Thank you!"
                scene Nurse_Scene15 with Dissolve(0.5)
                Luna "But... uhhh... I don't really have time to talk right now..."
                Luna "So if you don't have an actual problem you kinda have to leave..."
                "{color=#808080}**Luna love + 2**{color=#808080}"      
                $ Luna_love = Luna_love + 2
                jump LunaMenu
        "Pervert compliment":
            if Watched_Nurse_PervertCompliment:
                MC "{color=#808080}*I already told her that...*{color=#808080}"
                jump LunaMenu
            else:
                $ Watched_Nurse_PervertCompliment = True
                MC "I just wanted to let you know, about the biology class..."
                scene Nurse_Scene16 with Dissolve(0.5)
                Luna "Uhhh, yeah, what about it?"
                scene Nurse_Scene17 with Dissolve(0.5)
                MC "Your breasts were really soft, your ass as well!"
                scene Nurse_Scene18 with Dissolve(0.5)
                Luna "Ahh, I'm glad to hear that."
                Luna "Wouldn't you like to have a go at it aga—"
                scene Nurse_Scene19 with Dissolve(0.5)
                Luna "OHG!"
                scene BlackScreen with Dissolve(1)
                "....."
                scene Nurse_Scene20 with Dissolve(1)
                pause
                scene Nurse_Scene21 with Dissolve(1)
                pause
                scene Nurse_Scene22 with Dissolve(1)
                Unknown "What the fuck do you think you're doing?"
                scene Nurse_Scene23 with Dissolve(1)
                Luna "Huh?! W-w-w-w-wh-what am I doing?"
                scene Nurse_Scene24 with Dissolve(1)
                Unknown "Didn't I tell you that one is mine?"
                Unknown "Is there a misunderstanding?"
                scene Nurse_Scene25 with Dissolve(1)
                Luna "N-n-n-o Ma'am!"
                scene Nurse_Scene26 with Dissolve(1)
                Unknown "Good."
                scene Nurse_Scene27 with Dissolve(1)
                Unknown "Keep doing the shit you're doing, the deed is already done anyway."
                Unknown "But go any further than that... and I promise you won't like what happens next."
                Unknown "This is your last and only warning."
                scene Nurse_Scene29 with Dissolve(1)
                Luna "But I th—"
                scene Nurse_Scene28 with Dissolve(1)
                pause
                scene BlackScreen with Dissolve(1)
                "....."
                scene Nurse_Scene30 with Dissolve(0.5)
                Luna "Uhhhh..."
                scene Nurse_Scene31 with Dissolve(0.5)
                Luna "Ahem, ahem!"
                scene Nurse_Scene32 with Dissolve(0.5)
                Luna "Aghhh, Ughhh, I'm so angry about all of this! Aghhh!"
                scene Nurse_Scene33 with Dissolve(0.5)
                MC "Huh...?"
                scene Nurse_Scene34 with Dissolve(0.5)
                Luna "How could you say such obscene words to me, young man?!"
                Luna "I am a nurse and also your teacher!"
                scene Nurse_Scene35 with Dissolve(0.5)
                MC "Wait, what?! But I thought—"
                scene Nurse_Scene36 with Dissolve(0.5)
                Luna "Enough talking, [MC]!! Get out of my office right now!"
                scene BlackScreen with Dissolve(0.5)
                "{color=#808080}**Luna love - 2**{color=#808080}"
                "{color=#808080}**Luna corruption + 2**{color=#808080}"            
                $ Luna_love = Luna_love - 2
                $ Luna_Corruption = Luna_Corruption + 2
                $ Location = "MedicRoomFront"
                $ check_and_update_character_stats("Luna")
                $ renpy.call("GameLoop")
        "Insult":
            if Watched_Nurse_Insult:
                MC "{color=#808080}*I already insulted her...*{color=#808080}"
                jump LunaMenu
            else:
                $ Watched_Nurse_Insult = True
                MC "How old are you, Miss Lucky?"
                MC "In any case, the gray hair kinda gives it away..."
                MC "Have you ever thought of dyeing it?"
                scene Nurse_Scene37 with Dissolve(0.5)
                Luna "It's not because I'm old, imbecile!"
                Luna "I have a condition!"
                scene Nurse_Scene38 with Dissolve(0.5)
                Luna "Get out, now!"
                Luna "I don't have time for this right now!"
                scene BlackScreen with Dissolve(0.5)
                "{color=#808080}**Luna love - 2**{color=#808080}"
                "{color=#808080}**Luna corruption - 2**{color=#808080}"            
                $ Luna_love = Luna_love - 2
                $ Luna_Corruption = Luna_Corruption - 2
                $ Location = "MedicRoomFront"
                $ check_and_update_character_stats("Luna")
                $ renpy.call("GameLoop")
        "Leave":
            MC "I was feeling a little off, but I think I'm better now!"
            MC "Thank you, Miss Lucky!"
            scene Nurse_Scene39 with Dissolve(0.5)
            Luna "Uhhh, alright...."
            scene BlackScreen with Dissolve(0.5)        
            $ renpy.call("GameLoop")
