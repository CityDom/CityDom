init python:
    define_images("Isabella_weekend_9PM_", "WeekendScenes/IsabellaScenes/9PM", "Isabella_weekend_9PM_", 100)


image Isabella_weekend_9PM_struggle:
    "Isabella_weekend_9PM_11" with Dissolve(0.3)
    pause 0.3
    "Isabella_weekend_9PM_12" with Dissolve(0.3)
    pause 0.3
    repeat 7


label Isabella_weekend_9PM:
    scene Isabella_weekend_9PM_1 with Dissolve(1)
    Isabella "Finally decided to show yourself, huh?"
    Isabella "I'm surprised you had the balls to do it."
    scene Isabella_weekend_9PM_2 with Dissolve(0.5)
    MC "Huh? What are you doing? And why are you sitting alone with the lights off? It's creepy as fuck."
    scene Isabella_weekend_9PM_3 with Dissolve(0.5)
    MC "I can't even find the light switch..."
    scene Isabella_weekend_9PM_4 with Dissolve(0.5)
    MC "Oh, there it is!"
    scene Isabella_weekend_9PM_5 with Dissolve(0.5)
    pause
    Isabella "You're mine now."
    scene Isabella_weekend_9PM_6 with Dissolve(0.5)
    Isabella "UGGGGGGGGGGHHHHHH!!!!!!"
    scene Isabella_weekend_9PM_7 with Dissolve(0.5)
    MC "Uhhh... what are you doing?"
    scene Isabella_weekend_9PM_8 with Dissolve(0.5)
    Isabella "Are you made of fucking bricks? What the fuck is this?!"
    scene Isabella_weekend_9PM_9 with Dissolve(0.5)
    MC "Easy on the language missy!"
    MC "Come here!"
    scene Isabella_weekend_9PM_10 with Dissolve(0.5)
    Isabella "KYAAAAAAAA!!!"
    scene Isabella_weekend_9PM_struggle with Dissolve(0.5)
    Isabella "Put me down and fight me like a man! {w=3.5}{nw}"

    return