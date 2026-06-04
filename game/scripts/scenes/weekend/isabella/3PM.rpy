init python:
    define_images("Isabella_weekend_3PM_", "WeekendScenes/IsabellaScenes/3PM", "Isabella_weekend_3PM_", 100)

label Isabella_weekend_3PM:
    scene Isabella_weekend_3PM_1 with Dissolve(0.5)
    menu:
        "knock":
            Isabella "I'm changing, don't enter!"
            MC "Oh, okay, say less sis, you know I always respect your privacy!"
            Isabella "Myeah, appreciate it...."
            scene Isabella_weekend_3PM_2 with Dissolve(0.5)
            MC "{color=#808080}*At this point it's her fault for trusting me.*{color=#808080}"
            scene Isabella_weekend_3PM_3 with Dissolve(1.5)
            MC "{color=#808080}*What are they even doing?*{color=#808080}"
            MC "{color=#808080}*What is Isa wearing?*{color=#808080}"
            scene Isabella_weekend_3PM_4 with Dissolve(1)
            MC "{color=#808080}*Is that a cop uniform? What the...*{color=#808080}"
            scene Isabella_weekend_3PM_2 with Dissolve(1)
            MC "Can I enter now?! What are you changing for?"
            scene Isabella_weekend_3PM_5 with Dissolve(1)
            Isabella "HUH? Are you still at the door?!"
            Isabella "Yeah, I'm still changing, what do you want?!"
            scene Isabella_weekend_3PM_6 with Dissolve(0.5)
            MC "I'll tell you when you let me in!"
            scene Isabella_weekend_3PM_7 with Dissolve(0.5)
            Isabella "Tsk! Then wait! I'll tell you when you can come in!"
            scene BlackScreen with Dissolve(1)
            "5 minutes pass..."
            scene Isabella_weekend_3PM_8 with Dissolve(0.5)
            Isabella "Are you still there?! You can come in now!"
            scene Isabella_weekend_3PM_9 with Dissolve(0.5)
            Criss "I don't think he's still there, Isa..."
            scene Isabella_weekend_3PM_10 with Dissolve(0.5)
            Isabella "Don't be so sure, we opened the box..."
            scene Isabella_weekend_3PM_11 with Dissolve(0.5)
            Criss "Huh? What box?"
            scene Isabella_weekend_3PM_12 with Dissolve(0.5)
            MC "I came!"
            scene Isabella_weekend_3PM_13 with Dissolve(0.5)
            Isabella "Told ya..."
            scene Isabella_weekend_3PM_14 with Dissolve(0.5)
            Criss "Ughhh... You two have too many inside jokes for me to understand..."
            scene Isabella_weekend_3PM_15 with Dissolve(1.5)
            MC "Cosplay? Since when do you cosplay?"
            scene Isabella_weekend_3PM_16 with Dissolve(0.5)
            Isabella "I don't! Criss made me do it, but it's pretty fun!"
            scene Isabella_weekend_3PM_17 with Dissolve(0.5)
            Criss "Isaaaa!"
            scene Isabella_weekend_3PM_18 with Dissolve(0.5)
            Isabella "Yeah, yeah, I know, it's okay."
            scene Isabella_weekend_3PM_19 with Dissolve(0.5)
            MC "Suuuuuuure..."
            scene Isabella_weekend_3PM_20 with Dissolve(0.5)
            MC "Cool! So what's the plan? I want in!"
            MC "Do I get dressed up as well? Do we all get naked? Do I get to choose my outfit?"
            scene Isabella_weekend_3PM_21 with Dissolve(0.5)
            Isabella "Yeah! Exactly! All of those! It will be so much fun!"
            scene Isabella_weekend_3PM_22 with Dissolve(0.5)
            MC "Wait, no way! Are you serious?!"
            scene Isabella_weekend_3PM_23 with Dissolve(0.5)
            Isabella "Fuck no."
            scene Isabella_weekend_3PM_24 with Dissolve(0.5)
            Isabella "Get the hell out of my room!"
            scene Isabella_weekend_3PM_25 with Dissolve(0.5)
            MC "...."
            scene Isabella_weekend_3PM_26 with Dissolve(0.5)
            Isabella "...."
            scene BlackScreen with Dissolve(1)
            Criss "Every single time..."
            scene Isabella_weekend_3PM_27 with Dissolve(0.5)
            Criss "Sometimes I'm glad I'm an only child..."
            scene Isabella_weekend_3PM_28 with Dissolve(0.5)
            MC "Stop fighting like a girl!"
            Isabella "Not really an option for me, don't you think? dumbass!?"
            call stat_reward({"Criss": {"love": 2}, "Isabella": {"love": 2}}, return_to=None)
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "open":
            scene Isabella_weekend_3PM_29 with Dissolve(0.5)
            MC "Hey girls! What's up!"
            scene Isabella_weekend_3PM_30 with Dissolve(0.5)
            Criss "Huh?"
            scene Isabella_weekend_3PM_31 with Dissolve(0.5)
            Isabella "Hmm?"
            scene Isabella_weekend_3PM_32 with Dissolve(0.5)
            IsaAndCriss "AAAAAAAAAAAAAAAAAAAAAAAAAA!!!!"
            scene Isabella_weekend_3PM_33 with Dissolve(0.5)
            MC "Bad timing?"
            scene Isabella_weekend_3PM_34 with Dissolve(0.5)
            IsaAndCriss "GET OUT!!!!!!"
            scene Isabella_weekend_3PM_33 with Dissolve(0.5)
            MC "I'll take that as a yes..."
            scene Isabella_weekend_3PM_35 with Dissolve(0.5)
            MC "Geez... so dramatic..."
            scene Isabella_weekend_3PM_36 with Dissolve(0.5)
            MC "Huh?"
            scene Isabella_weekend_3PM_37 with Dissolve(0.5)
            Jennifer "Care to explain yourself?!"
            scene Isabella_weekend_3PM_38 with Dissolve(0.5)
            MC "Oh, mom! Well, it's actually pretty funny, you see, I was just-"
            scene Isabella_weekend_3PM_39 with Dissolve(0.5)
            MC "HEEEEEEEEEEELP!!!!"
            call stat_reward({"Criss": {"love": -2}, "Isabella": {"love": -2}, "Jennifer": {"love": -2}}, return_to=None)
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "leave":
            MC "Maybe another time..."
            "{color=#808080}**You leave.**{/color}"
            $ Location = "Hallway"
            call ReturnToLocation
