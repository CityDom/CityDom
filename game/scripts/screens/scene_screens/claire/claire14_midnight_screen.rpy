screen ClaireMidnightScreen14():
    add "ScenesScreens/ClaireSceneScreens/Claire14MidnightScreen/ClaireMidnight14Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/ClaireSceneScreens/Claire14MidnightScreen/ClaireMidnight14Button1_idle.png"
            hover "ScenesScreens/ClaireSceneScreens/Claire14MidnightScreen/ClaireMidnight14Button1_hover.png"
            xpos 712
            ypos 322
            action [Function(hideEventScreens), Jump("ClaireMidnightEvent14")]
