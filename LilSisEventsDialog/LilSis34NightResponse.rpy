label LilSisNight34:

    menu:
        "Knock":
            "{color=#808080}**Knock knock**{/color}"
            Isabella "Occupieeeed!!"
            MC "I really need to use the restroom sis please!!"
            Isabella "I'm almost done... just wait a second..."
            MC "I can't hold it anymore Isabella, pleaseeeee!!"
            Isabella "NO!!! go downstairs if you really need to!"
            MC "It's occupied there aswell!"
            Isabella "I don't care, piss yourself then!"
            MC "{color=#808080}*Fuck... I'll have to wait then...*{/color}"
            jump LilSisNight34
        "Peep":
            scene NIGHT34LILSIS1 with Dissolve(0.5)
            MC "Oh my god, I can almost see her pussy!!"
            MC "If she would open her legs just a little more..."
            MC "Anyway... I should leave before somebody finds me peeping through the restroom keyhole."
            $ Location = "Hallway"
            $ renpy.call("GameLoop")
        "Open":
            scene NIGHT34LILSIS2 with Dissolve(0.5)
            Isabella "AAAAAAAAAAAAAAAAAAAAAAAA"
            Isabella "GET OUT!!!!!!!!!!!!!!!!!!"
            "{color=#808080}**You leave in a hurry**{/color}"
            "{color=#808080}**Isabella love - 5**{color=#808080}"
            $ LilSis_love = LilSis_love - 5
            $ check_and_update_character_stats("LilSis")
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "Leave":
            $ Location = "Hallway"
            $ renpy.call("GameLoop")
