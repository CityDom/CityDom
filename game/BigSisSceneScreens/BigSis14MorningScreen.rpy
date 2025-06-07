screen BigSisMorningScreen14():
    add "ScenesScreens/BigSisSceneScreens/BigSis14MorningScreen/BigSisMorning14Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/BigSisSceneScreens/BigSis14MorningScreen/BigSisMorning14Button1_idle.png"
            hover "ScenesScreens/BigSisSceneScreens/BigSis14MorningScreen/BigSisMorning14Button1_hover.png"
            xpos 719
            ypos 277
            action [Hide("BigSisMorningScreen14"), Jump("BigSisMorningEvent14")]