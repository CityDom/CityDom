screen IsabellaAfterNoonScreen44():
    add "ScenesScreens/IsabellaSceneScreens/Isabella44AfternoonScreen/IsabellaAfternoon44Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/IsabellaSceneScreens/Isabella44AfternoonScreen/IsabellaAfternoon44Button1_idle.png"
            hover "ScenesScreens/IsabellaSceneScreens/Isabella44AfternoonScreen/IsabellaAfternoon44Button1_hover.png"
            xpos 1263
            ypos 339
            action [Function(hideEventScreens), Jump("IsabellaAfterNoonEvent44")]
