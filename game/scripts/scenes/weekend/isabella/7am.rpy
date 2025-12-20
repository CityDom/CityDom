init python:
    define_images("Isabella_weekend_7AM_", "WeekendScenes/IsabellaScenes/7AM", "Isabella_weekend_7AM_", 100)

    renpy.image("Isabella_weekend_7AM_1_video", Movie(play="images/WeekendScenes/IsabellaScenes/7AM/Isabella_weekend_7AM_1_video.webm", loop=True, group="pov_group"))
    renpy.image("Isabella_weekend_7AM_2_video", Movie(play="images/WeekendScenes/IsabellaScenes/7AM/Isabella_weekend_7AM_2_video.webm", loop=False, group="pov_group"))
    renpy.image("humanity_plus_overlay", "images/humanity_plus_overlay.png")

    renpy.image("YouDied", "YouDied.png")

transform fadein_out_overlay:
    xalign 0.5  # center horizontally
    yalign 0.5  # center vertically
    zoom 0.7
    alpha 0.0
    linear 1.0 alpha 1.0  # fade in 1.0 seconds (longer)
    pause 0.5           # hold for 2.5 seconds
    linear 1.0 alpha 0.0  # fade out 1.0 seconds (longer)
    on hide:
        alpha 0.0

label Isabella_weekend_7AM:
    scene Isabella_weekend_7AM_1 with Dissolve(0.5)
    MC "What's up sis?"
    scene Isabella_weekend_7AM_2 with Dissolve(0.5)
    Isabella "Sup, sup. Nothing much, just woke up."
    scene Isabella_weekend_7AM_3 with Dissolve(0.5)
    MC "....."
    scene Isabella_weekend_7AM_4 with Dissolve(0.5)
    MC "Soooo..."
    scene Isabella_weekend_7AM_5 with Dissolve(0.5)
    MC "What are you watching?"
    show Isabella_weekend_7AM_1_video with Dissolve(0.5)
    Isabella "Oh, just some random video on TitTok."
    MC "Uhhh... TitTok? What the hell is that?"
    Isabella "Yeah, right, for sure you don't know what it is."
    MC "No, I'm for real, what is it?"
    scene Isabella_weekend_7AM_6 with Dissolve(0.5)
    Isabella "Ghaaaaa!!"
    scene Isabella_weekend_7AM_7 with Dissolve(0.5)
    Isabella "No way you don't know what TitTok is!"
    Isabella "What were you doing before coming here? Have you been living under a rock or something?"
    scene Isabella_weekend_7AM_8 with Dissolve(0.5)
    MC "Uhhh... I guess... kinda..."
    MC "I didn't get to do a lot of stuff, why do you think I spend so much time on the computer now?"
    scene Isabella_weekend_7AM_9 with Dissolve(0.5)
    Isabella "Oh my god, oh my god, I have so much to show you!"
    scene Isabella_weekend_7AM_10 with Dissolve(0.5)
    Isabella "You have no idea how much fun it is! We will send each other TitToks all the time!"
    scene Isabella_weekend_7AM_11 with Dissolve(0.5)
    MC "Uhhhh..."
    scene Isabella_weekend_7AM_12 with Dissolve(0.5)
    Isabella "I'll show you some other time! Let me show you the dance I just learned!"
    scene Isabella_weekend_7AM_13 with Dissolve(0.5)
    MC "Uhhh... sure, I guess."
    scene Isabella_weekend_7AM_14 with Dissolve(0.5)
    Isabella "Alrightyyy! Are you ready?"
    scene Isabella_weekend_7AM_15 with Dissolve(0.5)
    MC "I guess so?"
    scene Isabella_weekend_7AM_16 with Dissolve(0.5)
    Isabella "Listen here you nonchalant bitch, I spent two hours learning this dance."
    Isabella "So you better act excited, don't fuck with me!"
    scene Isabella_weekend_7AM_17 with Dissolve(0.5)
    MC "Y-yes ma'am!"
    scene Isabella_weekend_7AM_18 with Dissolve(0.5)
    Isabella "Okaaaayyyy"
    scene Isabella_weekend_7AM_19 with Dissolve(0.5)
    MC "Yaaaay....."
    scene Isabella_weekend_7AM_20 with Dissolve(0.5)
    Isabella "Which one was it again?"
    scene Isabella_weekend_7AM_21 with Dissolve(0.5)
    MC "Ughhh...."
    scene Isabella_weekend_7AM_22 with Dissolve(0.5)
    Isabella "Ah, there it is, alright."
    scene Isabella_weekend_7AM_23 with Dissolve(0.5)
    Isabella "Alright, I'm ready!"
    window hide
    show Isabella_weekend_7AM_2_video with Dissolve(0.5)
    pause
    scene Isabella_weekend_7AM_24 with Dissolve(0.5)
    Isabella "Aaaaaaaand-"
    scene Isabella_weekend_7AM_25 with Dissolve(0.5)
    Isabella "Scene!"
    scene Isabella_weekend_7AM_26 with Dissolve(0.5)
    MC "......"
    scene Isabella_weekend_7AM_27 with Dissolve(0.5)
    Isabella "So, sooooo? What do you think?"
    Isabella "But, like, be honest about it! I'm trying to get better at it, so I need an honest opinion!"
    Isabella "I can take criticism, I promise!"
    scene Isabella_weekend_7AM_28 with Dissolve(0.5)
    menu:
        "It was great!":
            scene Isabella_weekend_7AM_29 with Dissolve(0.5)
            show humanity_plus_overlay at fadein_out_overlay
            MC "It was great Isa, way better than I thought it would be!"
            MC "You really nailed it!"
            scene Isabella_weekend_7AM_30 with Dissolve(0.5)
            Isabella "Yupieeeeeee!!"
            scene Isabella_weekend_7AM_31 with Dissolve(0.5)
            Isabella "Do you think I should post it on TitTok?"
            scene Isabella_weekend_7AM_32 with Dissolve(0.5)
            MC "Uhhhh... I don't know... I guess..."
            scene Isabella_weekend_7AM_33 with Dissolve(0.5)
            Isabella "Okay, get out, I need to get changed."
            Isabella "I can't record it like this, I need to look cute!"
            scene Isabella_weekend_7AM_34 with Dissolve(0.5)
            MC "Huh? What do you mean \"get out\"?" 
            MC "I can just turn around, you know?" 
            scene Isabella_weekend_7AM_35 with Dissolve(0.5)
            Isabella "Yeah, because you are so well known for respecting people's privacy."
            scene Isabella_weekend_7AM_36 with Dissolve(0.5)
            MC "Hey, I'm your big brother, do you really think I would do something like that?"
            scene Isabella_weekend_7AM_37 with Dissolve(0.5)
            Isabella "Yes, I know it because you are my big brother."
            Isabella "I would be less watched if I'd do it in the city center."
            Isabella "So, get out!"
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**Isabella love + 2**{color=#808080}"
            "{color=#808080}**Isabella corruption + 2**{color=#808080}"
            $ Isabella_love = Isabella_love + 2
            $ Isabella_Corruption = Isabella_Corruption + 2
            $ check_and_update_character_stats("Isabella")
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "It was alright":
            scene Isabella_weekend_7AM_29 with Dissolve(0.5)
            MC "It was alright, but I think you should work on it a bit more."
            MC "Maybe be a bit more energetic?"
            scene Isabella_weekend_7AM_38 with Dissolve(0.5)
            Isabella "Mhm, mhm..."
            window hide
            scene YouDied with Dissolve(3)
            pause 3.0
            scene Isabella_weekend_7AM_39 with Dissolve(0.5)
            MC "\"Can take criticism\" my ass..."
            scene BlackScreen with Dissolve(0.5)
            "{color=#808080}**Isabella love - 2**{color=#808080}"
            "{color=#808080}**Isabella corruption - 2**{color=#808080}"
            $ Isabella_love = Isabella_love - 2
            $ Isabella_Corruption = Isabella_Corruption - 2
            $ check_and_update_character_stats("Isabella")
            $ Location = "Hallway"
            $ advance_time_or_sleep()