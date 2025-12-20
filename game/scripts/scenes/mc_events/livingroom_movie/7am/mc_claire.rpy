init python:
    define_images("MC_Livingroom_Movie_7AM_Claire_", "MCEvents/MC_Livingroom_Movie/7AM/Claire", "MC_Livingroom_Movie_7AM_Claire_", 100)

label MC_Livingroom_Movie_7AM_Claire_Label:
    scene MC_Livingroom_Movie_7AM_Claire_1 with Dissolve(0.5)
    "{color=#808080}**Turns on the TV**"
    scene MC_Livingroom_Movie_7AM_Claire_2 with Dissolve(0.5)
    Claire "What do you think you're doing?!"
    Claire "I'm not gonna sit in here listening to whatever you're watching."
    Claire "Turn it off or leave!"
    scene MC_Livingroom_Movie_7AM_Claire_3 with Dissolve(0.5)
    MC "Wait what? Really? But it's not even that loud."
    MC "I can barely hear it myself."
    scene MC_Livingroom_Movie_7AM_Claire_4 with Dissolve(0.5)
    Claire "I don't care how loud it is!"
    Claire "I told you to turn it off!"
    scene MC_Livingroom_Movie_7AM_Claire_5 with Dissolve(0.5)
    Claire "Or do I gotta get up and turn it off myself?"
    scene MC_Livingroom_Movie_7AM_Claire_6 with Dissolve(0.5)
    MC "No, no, I'll turn it off..."
    $ advance_time_or_sleep()