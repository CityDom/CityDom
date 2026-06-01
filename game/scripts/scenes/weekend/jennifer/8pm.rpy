init python:
    define_images("Jennifer_weekend_8PM_", "WeekendScenes/JenniferScenes/8PM", "Jennifer_weekend_8PM_", 100)

image Jennifer_weekend_8PM_11_12_loop:
    "Jennifer_weekend_8PM_11" with Dissolve(0.4)
    pause 0.4

    "Jennifer_weekend_8PM_12" with Dissolve(0.4)
    pause 0.4

    repeat 4


label Jennifer_weekend_8PM:
    scene Jennifer_weekend_8PM_1 with Dissolve(0.5)
    MC "Ohhh, c'mon mom, are you still cleaning?"
    MC "I thought you'd be done after the pool break."
    scene Jennifer_weekend_8PM_2 with Dissolve(0.5)
    Jennifer "Well... somebody has to do it... right?"
    scene Jennifer_weekend_8PM_3 with Dissolve(0.5)
    Jennifer "But I appreciate the concern. Does that mean you're gonna help me out?"
    scene Jennifer_weekend_8PM_4 with Dissolve(0.5)
    MC "Uhhh... sure, I guess..."
    scene Jennifer_weekend_8PM_5 with Dissolve(0.5)
    MC "How can I help?"
    scene Jennifer_weekend_8PM_6 with Dissolve(0.5)
    Jennifer "To begin with, you can just keep me company."
    scene Jennifer_weekend_8PM_7 with Dissolve(0.5)
    Jennifer "It gets pretty lonely doing this all day by myself."
    scene Jennifer_weekend_8PM_8 with Dissolve(0.5)
    Jennifer "Better yet, you might learn a thing or two so I don't have to do it myself every time."
    scene Jennifer_weekend_8PM_9 with Dissolve(0.5)
    MC "Yep, I am here to watch and learn! And if any problems show up I am here to help!"
    scene Jennifer_weekend_8PM_10 with Dissolve(0.5)
    Jennifer "Problems? What problems could there even be?"
    scene Jennifer_weekend_8PM_11_12_loop with Dissolve(0.5)
    MC "Uhhh... I don't know, maybe getting stuck or something like that haha who knows it would be kinda awkward I guess but yeah anyway I guess anything can happen right? Haha!"
    scene Jennifer_weekend_8PM_13 with Dissolve(0.5)
    Jennifer "Yeahhh... that doesn't really happen, so don't worry."
    scene Jennifer_weekend_8PM_14 with Dissolve(0.5)
    $ rant_cps = 70
    $ rant_scroll_duration = 10.0
    $ rant_scroll_start_delay = 1
    $ rant_visible_height = 110
    $ rant_auto_advance_time = 10.0

    $ mc_rant = "{color=#808080}*It's happening! Oh my God is happening! I didn't think it would happen so soon. I mean I kinda hoped for it but I didn't prepare myself! She'll get in there and then she'll be stuck, booty cheeks fully in the open. But then what?! Do I act, do I slightly touch it? A slap might be too much though. Maybe a sniff? But how close? Do I get in there? Do I shove my nose all the way in it? Maybe I just pull down her pants and go to town?!!?!*"

    $ renpy.say(MC_rant, mc_rant)
    scene Jennifer_weekend_8PM_15 with Dissolve(0.5)
    Jennifer "See? Not that hard. Next time you do it, okay?"
    scene Jennifer_weekend_8PM_16 with Dissolve(0.5)
    MC "..."
    scene Jennifer_weekend_8PM_17 with Dissolve(0.5)
    MC "Sure, whatever, what do I start with?"
    scene Jennifer_weekend_8PM_18 with Dissolve(0.5)
    Jennifer "Let me see... How about..."
    scene Jennifer_weekend_8PM_19 with Dissolve(0.5)
    Jennifer "This! This should be fi-"
    scene Jennifer_weekend_8PM_20 with Dissolve(0.5)
    Jennifer "Uhhhhh..."
    scene Jennifer_weekend_8PM_21 with Dissolve(0.5)
    Jennifer "You know what? Never mind, I can do it myself."
    Jennifer "I remembered why I don't let you do the laundry..."
    scene Jennifer_weekend_8PM_22 with Dissolve(0.5)
    Jennifer "Sorry honey, but this is-"
    scene Jennifer_weekend_8PM_23 with Dissolve(0.5)
    MC "I know, I know, no worries..."
    scene Jennifer_weekend_8PM_24 with Dissolve(0.5)
    Jennifer "Thank you for offering though... we'll find something else to do together..."
    call stat_reward({"Jennifer": {"love": 2, "corruption": 2}}, return_to=None)
    $ Location = "entrance"
    $ advance_time_or_sleep()
