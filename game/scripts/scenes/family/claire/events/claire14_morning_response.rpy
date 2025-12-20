label ClaireMorning14:

    scene Claire_morning14_1 with Dissolve(0.5) 
    MC "{color=#808080}*It looks like Claire is waking up. Should I go talk to her?*{/color}"
    menu:
        "Talk to her":
            scene Claire_morning14_2 with Dissolve(0.5)
            "{color=#808080}**As you walk in, the door makes a small squeak.**{/color}" 
            scene Claire_morning14_3 with Dissolve(0.5)
            Claire "I'm awake, just let me lay in bed a few more minutes."
            Claire "It's early anyway!"
            scene Claire_morning14_4 with Dissolve(0.5)
            MC "Good morning Claire! I just wanted to see how you were doing."
            scene Claire_morning14_5 with Dissolve(0.5)
            Claire "Huh, what the fuck?"
            scene Claire_morning14_7 with Dissolve(0.5)
            Claire "Oh. It's you..."
            Claire "What do you want?"
            scene Claire_morning14_6 with Dissolve(0.5)
            MC "I told you. I just wanted to see how you were do-"
            scene Claire_morning14_7 with Dissolve(0.5)
            Claire "Actually, I don't even care, just get the fuck out of my room."
            scene Claire_morning14_6 with Dissolve(0.5)
            MC "But..."
            scene Claire_morning14_7 with Dissolve(0.5)
            Claire "I don't care [MC], just get out."
            Claire "Don't make me beat your ass again."
            "{color=#808080}**You leave the room**{/color}"
            $ Location = "Hallway"
            $ advance_time_or_sleep()
        "Leave":
            MC "Maybe some other time, I'm pretty sure I'm just wasting my time with her for now."
            $ Location = "Hallway"
            $ renpy.call("GameLoop")