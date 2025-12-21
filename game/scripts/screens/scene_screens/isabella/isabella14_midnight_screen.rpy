screen IsabellaMidnightScreen14():
    add "ScenesScreens/IsabellaSceneScreens/Isabella14MidnightScreen/IsabellaMidnight14Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/IsabellaSceneScreens/Isabella14MidnightScreen/IsabellaMidnight14Button1_idle.png"
            hover "ScenesScreens/IsabellaSceneScreens/Isabella14MidnightScreen/IsabellaMidnight14Button1_hover.png"
            xpos 823
            ypos 401
            action [Function(hideEventScreens), Jump("IsabellaMidnightEvent14")]
