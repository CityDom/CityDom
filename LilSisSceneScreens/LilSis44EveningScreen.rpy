screen LilSisEveningScreen44():
    add "ScenesScreens/LilSisSceneScreens/LilSis44EveningScreen/LilSisEvening44Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/LilSisSceneScreens/LilSis44EveningScreen/LilSisEvening44Button1_idle.png"
            hover "ScenesScreens/LilSisSceneScreens/LilSis44EveningScreen/LilSisEvening44Button1_hover.png"
            xpos 1699
            ypos 515
            action [Hide("LilSisEveningScreen44"), Jump("LilSisEveningEvent44")]