label ClaireEvening44:

    scene Claire_evening44_1 with Dissolve(0.5)
    MC "{color=#808080}*Sis seems to be doing her homework.*{/color}"
    MC "{color=#808080}*Should I go talk to her?*{/color}"
    menu:
        "Talk to her":
            MC "Hey Claire! What are you up to?"
            scene Claire_evening44_2 with Dissolve(0.5)
            Claire "....."
            MC "Ummm.... Claire?"
            scene Claire_evening44_3 with Dissolve(0.5)
            Claire "...."
            MC "Helloooo!! Claaaire!"
            scene Claire_evening44_4 with Dissolve(0.5)
            Claire "What the fuck does it looks like I'm doing?!"
            Claire "I'm trying to do my damn homework!"
            scene Claire_evening44_5 with Dissolve(0.5)
            MC "Come on sis, don't be so mean, I just wanted to see how are you."
            scene Claire_evening44_4 with Dissolve(0.5)
            Claire "I'm not in the mood to see your face loser, now get out of my room until I get up from this chair."
            MC "{color=#808080}*God she's such a fucking bitch!*{/color}"
            "{color=#808080}*You leave the room.*{/color}"
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "Leave":
            MC "{color=#808080}*Let's leave her alone for now...*{/color}"
            $ Location = "Hallway"
            $ renpy.call("GameLoop")