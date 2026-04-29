init python:
    define_images("Criss_weekend_4PM_", "WeekendScenes/CrissScenes/4PM", "Criss_weekend_4PM_", 100)

label Criss_weekend_4PM:
    scene Criss_weekend_4PM_1 with Dissolve(0.5)
    MC "Is... Is that Criss?"
    MC "Oh my..."
    scene Criss_weekend_4PM_2 with Dissolve(0.5)
    Mhyrorin "\"Oh my\" what? C'mon, give me better comms!"
    scene Criss_weekend_4PM_3 with Dissolve(0.5)
    MC "She... she is naked..."
    scene Criss_weekend_4PM_4 with Dissolve(0.5)
    Mhyrorin "Naked? What do you mean she's naked? While taking a piss?"
    scene Criss_weekend_4PM_5 with Dissolve(0.5)
    MC "Okay, first of all, you can't be the one that's acting so surprised about something like that."
    scene Criss_weekend_4PM_6 with Dissolve(0.5)
    Mhyrorin "Huh? Why couldn't I be? I don't get it."
    scene Criss_weekend_4PM_7 with Dissolve(0.5)
    MC "....."
    scene Criss_weekend_4PM_8 with Dissolve(0.5)
    MC "Nothing... Never mind."
    scene Criss_weekend_4PM_9 with Dissolve(0.5)
    MC "Anyway, she got on one of those onesies pajamas, and it doesn't seem to have a zipper I guess."
    scene Criss_weekend_4PM_10 with Dissolve(0.5)
    Mhyrorin "Myeah... and you say I'm weird."
    Mhyrorin "Okay, spit it out already before she puts it back on."
    scene Criss_weekend_4PM_11 with Dissolve(0.5)
    MC "It's like 40D... maybe 42..."
    MC "Bigger than I expected."
    scene Criss_weekend_4PM_10 with Dissolve(0.5)
    Mhyrorin "Noted. What else? Do you see any tattoos? Piercings? Scars? Birthmarks?"
    scene Criss_weekend_4PM_12 with Dissolve(0.5)
    MC "Hmmm, It doesn't seem like she has any, but I can't see her very clearly..."
    scene Criss_weekend_4PM_13 with Dissolve(0.5)
    MC "Also, we need to bounce, she'll get up soon."
    scene Criss_weekend_4PM_14 with Dissolve(0.5)
    MC "Tsk, and it was getting good..."
    call stat_reward({"Criss": {"Corruption": 2}}, return_to=None)
    $ Location = "Hallway"
    $ advance_time_or_sleep()