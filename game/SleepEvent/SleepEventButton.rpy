label SleepEventButton:
    if current_location == "my room":
        jump SleepEvent
    else:
        MC "I will only sleep in my room."
        $ renpy.call("GameLoop")
