label BigSisEvening14:

    scene EVENING14BIGSIS1 with Dissolve(0.5)
    MC "{color=#808080}*Claire just got home, should I try to talk to her?*{/color}"
    menu:
        "Talk to her":
            MC "Hey sis, I was just thinking about you, how was school?"
            scene EVENING14BIGSIS2 with Dissolve(0.5)
            Clair "I'm not in the mood loser, leave me alone."
            scene EVENING14BIGSIS3 with Dissolve(0.5)
            MC "Come on, Claire, don't be so mean, I just want to know how your day's been."
            MC "Is that too wrong to ask for a brother?"
            scene EVENING14BIGSIS4 with Dissolve(0.5)
            Clair "I don't care loser."
            scene EVENING14BIGSIS5 with Dissolve(0.5)
            Clair "Move out of the way already, you are a waste of space."
            scene EVENING14BIGSIS6 with Dissolve(0.5)
            MC "{color=#808080}*She is such a mean bitch...*{/color}"
            $ Location = "entrance"
            $ advance_time_or_sleep()
        "Ignore her":
            $ Location = "entrance"
            $ advance_time_or_sleep()
