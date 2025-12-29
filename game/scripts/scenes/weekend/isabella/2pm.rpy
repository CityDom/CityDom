init python:
    define_images("Isabella_weekend_2PM_", "WeekendScenes/IsabellaScenes/2PM", "Isabella_weekend_2PM_", 100)

label Isabella_weekend_2PM:
    scene Isabella_weekend_2PM_1 with Dissolve(0.5)
    MC "..."
    $ renpy.call("GameLoop")
