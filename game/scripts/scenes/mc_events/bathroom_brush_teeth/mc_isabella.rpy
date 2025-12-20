init python:
    define_images("MC_Bathroom_BrushTeeth_Isabella_", "MCEvents/MC_Bathroom_BrushTeeth/Isabella", "MC_Bathroom_BrushTeeth_Isabella_", 100)

label MC_Bathroom_BrushTeeth_Isabella:
    scene MC_Bathroom_BrushTeeth_Isabella_1 with Dissolve(0.5)
    MC "..."
    scene MC_Bathroom_BrushTeeth_Isabella_2 with Dissolve(0.5)
    Isabella "YAAAAWWNNNNNNNNN"
    scene MC_Bathroom_BrushTeeth_Isabella_3 with Dissolve(0.5)
    MC "G'morning, Isa."
    scene MC_Bathroom_BrushTeeth_Isabella_4 with Dissolve(0.5)
    Isabella "G'morning, [MC]..."
    scene MC_Bathroom_BrushTeeth_Isabella_5 with Dissolve(0.5)
    MC "You seem pretty lively this morning..."
    scene MC_Bathroom_BrushTeeth_Isabella_6 with Dissolve(0.5)
    Isabella "And you look like you wanna punch me."
    Isabella "You really gotta do something about that morning face of yours."
    Isabella "You scare people."
    scene MC_Bathroom_BrushTeeth_Isabella_7 with Dissolve(0.5)
    MC "Really? Is it that bad?"
    Isabella "Mhm."
    scene MC_Bathroom_BrushTeeth_Isabella_8 with Dissolve(0.5)
    Isabella "...."
    MC "...."
    scene MC_Bathroom_BrushTeeth_Isabella_9 with Dissolve(0.5)
    Isabella "...."
    MC "...."
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}**One hour passes...**"
    $ Location = "washing room"
    $ advance_time_or_sleep()