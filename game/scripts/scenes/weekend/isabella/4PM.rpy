init python:
    define_images("Isabella_weekend_4PM_", "WeekendScenes/IsabellaScenes/4PM", "Isabella_weekend_4PM_", 100)

label Isabella_weekend_4PM:
    scene Isabella_weekend_4PM_1 with Dissolve(0.5)
    MC "'Sup! Did Criss leave already?"
    scene Isabella_weekend_4PM_2 with Dissolve(0.5)
    Isabella "Nope. She's at the toilet."
    scene Isabella_weekend_4PM_3 with Dissolve(0.5)
    MC "Oh, really? I had no idea..."
    scene Isabella_weekend_4PM_6 with Dissolve(0.5)
    Isabella "I'm sure you didn't..."
    scene Isabella_weekend_4PM_4 with Dissolve(0.5)
    MC "Anyway, what's up?"
    scene Isabella_weekend_4PM_5 with Dissolve(0.5)
    Isabella "I'm trying to find a game to play with Criss."
    scene Isabella_weekend_4PM_7 with Dissolve(0.5)
    MC "And I'm invited as well, right?"
    scene Isabella_weekend_4PM_8 with Dissolve(0.5)
    Isabella "Fuck no you're not."
    scene Isabella_weekend_4PM_9 with Dissolve(0.5)
    MC "Ahhhhh, you're such a tsundere..."
    scene Isabella_weekend_4PM_10 with Dissolve(0.5)
    Isabella "A what? Do you even know what that means?"
    Isabella "And don't get so comfortable, I told you that you're not invited."
    scene Isabella_weekend_4PM_11 with Dissolve(0.5)
    Isabella "God, you're so annoying"
    scene Isabella_weekend_4PM_12 with Dissolve(0.5)
    Isabella "When Criss comes back you're out."
    scene Isabella_weekend_4PM_13 with Dissolve(0.5)
    MC "Yeah, yeah, sure..."
    MC "You're forgetting when we were little and you were asking me to play with you all the time."
    scene Isabella_weekend_4PM_14 with Dissolve(0.5)
    MC "They grow so fast... and they forget about you..."
    scene Isabella_weekend_4PM_15 with Dissolve(0.5)
    Isabella "Oh God, you're starting to sound like mom..."
    scene Isabella_weekend_4PM_16 with Dissolve(0.5)
    Isabella "And don't play that card with me, I was four or five when you left."
    Isabella "And Claire was a bitch back then too, so I had no one to play with."
    scene Isabella_weekend_4PM_17 with Dissolve(0.5)
    Isabella "Although I'm surprised you remember that time... You don't usually talk about it."
    Isabella "We used to be together quite a lot, remember?"
    scene Isabella_weekend_4PM_18 with Dissolve(0.5)
    Isabella "......."
    scene Isabella_weekend_4PM_19 with Dissolve(0.5)
    Isabella "Hellooooooo!"
    scene Isabella_weekend_4PM_20 with Dissolve(0.5)
    MC "HRRRRNGH… shhhhh… HRRRRNGH…"
    scene Isabella_weekend_4PM_21 with Dissolve(0.5)
    Isabella "And you wonder why I don't wanna play with you anymore..."
    call stat_reward({"Isabella": {"love": 2}}, return_to=None)
    $ Location = "Hallway"
    $ advance_time_or_sleep()
