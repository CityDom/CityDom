label ClaireMorning24:

    scene Claire_morning24_1 with Dissolve(0.5)
    MC "{color=#808080}*Claire seems to be drinking her coffee.*{/color}"
    MC "{color=#808080}*Should I try to talk to her?*{/color}"
    menu:
        "Talk to her":
            scene Claire_morning24_2 with Dissolve(0.5)
            MC "Hey Claire, how are you doing?"
            Claire "......."
            MC "Are you enjoying your coffee?"
            Claire "........"
            scene Claire_morning24_3 with Dissolve(0.5)
            MC "Heeeeeeey, Claireeeee!"
            scene Claire_morning24_5 with Dissolve(0.5)
            Claire "Oh my god, can't you take a fucking hint?!"
            Claire "Can I drink my damn coffee in peace?"
            scene Claire_morning24_4 with Dissolve(0.5)
            MC "I'm sorry, I just wanted to see how you're doing..."
            scene Claire_morning24_5 with Dissolve(0.5)
            Claire "Haven't left yet?"
            Claire "I don't give a fuck what u want."
            Claire "Bye!"
            scene Claire_morning24_2 with Dissolve(0.5)
            MC "{color=#808080}*She's such a mean fucking bitch*{/color}"
            MC "{color=#808080}*I'll just leave for now*{/color}"
            $ Location = "Entrance"
            $ advance_time_or_sleep()
        "Leave":
            MC "{color=#808080}*I don't have the disposition to deal with her bitch attitude right now.*{/color}"
            MC "{color=#808080}*I'd better leave.*{/color}"
            $ Location = "Entrance"
            $ renpy.call("GameLoop")