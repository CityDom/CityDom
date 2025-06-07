init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)
    define_images("MC_Bathroom_BrushTeeth_Claire_", "MCEvents/MC_Bathroom_BrushTeeth/Claire", "MC_Bathroom_BrushTeeth_Claire_", 100)

label MC_Bathroom_BrushTeeth_Claire:
    scene MC_Bathroom_BrushTeeth_Claire_1 with Dissolve(0.5)
    MC "..."
    scene MC_Bathroom_BrushTeeth_Claire_2 with Dissolve(0.5)
    Clair "...."
    scene MC_Bathroom_BrushTeeth_Claire_3 with Dissolve(0.5)
    Clair "Ugh..."
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