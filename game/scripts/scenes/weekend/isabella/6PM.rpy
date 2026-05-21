init python:
    define_images("Isabella_weekend_6PM_", "WeekendScenes/IsabellaScenes/6PM", "Isabella_weekend_6PM_", 100)

label Isabella_weekend_6PM:
    scene Isabella_weekend_6PM_1 with Dissolve(0.5)
    pause
    scene Isabella_weekend_6PM_2 with Dissolve(0.5)
    MC "Hey gi-"
    scene Isabella_weekend_6PM_3 with Dissolve(0.5)
    IsaAndCriss "SHUT THE FUCK UP!!!"
    scene Isabella_weekend_6PM_4 with Dissolve(0.5)
    Criss "Oh my God, I'm so sorry!"
    scene Isabella_weekend_6PM_5 with Dissolve(0.5)
    Isabella "SHHHHHHHHH!!!!"
    scene Isabella_weekend_6PM_6 with Dissolve(0.5)
    MCW "It's okay..."
    scene Isabella_weekend_6PM_7 with Dissolve(0.5)
    pause
    scene Isabella_weekend_6PM_8 with Dissolve(0.5)
    MCW "Oh shi... what the fuck?!"
    scene Isabella_weekend_6PM_9 with Dissolve(0.5)
    Isabella "Sit down already! What are you tripping on?!"
    scene Isabella_weekend_6PM_10 with Dissolve(0.5)
    MCW "My bad, thought I saw a rat..."
    scene Isabella_weekend_6PM_11 with Dissolve(0.5)
    Isabella "Finally..."
    scene Isabella_weekend_6PM_12 with Dissolve(0.5)
    Mhyrorin "A rat? Really? And you call me mean..."
    scene Isabella_weekend_6PM_13 with Dissolve(0.5)
    MC "{color=#808080}*My bad, okay? You startled me... what are you doing here anyway?*"
    scene Isabella_weekend_6PM_14 with Dissolve(0.5)
    Mhyrorin "Watching the show... but I don't really see the attraction. These men look like lesbians..."
    Mhyrorin "Also, you don't have to think it, I got you covered. How many times do I have to say it?"
    scene Isabella_weekend_6PM_15 with Dissolve(0.5)
    MC "Oh, really? You can do it in situations like this as well?"
    scene Isabella_weekend_6PM_16 with Dissolve(0.5)
    Isabella "Tsk, do what? Shut up already!"
    scene Isabella_weekend_6PM_17 with Dissolve(0.5)
    Mhyrorin "Haha, dumbass! Your mom is a rat!"
    scene BlackScreen with Dissolve(0.5)
    "20 minutes later..."
    scene Isabella_weekend_6PM_18 with Dissolve(0.5)
    MC "{color=#808080}*What did I get myself into...?*"
    scene Isabella_weekend_6PM_19 with Dissolve(0.5)
    Isabella "Oh my God, don't let him talk to you like that! You know what he did to you!"
    Criss "Girl, look at him... he's doing the soft voice again. The nerve!"
    Isabella "Yeah, and the others hairline is receding per sentence he gets out."
    Criss "So embarrassing... I can't with these men!"
    Isabella "Totally, they are all the same!"
    scene Isabella_weekend_6PM_20 with Dissolve(0.5)
    Mhyrorin "Uhhh... I got lost... why are these girls so mad again?"
    scene Isabella_weekend_6PM_21 with Dissolve(0.5)
    MC "{color=#808080}*How the hell am I supposed to know...*"
    scene Isabella_weekend_6PM_22 with Dissolve(0.5)
    Mhyrorin "Ask Isa then!"
    scene Isabella_weekend_6PM_23 with Dissolve(0.5)
    MC "{color=#808080}*Ughhhh...*{color=#808080}"
    scene Isabella_weekend_6PM_24 with Dissolve(0.5)
    MC "Why are they so mad again? He seemed nice-"
    scene Isabella_weekend_6PM_25 with Dissolve(0.5)
    Isabella "HAHA! You have no idea! You missed last week!"
    Isabella "He took her mom on a date last episode! All while she was crying, thinking he was hurt in that car accident!"
    scene Isabella_weekend_6PM_26 with Dissolve(0.5)
    MC "{color=#808080}*Hmph... he's more based than I thought...*"
    scene Isabella_weekend_6PM_27 with Dissolve(0.5)
    Mhyrorin "No fucking way he went out with her!!!!"
    scene Isabella_weekend_6PM_28 with Dissolve(0.5)
    Mhyrorin "Now ask if he fucked her!!!!"
    scene Isabella_weekend_6PM_29 with Dissolve(0.5)
    MC "{color=#808080}*It will be a long episode...*"
    call stat_reward({"Criss": {"love": 2}, "Isabella": {"love": 2}}, return_to=None)
    $ Location = "Hallway"
    $ advance_time_or_sleep()