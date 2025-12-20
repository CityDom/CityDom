screen IsabellaEveningScreen44():
    add "ScenesScreens/IsabellaSceneScreens/Isabella44EveningScreen/IsabellaEvening44Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/IsabellaSceneScreens/Isabella44EveningScreen/IsabellaEvening44Button1_idle.png"
            hover "ScenesScreens/IsabellaSceneScreens/Isabella44EveningScreen/IsabellaEvening44Button1_hover.png"
            xpos 1699
            ypos 515
            action [Hide("IsabellaEveningScreen44"), Jump("IsabellaEveningEvent44")]