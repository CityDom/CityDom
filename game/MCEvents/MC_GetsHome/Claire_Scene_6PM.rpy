init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)

    define_images("Claire_Scene_6PM_", "MCEvents/MC_GetsHome/Claire/6PM", "Claire_Scene_6PM_", 100)

label MC_GetsHome_Claire_6PM:
    scene Claire_Scene_6PM_4 with Dissolve(0.5)
    menu:
        "Knock":
            scene Claire_Scene_6PM_1 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_1 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_1 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_2 with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
            scene Claire_Scene_6PM_5 with Dissolve(1)
            MC "{color=#808080}*What the fuck is Isa doing?*"
            MC "{color=#808080}*She should be home by now...*"
            scene Claire_Scene_6PM_3 with Dissolve(1)
            Isabella "{color=#808080}*Myeah, no way I'm answering that...*"
            scene Claire_Scene_6PM_5 with Dissolve(1)
            MC "{color=#808080}*Well... I guess I'll be connecting with the nature for a bit...*"
            Clair "Move."
            scene Claire_Scene_6PM_6 with Dissolve(0.5)
            MC "Huh?!"
            scene Claire_Scene_6PM_7 with Dissolve(0.5)
            Clair "I said get the fuck out of my way."
            Clair "I won't repeat myself again."
            scene Claire_Scene_6PM_8 with Dissolve(0.5)
            MC "Ah, shit, Claire!"
            MC "Sorry, I didn't realize it was you!"
            scene Claire_Scene_6PM_9 with Dissolve(0.5)
            Clair "Pay more attention next time."
            scene BlackScreen with Dissolve(0.5)
            MC "...."
            $ Location = "entrance"
            $ advance_time_or_sleep()
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")