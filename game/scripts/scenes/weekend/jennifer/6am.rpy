init python:
    define_images("Jennifer_weekend_6AM_", "WeekendScenes/JenniferScenes/6AM", "Jennifer_weekend_6AM_", 100)

label Jennifer_weekend_6AM:
    scene Jennifer_weekend_6AM_1 with Dissolve(0.5)
    MC "G'morning, Mom!"
    scene Jennifer_weekend_6AM_2 with Dissolve(0.5)
    Jennifer "AAAAAAAAAAAA!!!!"
    scene Jennifer_weekend_6AM_3 with Dissolve(0.5)
    Jennifer "[MC], you scared the crap out of me!"
    scene Jennifer_weekend_6AM_4 with Dissolve(0.5)
    MC "...."
    scene Jennifer_weekend_6AM_5 with Dissolve(0.5)
    MC "Am I this ugly first thing in the morning?"
    scene Jennifer_weekend_6AM_6 with Dissolve(0.5)
    Jennifer "Oh no, honey, it's not that."
    Jennifer "But you really need to stop sneaking up on me like that."
    scene Jennifer_weekend_6AM_7 with Dissolve(0.5)
    MC "Yeah, you're right. I'll send you an email in advance next time."
    scene Jennifer_weekend_6AM_8 with Dissolve(0.5)
    Jennifer "Haha, very funny, honey. I'm surprised you kids even know what an email is these days."
    scene Jennifer_weekend_6AM_9 with Dissolve(0.5)
    Jennifer "Now tell me, to what do I owe the pleasure of this early morning visit?"
    scene Jennifer_weekend_6AM_10 with Dissolve(0.5)
    MC "Oh, c'mon, Mom. Do I really need a reason to want to spend time with my mom first thing in the morning?"
    scene Jennifer_weekend_6AM_11 with Dissolve(0.5)
    Jennifer "Really...? Then let's spend some time together."
    Jennifer "I'll start loading the washing machine, and you can water the plants."
    scene Jennifer_weekend_6AM_12 with Dissolve(0.5)
    Jennifer "And after that, you can move on to the flowers in the garden while I prepare breakfast."
    scene Jennifer_weekend_6AM_13 with Dissolve(0.5)
    MC "Okay, Mom. Wonderful chat we had. See you around!"
    scene Jennifer_weekend_6AM_14 with Dissolve(0.5)
    Jennifer "Mhm. That's what I thought."
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}**Jennifer love +2**{/color}"
    $ Jennifer_love = Jennifer_love + 2
    $ check_and_update_character_stats("Jennifer")
    $ Location = "Hallway"
    $ advance_time_or_sleep()
