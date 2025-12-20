init python:
    define_images("MC_Toilet_Alone_Piss_", "MCEvents/MC_Toilet_Piss/Alone", "MC_Toilet_Alone_Piss_", 100)

label MC_Toilet_Piss_Alone:
    scene MC_Toilet_Alone_Piss_1 with Dissolve(0.5)
    MC "..."
    scene MC_Toilet_Alone_Piss_2 with Dissolve(0.5)
    pause 3
    scene MC_Toilet_Alone_Piss_1 with Dissolve(0.5)
    "{color=#808080}**One hour passes...**"
    $ Location = "Hallway" 
    $ advance_time_or_sleep()