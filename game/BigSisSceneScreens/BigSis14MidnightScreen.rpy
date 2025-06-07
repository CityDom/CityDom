screen BigSisMidnightScreen14():
    add "ScenesScreens/BigSisSceneScreens/BigSis14MidnightScreen/BigSisMidnight14Screen1.webp"
    if not MapScreenShown and not StatsScreenShown:
        imagebutton:
            idle "ScenesScreens/BigSisSceneScreens/BigSis14MidnightScreen/BigSisMidnight14Button1_idle.png"
            hover "ScenesScreens/BigSisSceneScreens/BigSis14MidnightScreen/BigSisMidnight14Button1_hover.png"
            xpos 712
            ypos 322
            action [Hide("BigSisMidnightScreen14"), Jump("BigSisMidnightEvent14")]