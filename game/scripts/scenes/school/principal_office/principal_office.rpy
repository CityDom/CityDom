init python:
    define_images("PrincipalOffice_scene", "PrincipalOffice", "PrincipalOffice_scene", 100)

label PrincipalOffice:
    scene PrincipalOffice_scene1 with Dissolve(0.5)
    MC "{color=#808080}*Ughhh, do I really have to do this?*"
    MC "{color=#808080}*This is going to be such a pain...*"
    menu:
        "Knock":
            MC "{color=#808080}*Alright... let's do it...*"
            scene PrincipalOffice_scene2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene PrincipalOffice_scene3 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene PrincipalOffice_scene2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene PrincipalOffice_scene3 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene PrincipalOffice_scene2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene PrincipalOffice_scene3 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene PrincipalOffice_scene4 with Dissolve(0.5)
            Angeline "Yeah, yeah, come in!"
            scene PrincipalOffice_scene5 with Dissolve(0.5)
            MC "{color=#808080}*Here we go...*"
            scene PrincipalOffice_scene6 with Dissolve(0.5)
            MC "Excuse me!"
            scene PrincipalOffice_scene7 with Dissolve(0.5)
            Angeline "....."
            scene PrincipalOffice_scene8 with Dissolve(0.5)
            pause
            scene PrincipalOffice_scene9 with Dissolve(0.5)
            pause
            scene PrincipalOffice_scene10 with Dissolve(0.5)
            pause
            scene PrincipalOffice_scene11 with Dissolve(0.5)
            Angeline "Ugh, of course..."
            scene PrincipalOffice_scene12 with Dissolve(0.5)
            Angeline "What did you do this time?"
            scene PrincipalOffice_scene13 with Dissolve(0.5)
            MC "Nothing! I've actually been really good lately!"
            scene PrincipalOffice_scene14 with Dissolve(0.5)
            Angeline "Huh? Really?"
            scene PrincipalOffice_scene15 with Dissolve(0.5)
            Angeline "Then why are you here?"
            jump AngelineMenu
        "Don't":
            MC "{color=#808080}*Nah, I can't be bothered right now...*"
            $ renpy.call("GameLoop")

label AngelineMenu:
    scene PrincipalOffice_scene16 with Dissolve(0.5)
    menu:
        "What do you think about me?":
            if Watched_PrincipalOffice_WDYTAM:
                MC "{color=#808080}*I already know what she thinks...*"
                jump AngelineMenu
            $ Watched_PrincipalOffice_WDYTAM = True
            MC "I just wanted to ask, what do you think about me?"
            scene PrincipalOffice_scene17 with Dissolve(0.5)
            Angeline "Huh? That's why you came here?"
            Angeline "I don't have time for chitchat, unless you don't have an actual problem to report, you can leave."
            scene PrincipalOffice_scene18 with Dissolve(0.5)
            MC "Uhhh, it's just a quick question..."
            scene PrincipalOffice_scene19 with Dissolve(0.5)
            Angeline "..."
            scene PrincipalOffice_scene20 with Dissolve(0.5)
            Angeline "Ehhh..."
            Angeline "You are a pain in my butt."
            Angeline "And teachers complain about your behavior, so you add to my workload."
            scene PrincipalOffice_scene21 with Dissolve(0.5)
            Angeline "Buuuuut, your mother and I used to be colleagues back in high school and college."
            scene PrincipalOffice_scene22 with Dissolve(0.5)
            Angeline "So I'm doing her a favor!"
            scene PrincipalOffice_scene23 with Dissolve(0.5)
            MC "Oh... okay..."
            scene PrincipalOffice_scene24 with Dissolve(0.5)
            MC "Wait, you know my mom?"
            scene PrincipalOffice_scene25 with Dissolve(0.5)
            Angeline "A ta ta ta, let me stop you right there."
            Angeline "I don't have time for a Q&A."
            scene PrincipalOffice_scene26 with Dissolve(0.5)
            Angeline "So I'll invite you to get out of my office."
            scene PrincipalOffice_scene27 with Dissolve(0.5)
            MC "Oh... Okay, thank you for your time either way!"
            scene PrincipalOffice_scene28 with Dissolve(0.5)
            Angeline "Yeah, yeah, just get out already!"
            $ Location = "TeacherHall"
            $ advance_time_or_sleep()
            $ renpy.call("GameLoop")
        "Compliment":
            if Watched_PrincipalOffice_Compliment:
                MC "{color=#808080}*I've already complimented her... no need to do it again.*"
                jump AngelineMenu
            $ Watched_PrincipalOffice_Compliment = True
            MC "I dropped by to let you know that I am really grateful for the opportunity that you gave me."
            MC "I know that the school is predominantly a girls' school, and the few boys that come here are... uhhh..."
            scene PrincipalOffice_scene29 with Dissolve(0.5)
            MC "Affluent individuals..."
            scene PrincipalOffice_scene30 with Dissolve(0.5)
            MC "So I just wanted to thank you!"
            scene PrincipalOffice_scene31 with Dissolve(0.5)
            Angeline "Mhm, yeah, right, no problem."
            scene PrincipalOffice_scene32 with Dissolve(0.5)
            Angeline "Now tell me, did Jennifer put you up to this?"
            scene PrincipalOffice_scene33 with Dissolve(0.5)
            MC "No! But she taught me not to take good deeds for granted!"
            MC "Especially when they come from beautiful women!"
            scene PrincipalOffice_scene34 with Dissolve(0.5)
            Angeline "Hah, she taught you well!"
            scene PrincipalOffice_scene35 with Dissolve(0.5)
            Angeline "Now get out, you already cause me enough trouble to waste my time chitchatting."
            Angeline "This school doesn't run itself!"
            scene PrincipalOffice_scene36 with Dissolve(0.5)
            MC "Yes ma'am! Thank you for your time!"
            $ Location = "TeacherHall"
            call stat_reward({"Angeline": {"love": 2}}, return_to=None)
            $ advance_time_or_sleep()
            $ renpy.call("GameLoop")
        "Pervert compliment":
            if Watched_PrincipalOffice_PervertCompliment:
                MC "{color=#808080}*I better not push my luck...*"
                jump AngelineMenu
            $ Watched_PrincipalOffice_PervertCompliment = True
            MC "I saw you earlier in the hallway, and I just wanted to tell you that you look amazing today, ma'am!"
            scene PrincipalOffice_scene37 with Dissolve(0.5)
            MC "That suit really shows all your good parts!"
            scene PrincipalOffice_scene38 with Dissolve(0.5)
            Angeline "............"
            scene PrincipalOffice_scene39 with Dissolve(0.5)
            Angeline "Get out."
            scene PrincipalOffice_scene40 with Dissolve(0.5)
            MC "Yes ma'am!"
            $ Location = "TeacherHall"
            call stat_reward({"Angeline": {"love": -2, "corruption": -2}}, return_to=None)
            $ advance_time_or_sleep()
            $ renpy.call("GameLoop")
        "Insult":
            if Watched_PrincipalOffice_Insult:
                MC "{color=#808080}*I really don't want to go there again...*"
                jump AngelineMenu
            $ Watched_PrincipalOffice_Insult = True
            MC "{color=#808080}*This is not the right person to try my luck with...*"
            MC "{color=#808080}*It's too dangerous.*"
            jump AngelineMenu
        "Leave":
            MC "Uhhh, actually... I think I'm late to class!"
            scene PrincipalOffice_scene41 with Dissolve(0.5)
            Angeline "Are you actually just trying to waste my time as much as possible?"
            $ Location = "TeacherHall"
            $ renpy.call("GameLoop")
