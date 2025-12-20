label AfterGoToSchoolMinigameSuccess():
    show GoToSchoolMovieBackground1
    show GoToSchoolFirstScenes16
    Isabella "Please stop, [MC], I'm feeling a bit weird, I think the cars AC stopped working."
    Isabella "And we almost arrived, I don't want to go to school looking like a mess."
    scene GoToSchoolFirstScenes17 with Dissolve(0.5)
    Jennifer "Stop fighting kids!"
    scene GoToSchoolFirstScenes18 with Dissolve(0.5)
    MC "We are not fighting mom! If you don't hear what we are saying it doesn't mean we are fighting!"
    scene GoToSchoolFirstScenes17 with Dissolve(0.5)
    Jennifer "Just get out of the car already, I'm late for work!"
    if beenToSchoolOnce: 
        $ LocationID = 1
        $ Location = "school"
        $ calendar.Hours = 6
        $ school_clock.hour = 12
        $ renpy.call("GameLoop")
    else:
        jump AfterGoToSchoolMinigame