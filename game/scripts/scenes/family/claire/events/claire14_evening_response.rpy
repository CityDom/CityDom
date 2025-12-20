label ClaireEvening14:

    scene Claire_evening14_1 with Dissolve(0.5)
    MC "{color=#808080}*Claire just got home, should I try to talk to her?*{/color}"
    menu:
        "Talk to her":
            MC "Hey sis, I was just thinking about you, how was school?"
            scene Claire_evening14_2 with Dissolve(0.5)
            Claire "I'm not in the mood loser, leave me alone."
            scene Claire_evening14_3 with Dissolve(0.5)
            MC "Come on, Claire, don't be so mean, I just want to know how your day's been."
            MC "Is that too wrong to ask for a brother?"
            scene Claire_evening14_4 with Dissolve(0.5)
            Claire "I don't care loser."
            scene Claire_evening14_5 with Dissolve(0.5)
            Claire "Move out of the way already, you are a waste of space."
            scene Claire_evening14_6 with Dissolve(0.5)
            MC "{color=#808080}*She is such a mean bitch...*{/color}"
            $ Location = "entrance"
            $ advance_time_or_sleep()
        "Ignore her":
            $ Location = "entrance"
            $ advance_time_or_sleep()
