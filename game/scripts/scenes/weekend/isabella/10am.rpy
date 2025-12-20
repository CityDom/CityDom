init python:
    define_images("Isabella_weekend_10AM_", "WeekendScenes/IsabellaScenes/10AM", "Isabella_weekend_10AM_", 100)

label Isabella_weekend_10AM:
    scene Isabella_weekend_10AM_1 with Dissolve(0.5)
    Isabella "CRISS!!"
    scene Isabella_weekend_10AM_2 with Dissolve(0.5)
    Criss "H-hey Isa... you're hugging me kinda tight..."
    scene Isabella_weekend_10AM_3 with Dissolve(0.5)
    MC "Hm?"
    scene Isabella_weekend_10AM_4 with Dissolve(0.5)
    Criss "Huh?"
    scene Isabella_weekend_10AM_5 with Dissolve(0.5)
    Criss "H-hi, [MC]!"
    scene Isabella_weekend_10AM_6 with Dissolve(0.5)
    MC "Heya, Criss."
    MC "Do you need any help with the leech? She grows roots if you don't pull her off you."
    scene Isabella_weekend_10AM_7 with Dissolve(0.5)
    Criss "Uhhh... a bit of help, if you can, please."
    scene Isabella_weekend_10AM_8 with Dissolve(0.5)
    MC "Ok, that's enough, get off her!"
    scene Isabella_weekend_10AM_9 with Dissolve(0.5)
    Isabella "NAUR! She's warm and squishy!"
    scene Isabella_weekend_10AM_10 with Dissolve(0.5)
    MC "I'm warm and squishy too, and you never hug me like this!"
    scene Isabella_weekend_10AM_9 with Dissolve(0.5)
    Isabella "NOO! You're always hard! Let me go!"
    scene Isabella_weekend_10AM_11 with Dissolve(0.5)
    Criss "{color=#808080}*He's always what?!*{/color}"
    scene Isabella_weekend_10AM_12 with Dissolve(0.5)
    MC "Okay, missy, you're forcing my hand here!"
    scene Isabella_weekend_10AM_13 with Dissolve(0.5)
    Isabella "Oh no, don't get serious, what am I gonna dooo..."
    menu:
        "Pull her seriously":
            scene Isabella_weekend_10AM_14 with Dissolve(0.5)
            MC "You asked for it!"
            scene Isabella_weekend_10AM_15 with Dissolve(0.5)
            MC "Hmph!"
            scene Isabella_weekend_10AM_16 with Dissolve(0.5)
            Isabella "Huh?"
            scene Isabella_weekend_10AM_17 with Dissolve(0.5)
            MC "WAIT! YOU WERE FOR REAL FOR REAL?!"
            scene Isabella_weekend_10AM_18 with Dissolve(0.5)
            Isabella "{color=#808080}*Ah, shit, this is gonna sting*"
            scene Isabella_weekend_10AM_19 with Dissolve(0.5)
            Criss "W-wait!!!"
            scene Isabella_weekend_10AM_20 with Dissolve(0.5)
            pause
            scene Isabella_weekend_10AM_21 with Dissolve(0.5)
            pause
            scene Isabella_weekend_10AM_22 with Dissolve(0.5)
            pause
            scene Isabella_weekend_10AM_23 with Dissolve(0.5)
            pause
            scene Isabella_weekend_10AM_24 with Dissolve(0.5)
            pause
            scene Isabella_weekend_10AM_25 with Dissolve(0.5)
            Isabella "Auchh..."
            scene Isabella_weekend_10AM_26 with Dissolve(0.5)
            MC "Hah, guess what, I think your diet is actually working, you feel lighter now!"
            scene Isabella_weekend_10AM_27 with Dissolve(0.5)
            Isabella "Wait, really?! Niceeee!"
            scene Isabella_weekend_10AM_28 with Dissolve(0.5)
            Criss "{color=#808080}*Is this how they are at home all the time? They are insane...*"
            scene Isabella_weekend_10AM_29 with Dissolve(0.5)
            Criss "M-maybe I should leave..."
            scene Isabella_weekend_10AM_30 with Dissolve(0.5)
            Isabella "Huh? Why? What happened?"
            scene Isabella_weekend_10AM_31 with Dissolve(0.5)
            MC "Oh, no, no, no, wait, my bad."
            MC "I'll let you two girls be."
            scene Isabella_weekend_10AM_32 with Dissolve(0.5)
            MC "See you around, have fun!"
            scene Isabella_weekend_10AM_33 with Dissolve(0.5)
            Criss "Are you okay, Isa?"
            scene Isabella_weekend_10AM_34 with Dissolve(0.5)
            Isabella "Huh? Yeah, no, I'm good!"
            Isabella "It pinched a bit, but I'm fine!"
            scene Isabella_weekend_10AM_35 with Dissolve(0.5)
            Criss "B-but he dropped you on your head..."
            Criss "Are you sure you're okay?"
            scene Isabella_weekend_10AM_36 with Dissolve(0.5)
            Isabella "Yeah, yeah, I'm totally fine!"
            Isabella "We wrestle like this quite often actually!"
            scene Isabella_weekend_10AM_37 with Dissolve(0.5)
            Isabella "First time he did it I shat myself..."
            Isabella "But he stops himself right before the impact, then let's me down gently."
            scene Isabella_weekend_10AM_38 with Dissolve(0.5)
            Isabella "I don't know what they fed him back at dad's..."
            scene Isabella_weekend_10AM_39 with Dissolve(0.5)
            Isabella "But he is scary strong sometimes..."
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**Isabella love + 2**{color=#808080}"
            $ Isabella_love = Isabella_love + 2
            $ check_and_update_character_stats("Isabella")
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "Change grip":
            scene Isabella_weekend_10AM_40 with Dissolve(0.5)
            MC "Okay then, don't say I didn't warn you."
            scene Isabella_weekend_10AM_41 with Dissolve(0.5)
            Isabella "HAH! Do your worst! You think you can scare me?!"
            scene Isabella_weekend_10AM_42 with Dissolve(0.5)
            Isabella "Huh...?"
            scene Isabella_weekend_10AM_43 with Dissolve(0.5)
            pause
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**SLAP!!!**"
            scene Isabella_weekend_10AM_44 with Dissolve(0.5)
            MC "To be honest... I don't feel like I deserved that..."
            scene Isabella_weekend_10AM_45 with Dissolve(0.5)
            Isabella "UGHHHH!!!"
            scene Isabella_weekend_10AM_46 with Dissolve(0.5)
            Isabella "You are such a piece of shit!"
            scene Isabella_weekend_10AM_47 with Dissolve(0.5)  
            MC "Come on, Criss!"
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**Isabella love - 5**{color=#808080}"
            $ Isabella_love = Isabella_love - 5
            $ check_and_update_character_stats("Isabella")
            $ Location = "Entrance"
            $ advance_time_or_sleep()
