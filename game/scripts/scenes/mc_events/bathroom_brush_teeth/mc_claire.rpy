init python:
    define_images("MC_Bathroom_BrushTeeth_Claire_", "MCEvents/MC_Bathroom_BrushTeeth/Claire", "MC_Bathroom_BrushTeeth_Claire_", 100)

label MC_Bathroom_BrushTeeth_Claire:
    scene MC_Bathroom_BrushTeeth_Claire_1 with Dissolve(0.5)
    MC "..."
    scene MC_Bathroom_BrushTeeth_Claire_2 with Dissolve(0.5)
    Claire "...."
    scene MC_Bathroom_BrushTeeth_Claire_3 with Dissolve(0.5)
    Claire "Ugh..."
    scene MC_Bathroom_BrushTeeth_Claire_4 with Dissolve(0.5)
    MC "Morning, Claire."
    scene MC_Bathroom_BrushTeeth_Claire_5 with Dissolve(0.5)
    MC "...."
    scene MC_Bathroom_BrushTeeth_Claire_6 with Dissolve(0.5)
    MC "Bitch..."
    scene MC_Bathroom_BrushTeeth_Claire_7 with Dissolve(0.5)
    MC "...."
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}**One hour passes...**"
    $ Location = "washing room"
    $ advance_time_or_sleep()