screen BigSisEveningScreen44():
    add "ScenesScreens/BigSisSceneScreens/BigSis44EveningScreen/BigSisEvening44Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/BigSisSceneScreens/BigSis44EveningScreen/BigSisEvening44Button1_idle.png"
            hover "ScenesScreens/BigSisSceneScreens/BigSis44EveningScreen/BigSisEvening44Button1_hover.png"
            xpos 626
            ypos 261
            action [Hide("BigSisEveningScreen44"), Jump("BigSisEveningEvent44")]