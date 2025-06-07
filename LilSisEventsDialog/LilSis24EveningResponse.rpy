label LilSisEvening24:

    scene EVENING14LILSIS1 with Dissolve(0.5)
    MC "{color=#808080}*Oh, Isa is watching TV. Should I spend some time with her?*{/color}"
    menu:
        "Join her":
            scene EVENING14LILSIS3 with Dissolve(0.5)
            MC "Hey sis, what are you watching?"
            scene EVENING14LILSIS2 with Dissolve(0.5)
            Isabella "Some bullshit drama, but somehow I got invested, so here I am..."
            scene EVENING14LILSIS3 with Dissolve(0.5)
            MC "Do you mind if I join?"
            scene EVENING14LILSIS2 with Dissolve(0.5)
            Isabella "If you don't mind standing, then I don't."
            extend "I'm waaaaay too comfy to move right now."
            scene EVENING14LILSIS5 with Dissolve(0.5)
            MC "Ummm......"
            extend "Are you serious?"
            scene EVENING14LILSIS4 with Dissolve(0.5)
            Isabella "Yep. I'm not moving an inch."
            scene EVENING14LILSIS5 with Dissolve(0.5)
            MC "There's a little bit of space. I shouldn't trouble you if I sit there, right?"
            scene EVENING14LILSIS4 with Dissolve(0.5)
            Isabella "Sit up, or I'll scream for mom that you're touching me!"
            scene EVENING14LILSIS5 with Dissolve(0.5)
            MC "Tsk..."
            "{color=#808080}**You walk out of the living room**{/color}"
            $ Location = "Entrance"
            $ advance_time_or_sleep()
            # TODO Dupa un timp o sa se puna pe un colt sau ceva de genu si o sa stea acolo
            # TODO Dupa un timp o sa se pun sub piciorele ei si o sa i puna picioarele in poala sau ma mai gandesc eu la altceva

        "Leave":
            MC "{color=#808080}*Maybe some other time.*{/color}"
            $ Location = "Entrance"
            $ renpy.call("GameLoop")
