label IsabellaEvening24:

    scene Isabella_evening24_1 with Dissolve(0.5)
    MC "{color=#808080}*Oh, Isa is watching TV. Should I spend some time with her?*{/color}"
    menu:
        "Join her":
            scene Isabella_evening24_3 with Dissolve(0.5)
            MC "Hey sis, what are you watching?"
            scene Isabella_evening24_2 with Dissolve(0.5)
            Isabella "Some bullshit drama, but somehow I got invested, so here I am..."
            scene Isabella_evening24_3 with Dissolve(0.5)
            MC "Do you mind if I join?"
            scene Isabella_evening24_2 with Dissolve(0.5)
            Isabella "If you don't mind standing, then I don't."
            extend "I'm waaaaay too comfy to move right now."
            scene Isabella_evening24_5 with Dissolve(0.5)
            MC "Ummm......"
            extend "Are you serious?"
            scene Isabella_evening24_4 with Dissolve(0.5)
            Isabella "Yep. I'm not moving an inch."
            scene Isabella_evening24_5 with Dissolve(0.5)
            MC "There's a little bit of space. I shouldn't trouble you if I sit there, right?"
            scene Isabella_evening24_4 with Dissolve(0.5)
            Isabella "Sit up, or I'll scream for mom that you're touching me!"
            scene Isabella_evening24_5 with Dissolve(0.5)
            MC "Tsk..."
            "{color=#808080}**You walk out of the living room**{/color}"
            $ Location = "Entrance"
            $ advance_time_or_sleep()
            # TODO After a while, she will sit in a corner or something like that and stay there
            # TODO After a while, she will get under her legs and put her feet in his lap or I'll think of something els'

        "Leave":
            MC "{color=#808080}*Maybe some other time.*{/color}"
            $ Location = "Entrance"
            $ renpy.call("GameLoop")
