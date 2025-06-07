init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)
    define_images("MC_Bathroom_BrushTeeth_Jennifer_", "MCEvents/MC_Bathroom_BrushTeeth/Jennifer", "MC_Bathroom_BrushTeeth_Jennifer_", 100)

label MC_Bathroom_BrushTeeth_Jennifer:
    scene MC_Bathroom_BrushTeeth_Jennifer_1 with Dissolve(0.5) 
    MC "..."
    scene MC_Bathroom_BrushTeeth_Jennifer_2 with Dissolve(0.5)
    McMom "Ohh"
    McMom "You scared me!"
    scene MC_Bathroom_BrushTeeth_Jennifer_3 with Dissolve(0.5)
    MC "Oh, g'morning mom."
    MC "I didn't mean to scare you. I was just standing here..."
    scene MC_Bathroom_BrushTeeth_Jennifer_4 with Dissolve(0.5)
    McMom "Awww, what's wrong sweetie?"
    McMom "Didn't you sleep well?"
    McMom "Or are you mad at mommy? Did I do something?"
    scene MC_Bathroom_BrushTeeth_Jennifer_5 with Dissolve(0.5)
    MC "No, no, no, nothing like that."
    MC "Isa calls it my morning face..."
    MC "I have to work on that apparently, she says I'm scaring people."
    scene MC_Bathroom_BrushTeeth_Jennifer_6 with Dissolve(0.5)
    McMom "Haha, is that it?"
    McMom "It's okay kiddo, you didn't like waking up early as a kid either."
    scene MC_Bathroom_BrushTeeth_Jennifer_7 with Dissolve(0.5)
    MC "I don't know how you can be so energetic so early in the morning."
    scene MC_Bathroom_BrushTeeth_Jennifer_8 with Dissolve(0.5)
    McMom "Well, you'll get used to it as you become an adult and will have to go to work."
    scene MC_Bathroom_BrushTeeth_Jennifer_9 with Dissolve(0.5)
    MC "I am an adult already, mom..."
    scene MC_Bathroom_BrushTeeth_Jennifer_10 with Dissolve(0.5)
    McMom "You will always be my little boy, sweetie."
    scene MC_Bathroom_BrushTeeth_Jennifer_11 with Dissolve(0.5)
    ".........."
    scene BlackScreen with Dissolve(0.5)
    "{color=#808080}**One hour passes...**"
    $ Location = "washing room"
    $ advance_time_or_sleep()