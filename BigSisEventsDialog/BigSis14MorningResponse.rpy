label BigSisMorning14:

    scene MORNING14BIGSIS1 with Dissolve(0.5) 
    MC "{color=#808080}*It looks like Claire is waking up. Should I go talk to her?*{/color}"
    menu:
        "Talk to her":
            scene MORNING14BIGSIS2 with Dissolve(0.5)
            "{color=#808080}**As you walk in, the door makes a small squeak.**{/color}" 
            scene MORNING14BIGSIS3 with Dissolve(0.5)
            Clair "I'm awake, just let me lay in bed a few more minutes."
            Clair "It's early anyway!"
            scene MORNING14BIGSIS4 with Dissolve(0.5)
            MC "Good morning Claire! I just wanted to see how you were doing."
            scene MORNING14BIGSIS5 with Dissolve(0.5)
            Clair "Huh, what the fuck?"
            scene MORNING14BIGSIS7 with Dissolve(0.5)
            Clair "Oh. It's you..."
            Clair "What do you want?"
            scene MORNING14BIGSIS6 with Dissolve(0.5)
            MC "I told you. I just wanted to see how you were do-"
            scene MORNING14BIGSIS7 with Dissolve(0.5)
            Clair "Actually, I don't even care, just get the fuck out of my room."
            scene MORNING14BIGSIS6 with Dissolve(0.5)
            MC "But..."
            scene MORNING14BIGSIS7 with Dissolve(0.5)
            Clair "I don't care [MC], just get out."
            Clair "Don't make me beat your ass again."
            "{color=#808080}**You leave the room**{/color}"
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "Leave":
            MC "Maybe some other time, I'm pretty sure I'm just wasting my time with her for now."
            $ Location = "Hallway"
            $ renpy.call("GameLoop")