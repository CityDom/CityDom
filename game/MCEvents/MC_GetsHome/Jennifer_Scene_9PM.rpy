init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)

    define_images("Jennifer_Scene_9PM_", "MCEvents/MC_GetsHome/Jennifer/9PM", "Jennifer_Scene_9PM_", 100)

label MC_GetsHome_Jennifer_9PM:
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
            scene Jennifer_Scene_9PM_1 with Dissolve(0.5)
            "{color=#808080}*KNOCK KNOCK KNOCK!!!*"
            scene Jennifer_Scene_9PM_2 with Dissolve(0.5)
            McMom "KIDS!!! CAN ONE OF YOU CHECK ON THE DOOR?!"
            scene Jennifer_Scene_9PM_3 with Dissolve(0.5)
            McMom "........"
            scene Jennifer_Scene_9PM_4 with Dissolve(0.5)
            McMom "God damn it..."
            scene Jennifer_Scene_9PM_5 with Dissolve(0.5)
            McMom "I'm doing everything in this house and no one ever help me!"
            scene Jennifer_Scene_9PM_6 with Dissolve(0.5)
            "{color=#808080}*PLAP PLAP PLAP PLAP*"
            scene Jennifer_Scene_9PM_7 with Dissolve(0.5)
            MC "{color=#808080}*Ah shit... that gotta be mom... and she isn't happy.*"
            scene Jennifer_Scene_9PM_8 with Dissolve(0.5)
            McMom "Get in already, I have food on the stove!"
            McMom "Bring a damn key with you, will you?!"
            scene Jennifer_Scene_9PM_9 with Dissolve(0.5)
            MC "Uhh... I have it... Y'all just leave the key in the do-"
            scene Jennifer_Scene_9PM_10 with Dissolve(0.5)
            McMom "I DON'T WANNA HEAR IT!!"
            scene BlackScreen with Dissolve(0.5)
            $ Location = "entrance"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")
