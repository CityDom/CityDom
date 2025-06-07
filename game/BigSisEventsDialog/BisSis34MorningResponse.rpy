label BigSisMorning34:

    scene NIGHT24MOM0 with Dissolve(0.5)
    menu:
        "Knock":
            "{color=#808080}**Knock knock**{/color}"
            Clair "It's occupied."
            MC "I really have to go to the toilet, please!"
            Clair "Are you crazy or something?"
            Clair "Leave already!"
            MC "But downstairs is also occupied!"
            Clair "I don't give a fuck!"
            MC "{color=#808080}*Fuck... I'll have to wait then...*{/color}"
            jump BigSisMorning34
        "Peep":
            scene MORNING34BIGSIS1 with Dissolve(0.5)
            MC "{color=#808080}*Oh my god, it's Claire!!*{/color}"
            MC "{color=#808080}*And she doesn't have any pants on.*{/color}"
            MC "{color=#808080}*But I can't seem to see anything if she stays in that position.*{/color}"
            MC "{color=#808080}*I better leave before anyone sees me.*{/color}"
            $ Location = "Hallway"
            $ renpy.call("GameLoop")
        "Open":
            MC "{color=#808080}*If I do that... I'm dead.*{/color}"
            MC "{color=#808080}*Like, she literally kills me.*{/color}"
            $ Location = "Hallway"
            $ renpy.call("GameLoop")
            return
        "Leave":
            $ Location = "Hallway"
            $ renpy.call("GameLoop")
