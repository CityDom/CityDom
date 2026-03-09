init python:
    def can_sleep_in_current_room():
        return normalize_location_key(Location) == "my room"

label SleepEventButton:
    if can_sleep_in_current_room():
        jump SleepEvent
    else:
        MC "I will only sleep in my room."
        $ renpy.call("GameLoop")
