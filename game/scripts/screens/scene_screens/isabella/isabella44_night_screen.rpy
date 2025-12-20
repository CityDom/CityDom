screen IsabellaNightScreen44():
    add "ScenesScreens/IsabellaSceneScreens/Isabella44NightScreen/IsabellaNight44Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/IsabellaSceneScreens/Isabella44NightScreen/IsabellaNight44Button1_idle.png"
            hover "ScenesScreens/IsabellaSceneScreens/Isabella44NightScreen/IsabellaNight44Button1_hover.png"
            xpos 753
            ypos 398
            action [Hide("IsabellaNightScreen44"), Jump("IsabellaNightEvent44")]