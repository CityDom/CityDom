init python:
    define_images("Isabella_weekend_1PM_", "WeekendScenes/IsabellaScenes/1PM", "Isabella_weekend_1PM_", 100)
    renpy.image("Isabella_weekend_1PM_Video_1", Movie(play="images/WeekendScenes/IsabellaScenes/1PM/Isabella_weekend_1PM_Video_1.webm", loop=False, group="pov_group"))
label Isabella_weekend_1PM:
    scene Isabella_weekend_1PM_1 with Dissolve(0.5)
    Isabella "You haven't made a sound in like 10 minutes..."
    Isabella "What are you thinking about?"
    scene Isabella_weekend_1PM_2 with Dissolve(0.5)
    Criss "..."
    Criss "I don't wanna tell you."
    scene Isabella_weekend_1PM_3 with Dissolve(0.5)
    Isabella "Hah! Is it really that bad?"
    Isabella "C'mon, how long have we known each other now?"
    scene Isabella_weekend_1PM_4 with Dissolve(0.5)
    Criss "Please don't get this the wrong way..."
    Criss "I was just thinking how nice it must be with a pool like this..."
    Criss "A big house... siblings..."
    Criss "It seems fun..."
    scene Isabella_weekend_1PM_5 with Dissolve(0.5)
    Isabella "Well... I can't really say much about that. I've been living here my whole life."
    Isabella "So I've grown used to it. At this point I can only see the bad parts, but I guess you don't wanna hear about that."
    Isabella "If I tell you I don't ever use the pool unless you're here you'll think I'm just a spoiled bitch."
    scene Isabella_weekend_1PM_6 with Dissolve(0.5)
    Criss "What? No?! I would never think that."
    scene Isabella_weekend_1PM_7 with Dissolve(0.5)
    Isabella "Heh, I'm just messing with you."
    scene Isabella_weekend_1PM_8 with Dissolve(0.5)
    Isabella "But I know how most people look at me. Classmates, and especially the ones who know where I live."
    scene Isabella_weekend_1PM_9 with Dissolve(0.5)
    Isabella "Big house, huge pool... I'm put in the same category with Selina and Sophie, and we both know what everybody thinks about them."
    Isabella "But people don't really have any idea what they're talking about."
    scene Isabella_weekend_1PM_10 with Dissolve(0.5)
    Criss "What do you mean?"
    scene Isabella_weekend_1PM_11 with Dissolve(0.5)
    Isabella "Well... first of all, do a check for [MC], he can't hear this. And I already feel like he's doing something stupid."
    scene Isabella_weekend_1PM_12 with Dissolve(0.5)
    Criss "Uhhh... It seems clear. And stupid like what? I don't think he would spy on us or anything."
    Isabella "You never know with him..."
    Isabella "Okay, so..."
    scene Isabella_weekend_1PM_13 with Dissolve(0.5)
    MC "So what do you think they're saying? I think they're talking about me."
    scene Isabella_weekend_1PM_14 with Dissolve(0.5)
    Mhyrorin "I don't need to think, I can hear them clearly."
    scene Isabella_weekend_1PM_15 with Dissolve(0.5)
    Mhyrorin "Or I would if you would shut the fuck up for a second!"
    scene Isabella_weekend_1PM_16 with Dissolve(0.5)
    MC "Fuck you!"
    scene Isabella_weekend_1PM_17 with Dissolve(0.5)
    Mhyrorin "Shhhh, quiet!"
    scene Isabella_weekend_1PM_18 with Dissolve(0.5)
    Mhyrorin "Uhhhh..."
    scene Isabella_weekend_1PM_19 with Dissolve(0.5)
    pause
    scene Isabella_weekend_1PM_20 with Dissolve(0.5)
    MC "Soooo...? Are you still there? What are they saying?"
    scene Isabella_weekend_1PM_21 with Dissolve(0.5)
    Mhyrorin "Yeah... I don't know if I should be the one telling you these news to be honest."
    scene Isabella_weekend_1PM_22 with Dissolve(0.5)
    MC "Yeah, right. I bet they are talking about kissing each other."
    scene Isabella_weekend_1PM_23 with Dissolve(0.5)
    MC "Or maybe kissing me."
    MC "And getting all oily and rubbing their-"
    scene Isabella_weekend_1PM_24 with Dissolve(0.5)
    Mhyrorin "Okay, I had enough."
    scene Isabella_weekend_1PM_25 with Dissolve(0.5)
    MC "Huh? What are you doing?"
    scene Isabella_weekend_1PM_26 with Dissolve(0.5)
    MC "Okay, let's talk about it. I done joking."
    scene Isabella_weekend_1PM_27 with Dissolve(0.5)
    Mhyrorin "Are you sure?!"
    scene Isabella_weekend_1PM_28 with Dissolve(0.5)
    MC "Yeah, yeah, super duper sure. Just put me back, please."
    scene Isabella_weekend_1PM_29 with Dissolve(0.5)
    Mhyrorin "Ughhh... you're such a pussy!"
    scene Isabella_weekend_1PM_30 with Dissolve(0.5)
    MC "Thank you!"
    scene Isabella_weekend_1PM_31 with Dissolve(0.5)
    Criss "I didn't realize it was that bad..."
    Criss "I also feel so bad for [MC], you were right to double check for him."
    show Isabella_weekend_1PM_Video_1
    MC "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{nw}"
    $ renpy.pause(0.6, hard=True)
    scene Isabella_weekend_1PM_32
    Criss "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}**Isabella love + 2**{color=#808080}"
    "{color=#808080}**Criss love + 2**{color=#808080}"
    $ Isabella_love = Isabella_love + 2
    $ Criss_love = Criss_love + 2
    $ check_and_update_character_stats("Isabella")
    $ check_and_update_character_stats("Criss")
    $ Location = "Entrance"
    $ advance_time_or_sleep()
