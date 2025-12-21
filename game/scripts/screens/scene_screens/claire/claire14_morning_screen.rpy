screen ClaireMorningScreen14():
    add "ScenesScreens/ClaireSceneScreens/Claire14MorningScreen/ClaireMorning14Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/ClaireSceneScreens/Claire14MorningScreen/ClaireMorning14Button1_idle.png"
            hover "ScenesScreens/ClaireSceneScreens/Claire14MorningScreen/ClaireMorning14Button1_hover.png"
            xpos 719
            ypos 277
            action [Function(hideEventScreens), Jump("ClaireMorningEvent14")]
