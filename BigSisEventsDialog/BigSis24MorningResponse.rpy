label BigSisMorning24:

    scene MORNING24BIGSIS1 with Dissolve(0.5)
    MC "{color=#808080}*Claire seems to be drinking her coffee.*{/color}"
    MC "{color=#808080}*Should I try to talk to her?*{/color}"
    menu:
        "Talk to her":
            scene MORNING24BIGSIS2 with Dissolve(0.5)
            MC "Hey Claire, how are you doing?"
            Clair "......."
            MC "Are you enjoying your coffee?"
            Clair "........"
            scene MORNING24BIGSIS3 with Dissolve(0.5)
            MC "Heeeeeeey, Claireeeeee!"
            scene MORNING24BIGSIS5 with Dissolve(0.5)
            Clair "Oh my god, can't you take a fucking hint?!"
            Clair "Can I drink my damn coffee in peace?"
            scene MORNING24BIGSIS4 with Dissolve(0.5)
            MC "I'm sorry, I just wanted to see how you're doing..."
            scene MORNING24BIGSIS5 with Dissolve(0.5)
            Clair "Haven't left yet?"
            Clair "I don't give a fuck what u want."
            Clair "Bye!"
            scene MORNING24BIGSIS2 with Dissolve(0.5)
            MC "{color=#808080}*She's such a mean fucking bitch*{/color}"
            MC "{color=#808080}*I'll just leave for now*{/color}"
            $ Location = "Entrance"
            $ advance_time_or_sleep()
        "Leave":
            MC "{color=#808080}*I don't have the disposition to deal with her bitch attitude right now.*{/color}"
            MC "{color=#808080}*I'd better leave.*{/color}"
            $ Location = "Entrance"
            $ renpy.call("GameLoop")