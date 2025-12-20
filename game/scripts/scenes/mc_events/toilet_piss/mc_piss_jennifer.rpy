init python:
    define_images("MC_Toilet_Jennifer_Piss_", "MCEvents/MC_Toilet_Piss/Jennifer", "MC_Toilet_Jennifer_Piss_", 100)

label MC_Toilet_Piss_Jennifer:
    scene MC_Toilet_Jennifer_Piss_1 with Dissolve(0.5)
    MC "..."
    scene MC_Toilet_Jennifer_Piss_2 with Dissolve(0.5)
    MC "..."
    scene MC_Toilet_Jennifer_Piss_3 with Dissolve(0.5)
    $ renpy.pause(0.2, hard=True)
    scene MC_Toilet_Jennifer_Piss_4 with Dissolve(0.2)
    $ renpy.pause(0.2, hard=True)
    scene MC_Toilet_Jennifer_Piss_3 with Dissolve(0.2)
    $ renpy.pause(0.2, hard=True)
    scene MC_Toilet_Jennifer_Piss_4 with Dissolve(0.2)
    $ renpy.pause(0.2, hard=True)
    scene MC_Toilet_Jennifer_Piss_3 with Dissolve(0.2)
    $ renpy.pause(0.2, hard=True)
    scene MC_Toilet_Jennifer_Piss_4 with Dissolve(0.2)
    $ renpy.pause(0.2, hard=True)
    scene MC_Toilet_Jennifer_Piss_5 with Dissolve(0.5)
    MC "It's occupied!!"
    scene MC_Toilet_Jennifer_Piss_6 with Dissolve(0.5)
    Jennifer "Are you getting out soon? I really need to go!"
    scene MC_Toilet_Jennifer_Piss_5 with Dissolve(0.5)
    MC "I'll be out soon! Sorry!"
    scene MC_Toilet_Jennifer_Piss_7 with Dissolve(0.5)
    Jennifer "It's okay honey, take your time."
    Jennifer "It's not healthy to hurry when you are using the toilet."
    Jennifer "I will go down stairs!"
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}**One hour passes...**"
    $ Location = "Hallway" 
    $ advance_time_or_sleep()