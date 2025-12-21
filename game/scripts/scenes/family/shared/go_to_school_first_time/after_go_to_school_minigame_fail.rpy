label AfterGoToSchoolMinigameFail():
    show GoToSchoolMovieBackground1
    show GoToSchoolFirstScenes19
    Isabella "WHAT THE FUCK ARE YOU DOING [MC_upper]?!?!"
    Isabella "TAKE YOUR HAND OFF ME!"
    scene GoToSchoolFirstScenes17 with Dissolve(0.5)
    Jennifer "Stop fighting kids!"
    scene GoToSchoolFirstScenes18 with Dissolve(0.5)
    Isabella "Then tell this creep to keep his hands in place"
    MC "I just rolled over on that last curb, I'm sorry!"
    scene GoToSchoolFirstScenes17 with Dissolve(0.5)
    Jennifer "Just get out of the car already, I'm late for work!"
    if beenToSchoolOnce: 
        $ LocationID = 1
        $ Location = "school"
        $ calendar.Hours = 6
        $ school_clock.reset()
        $ renpy.call("GameLoop")
    else:
        jump AfterGoToSchoolMinigame
