screen ClaireEveningScreen14():
    add "ScenesScreens/ClaireSceneScreens/Claire14EveningScreen/ClaireEvening14Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/ClaireSceneScreens/Claire14EveningScreen/ClaireEvening14Button1_idle.png"
            hover "ScenesScreens/ClaireSceneScreens/Claire14EveningScreen/ClaireEvening14Button1_hover.png"
            xpos 1302
            ypos 379
            action [Function(hideEventScreens), Jump("ClaireEveningEvent14")]
