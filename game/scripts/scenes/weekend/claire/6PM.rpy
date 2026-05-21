init python:
    define_images("Claire_weekend_6PM_", "WeekendScenes/ClaireScenes/6PM", "Claire_weekend_6PM_", 100)

label Claire_weekend_6PM:
    scene Claire_weekend_6PM_1 with Dissolve(0.5)
    MC "Oh, hey Claire! Are you leaving?"
    scene Claire_weekend_6PM_2 with Dissolve(0.5)
    Claire "I just arrived..."
    scene Claire_weekend_6PM_3 with Dissolve(0.5)
    Claire "Not that you would notice I was gone. Move out of the way."
    scene Claire_weekend_6PM_4 with Dissolve(0.5)
    MC "{color=#808080}*Welcome home I guess...*{/color}"
    scene BlackScreen with Dissolve(0.5)
    $ Location = "Entrance"
    $ advance_time_or_sleep()