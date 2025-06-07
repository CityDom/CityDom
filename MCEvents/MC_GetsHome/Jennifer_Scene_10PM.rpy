init python:
    def define_images(variable_prefix, folder, image_prefix, count):
        for i in range(1, count + 1):
            variable_name = f"{variable_prefix}{i}"
            image_path = f"{folder}/{image_prefix}{i}.webp"
            renpy.image(variable_name, image_path)

    define_images("Jennifer_Scene_10PM_", "MCEvents/MC_GetsHome/Jennifer/10PM", "Jennifer_Scene_10PM_", 100)

label MC_GetsHome_Jennifer_10PM:
    scene Jennifer_Scene_10PM_1 with Dissolve(0.5)
    menu:
        "Knock":
            scene Jennifer_Scene_10PM_2 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_10PM_3 with Dissolve(0.5)
            $ renpy.pause(0.2, hard=True)
            scene Jennifer_Scene_10PM_2 with Dissolve(0.5)
            "{color=#808080}*PLAP PLAP PLAP PLAP*"
            scene Jennifer_Scene_10PM_4 with Dissolve(0.5)
            MC "{color=#808080}*Ughh... I'm fucked...*"
            MC "{color=#808080}*I better take a step back...*"
            scene Jennifer_Scene_10PM_5 with Dissolve(0.5)
            "............"
            MC "Uhhh... sorry mom, I wa-"
            scene Jennifer_Scene_10PM_6 with Dissolve(0.5)
            McMom "Get in the house! Now!"
            scene Jennifer_Scene_10PM_7 with Dissolve(0.5)
            McMom "Wash you hands first then go eat!"
            McMom "The food must be cold by now!"
            scene Jennifer_Scene_10PM_8 with Dissolve(0.5)
            MC "Okay mom..."
            scene Jennifer_Scene_10PM_9 with Dissolve(0.5)
            McMom "And don't be late next time!"
            scene Jennifer_Scene_10PM_10 with Dissolve(0.5)
            McMom "Understood?!"
            scene Jennifer_Scene_10PM_11 with Dissolve(0.5)
            MC "Auch, yeah, I got it..."
            scene BlackScreen with Dissolve(0.5)
            $ Location = "entrance"
            $ renpy.call("GameLoop")
        "Enter":
            $ Location = "entrance"
            $ renpy.call("GameLoop")
