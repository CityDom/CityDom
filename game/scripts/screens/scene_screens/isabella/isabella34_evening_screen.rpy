screen IsabellaEveningScreen34():
    add "ScenesScreens/IsabellaSceneScreens/Isabella34EveningScreen/IsabellaEvening34Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/IsabellaSceneScreens/Isabella34EveningScreen/IsabellaEvening34Button1_idle.png"
            hover "ScenesScreens/IsabellaSceneScreens/Isabella34EveningScreen/IsabellaEvening34Button1_hover.png"
            xpos 663
            ypos 370
            action [Hide("IsabellaEveningScreen34"), Jump("IsabellaEveningEvent34")]