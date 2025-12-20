init python:
    define_images("SelinaPauseScene", "SchoolFirstPause/SelinaEventScene", "SelinaPauseScene", 60)

label SelinaFirstPauseScene:
    scene SelinaPauseScene1 with Dissolve(0.5)
    MC "Hey Selina!"
    scene SelinaPauseScene2 with Dissolve(0.5)
    Armand "Huh?"
    scene SelinaPauseScene3 with Dissolve(0.5)
    Armand "Selina, I think this random is trying to talk to you."
    scene SelinaPauseScene2 with Dissolve(0.5)
    Selina "Huh?"
    scene SelinaPauseScene4 with Dissolve(0.5)
    Selina "Ughhh... this guy?"
    Selina "I don't know his name, but I think he just moved in my class."
    Selina "He must think we are friends or something."
    scene SelinaPauseScene5 with Dissolve(0.5)
    $ renpy.pause(0.1, hard=True)
    scene SelinaPauseScene6 with Dissolve(0.5)
    $ renpy.pause(0.1, hard=True)
    scene SelinaPauseScene5 with Dissolve(0.5)
    $ renpy.pause(0.1, hard=True)
    scene SelinaPauseScene6 with Dissolve(0.5)
    $ renpy.pause(0.1, hard=True)
    scene SelinaPauseScene5 with Dissolve(0.5)
    Selina "Get lost looser, I won't give you any money."
    scene SelinaPauseScene7 with Dissolve(0.5)
    Armand "Haha, that's right, get lost!"
    scene SelinaPauseScene8 with Dissolve(0.5)
    MC "{color=#808080}*Tsk...*"
    MC "{color=#808080}*She is worst than Claire.*"
    MC "{color=#808080}*And Maria was right, she really is just an entitled bitch, no other personality at all.*"
    scene SelinaPauseScene9 with Dissolve(0.5)
    Selina "Do you have a hearing problem?"
    Selina "I said get lost!"
    scene BlackScreen with Dissolve(0.5)
    $ Maria_Report_Selina = True
    $ advance_time_or_sleep()
