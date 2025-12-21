screen ClaireEveningScreen44():
    add "ScenesScreens/ClaireSceneScreens/Claire44EveningScreen/ClaireEvening44Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/ClaireSceneScreens/Claire44EveningScreen/ClaireEvening44Button1_idle.png"
            hover "ScenesScreens/ClaireSceneScreens/Claire44EveningScreen/ClaireEvening44Button1_hover.png"
            xpos 626
            ypos 261
            action [Function(hideEventScreens), Jump("ClaireEveningEvent44")]
